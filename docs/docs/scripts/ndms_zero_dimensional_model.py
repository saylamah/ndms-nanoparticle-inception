"""
Zero-dimensional NDMS persistence-stabilization demonstration.

This script illustrates the reduced transient nano-dense molecular state
(NDMS) closure for nanoparticle inception.

The model separates:
- precursor association,
- transient NDMS reservoir formation,
- dissociation,
- non-stabilizing loss,
- chemical or structural stabilization.

Author: Ahmad Saylam
Repository: ndms-nanoparticle-inception
"""

from dataclasses import dataclass


@dataclass
class NDMSCase:
    name: str
    k_on: float
    c_assoc: float
    m: float
    k_off: float
    k_loss: float
    k_stab: float


def stabilization_probability(k_off: float, k_loss: float, k_stab: float) -> float:
    """Return bounded stabilization probability."""
    denominator = k_off + k_loss + k_stab
    if denominator <= 0:
        raise ValueError("The sum of k_off, k_loss, and k_stab must be positive.")
    return k_stab / denominator


def ndms_source(case: NDMSCase) -> float:
    """Return quasi-steady NDMS inception source term."""
    formation_rate = case.k_on * case.c_assoc**case.m
    denominator = case.k_off + case.k_loss + case.k_stab
    if denominator <= 0:
        raise ValueError("The sum of k_off, k_loss, and k_stab must be positive.")
    z_reservoir = formation_rate / denominator
    return case.k_stab * z_reservoir


def main() -> None:
    cases = [
        NDMSCase(
            name="Rapid removal",
            k_on=1.0,
            c_assoc=1.0,
            m=1.0,
            k_off=10.0,
            k_loss=1.0,
            k_stab=0.1,
        ),
        NDMSCase(
            name="Comparable loss and stabilization",
            k_on=1.0,
            c_assoc=1.0,
            m=1.0,
            k_off=0.7,
            k_loss=0.3,
            k_stab=1.0,
        ),
        NDMSCase(
            name="Strong stabilization",
            k_on=1.0,
            c_assoc=1.0,
            m=1.0,
            k_off=0.05,
            k_loss=0.05,
            k_stab=10.0,
        ),
    ]

    print("NDMS zero-dimensional persistence-stabilization demonstration")
    print("-" * 72)
    print(f"{'Case':35s} {'P_stab':>12s} {'S_NDMS':>12s}")
    print("-" * 72)

    for case in cases:
        p_stab = stabilization_probability(case.k_off, case.k_loss, case.k_stab)
        source = ndms_source(case)
        print(f"{case.name:35s} {p_stab:12.4f} {source:12.4f}")


if __name__ == "__main__":
    main()
