"""Run a minimal VEHICLE-CPS synthetic demonstration."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from vehicle_cps_core import run_demo


if __name__ == "__main__":
    result = run_demo(n_nodes=1000, steps=5, seed=7)
    for row in result["history"]:
        print(
            f"step={row['step']} nodes={row['nodes']} edges={row['edges']} "
            f"tension={row['total_tension']:.4f} "
            f"mean_incoherence={row['mean_incoherence']:.4f} regime={row['regime']}"
        )
