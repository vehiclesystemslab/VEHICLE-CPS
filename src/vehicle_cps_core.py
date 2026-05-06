"""
VEHICLE-CPS core utilities.

Minimal synthetic simulation helpers for Civil Protection Systems experiments.
This module is intentionally simple and reproducible. It is not an operational
safety system and must not be used for real-world deployment without legal,
ethical, institutional, and technical review.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, Tuple

import networkx as nx
import numpy as np


class Regime(str, Enum):
    P0 = "P0_STRUCTURAL_REST"
    P1 = "P1_CONTROLLED_NORMAL_FLOW"
    P2 = "P2_LOCALIZED_REVIEW"
    P3 = "P3_ANOMALOUS_CONCENTRATION"
    P4 = "P4_CRITICAL_INCOHERENCE"
    P5 = "P5_REINFORCEMENT_CONTAINMENT"
    P6 = "P6_CONTROLLED_EVACUATION"


@dataclass(frozen=True)
class CPSParameters:
    """Parameters for a synthetic VEHICLE-CPS experiment."""

    lambda_internal: float = 0.35
    coherence_limit: float = 1.25
    gamma: float = 0.08
    alpha: float = 0.35
    p2_threshold: float = 0.35
    p3_threshold: float = 0.65
    p4_threshold: float = 0.95
    p6_threshold: float = 1.35


def create_synthetic_event_graph(n_nodes: int = 1000, radius: float = 0.085, seed: int = 7) -> nx.Graph:
    """Create a random geometric graph representing a synthetic human event field."""
    rng = np.random.default_rng(seed)
    positions = {i: tuple(rng.random(2)) for i in range(n_nodes)}
    graph = nx.random_geometric_graph(n_nodes, radius=radius, pos=positions, seed=seed)
    for node, pos in positions.items():
        graph.nodes[node]["pos"] = np.array(pos, dtype=float)
    return graph


def initialize_states(graph: nx.Graph, seed: int = 7) -> np.ndarray:
    """Initialize E.I.A.R.(V)-style structured node states in R^5."""
    rng = np.random.default_rng(seed)
    n = graph.number_of_nodes()
    states = rng.normal(loc=0.0, scale=0.22, size=(n, 5))

    # Add mild environmental structure: nodes near the center have slightly
    # higher exposure and coupling, representing crowd density effects.
    for i in graph.nodes:
        pos = graph.nodes[i].get("pos", np.array([0.5, 0.5]))
        center_pressure = 1.0 - min(1.0, np.linalg.norm(pos - np.array([0.5, 0.5])) * 2.0)
        states[i, 0] += 0.45 * center_pressure  # E: exposure
        states[i, 2] += 0.25 * center_pressure  # A: active coupling
    return states


def internal_incoherence(states: np.ndarray) -> np.ndarray:
    """Compute per-node incoherence by removing each node's component mean."""
    centered = states - states.mean(axis=1, keepdims=True)
    return np.linalg.norm(centered, axis=1)


def external_tension(graph: nx.Graph, states: np.ndarray) -> float:
    """Compute graph relational tension as sum of squared state differences."""
    total = 0.0
    for i, j in graph.edges:
        diff = states[i] - states[j]
        total += float(np.dot(diff, diff))
    return total


def total_tension(graph: nx.Graph, states: np.ndarray, params: CPSParameters = CPSParameters()) -> float:
    """Compute total VEHICLE-CPS tension."""
    t_ext = external_tension(graph, states)
    t_int = params.lambda_internal * float(np.sum(internal_incoherence(states) ** 2))
    return t_ext + t_int


def classify_regime(graph: nx.Graph, states: np.ndarray, params: CPSParameters = CPSParameters()) -> Regime:
    """Classify the synthetic event field into a P0-P6 operational regime."""
    n = max(1, graph.number_of_nodes())
    normalized_degree = np.mean([degree for _, degree in graph.degree()]) / max(1.0, np.sqrt(n))
    incoherence = float(np.mean(internal_incoherence(states)))
    score = 0.55 * normalized_degree + 0.45 * incoherence

    if score < params.p2_threshold:
        return Regime.P1 if graph.number_of_edges() else Regime.P0
    if score < params.p3_threshold:
        return Regime.P2
    if score < params.p4_threshold:
        return Regime.P3
    if score < params.p6_threshold:
        return Regime.P4
    return Regime.P6


def projected_update(states: np.ndarray, params: CPSParameters = CPSParameters()) -> np.ndarray:
    """Apply a simple projected correction toward internal coherence.

    This is a compact demonstrator of the VEHICLE idea. It pulls each node's
    state toward its internal component mean and clips the result into an
    admissible coherence region.
    """
    means = states.mean(axis=1, keepdims=True)
    gradient = states - means
    corrected = states - params.gamma * gradient
    relaxed = (1.0 - params.alpha) * states + params.alpha * corrected

    incoh = internal_incoherence(relaxed)
    scale = np.ones_like(incoh)
    mask = incoh > params.coherence_limit
    scale[mask] = params.coherence_limit / np.maximum(incoh[mask], 1e-9)
    centered = relaxed - relaxed.mean(axis=1, keepdims=True)
    return relaxed.mean(axis=1, keepdims=True) + centered * scale[:, None]


def run_demo(n_nodes: int = 1000, steps: int = 5, seed: int = 7) -> Dict[str, object]:
    """Run a small synthetic VEHICLE-CPS demonstration."""
    graph = create_synthetic_event_graph(n_nodes=n_nodes, seed=seed)
    states = initialize_states(graph, seed=seed)
    params = CPSParameters()

    history = []
    for step in range(steps + 1):
        history.append(
            {
                "step": step,
                "nodes": graph.number_of_nodes(),
                "edges": graph.number_of_edges(),
                "total_tension": total_tension(graph, states, params),
                "mean_incoherence": float(np.mean(internal_incoherence(states))),
                "regime": classify_regime(graph, states, params).value,
            }
        )
        if step < steps:
            states = projected_update(states, params)
    return {"parameters": params.__dict__, "history": history}


if __name__ == "__main__":
    result = run_demo(n_nodes=1000, steps=5, seed=7)
    for row in result["history"]:
        print(row)
