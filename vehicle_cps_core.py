import numpy as np
import matplotlib.pyplot as plt

class VehicleCPSSimulator:
    """
    VEHICLE-CPS: Civil Protection Systems Architecture.
    Based on the Borda Milan Pyramid and Formula-as-Architecture.
    Author: Roberto Borda Milan | ORCID: 0009-0009-9047-1036
    """
    def __init__(self, n_nodes=1000, t_limit=0.5, lambda_param=0.2):
        self.n = n_nodes
        self.t_limit = t_limit
        self.lambd = lambda_param
        
        # 1. INITIALIZATION: E.I.A.R.(V) Structured Nodes[cite: 1]
        # E (Orientation), I (Information), A (Coupling), R (Relational), V (Verification)
        self.X = np.random.normal(0.5, 0.05, (self.n, 5)).astype(np.float32)
        
        # 2. OPERATOR: P- Centering Matrix for Internal Coherence[cite: 1]
        self.P_minus = np.eye(5) - (1/5) * np.ones((5, 5))
        
        # 3. METRICS & TAXONOMY[cite: 1]
        self.p_labels = ["P0: Rest", "P1: Flow", "P2: Review", "P3: Concentration", 
                         "P4: Breach", "P5: Reinforce", "P6: Evacuate"]
        self.history = {'entropy': [], 'max_tension': []}

    def compute_metrics(self):
        """Calculates Internal Incoherence O(S) and External Tension T(X)[cite: 1]"""
        centered = self.X @ self.P_minus
        internal_t = np.sum(centered**2, axis=1)
        external_t = np.linalg.norm(self.X - np.mean(self.X, axis=0), axis=1)
        return internal_t, external_t

    def classify_attractors(self, combined_tension):
        """Maps continuous tension to P0-P6 operational taxonomy[cite: 1]"""
        indices = np.clip((combined_tension * 3).astype(int), 0, 6)
        return indices

    def inject_tension_type_1(self, magnitude=3.0):
        """Simulates a critical Type 1 Tension: Perimeter Breach[cite: 1]"""
        print(f"\n[ALERT] Injecting Type 1 Tension: Magnitude {magnitude}")
        sector = np.random.choice(self.n, self.n // 5, replace=False)
        self.X[sector] += np.random.uniform(-magnitude, magnitude, (self.n // 5, 5))

    def step(self, eta=0.08):
        """Projection-Governed Step (Layer 5: Governance)[cite: 1]"""
        grad_int = self.X @ self.P_minus
        grad_ext = self.X - np.mean(self.X, axis=0)
        
        # Total Functional Gradient[cite: 1]
        Z = self.X - eta * (grad_ext + self.lambd * grad_int)
        
        # V_op: Projection onto Admissible Coherent Region K[cite: 1]
        incoherence = np.sum((Z @ self.P_minus)**2, axis=1)
        mask = incoherence > self.t_limit
        factors = np.ones(self.n)
        factors[mask] = np.sqrt(self.t_limit / incoherence[mask])
        
        self.X = Z * factors[:, np.newaxis]
        
        # Entropy Logging for Scientific Review
        self.history['entropy'].append(-np.sum(incoherence * np.log(incoherence + 1e-9)) / self.n)

    def visualize_dashboard(self, phase_name):
        """Scientific Visualization for Google Deep Tech Review[cite: 1]"""
        int_t, ext_t = self.compute_metrics()
        combined = int_t + ext_t
        attractors = self.classify_attractors(combined)
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        fig.suptitle(f"VEHICLE-CPS Framework: {phase_name}", fontsize=16)

        # Plot A: EIARV Projection Field[cite: 1]
        scatter = ax1.scatter(ext_t, int_t, c=combined, cmap='viridis', s=15)
        ax1.axhline(y=self.t_limit, color='r', linestyle='--', label='K-Limit (Admissibility)')
        ax1.set_xlabel("External Relational Tension")
        ax1.set_ylabel("Internal Incoherence (EIARV)")
        ax1.legend()
        ax1.grid(True, alpha=0.2)

        # Plot B: Operational Taxonomy Distribution (P0-P6)[cite: 1]
        ax2.hist(attractors, bins=range(8), rwidth=0.8, color='teal', align='left')
        ax2.set_xticks(range(7))
        ax2.set_xticklabels(self.p_labels, rotation=45)
        ax2.set_title("Operational Dashboard (Alert Levels)")

        plt.tight_layout()
        plt.show()

# --- EXPERIMENTAL PROTOCOL ---
if __name__ == "__main__":
    # Initialize simulation with 1,000 nodes (Optimized for legacy hardware)[cite: 1]
    sim = VehicleCPSSimulator(n_nodes=1000)

    # PHASE 1: Baseline (Stability)
    sim.step()
    sim.visualize_dashboard("Baseline Stability (Normal Flow)")

    # PHASE 2: Critical Incident (Type 1 Tension Injection)[cite: 1]
    sim.inject_tension_type_1(magnitude=2.8)
    sim.visualize_dashboard("Critical Anomaly (Detection of P4 Breach)")

    # PHASE 3: Mathematical Governance (Recovery)[cite: 1]
    print("[INFO] Applying VEHICLE Projection Governance...")
    for _ in range(20): 
        sim.step()
    sim.visualize_dashboard("Recovery & Re-stabilization (K-Region)")