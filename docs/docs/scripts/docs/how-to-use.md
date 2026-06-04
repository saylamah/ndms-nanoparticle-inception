# How to Use This Repository

This repository provides companion materials for the transient nano-dense molecular state (NDMS) hypothesis and the persistence–stabilization closure for combustion nanoparticle inception.

The current executable example is a zero-dimensional demonstration of the NDMS persistence–stabilization model.

## Current Script

```text
scripts/ndms_zero_dimensional_model.py
```

This script demonstrates how the particle-inception source depends on the competition between:

* transient precursor association,
* cluster dissociation,
* non-stabilizing loss,
* chemical or structural stabilization.

## Model Quantities

The script evaluates the bounded stabilization probability:

```text
P_stab = k_stab / (k_off + k_loss + k_stab)
```

and the reduced NDMS inception source:

```text
S_NDMS = k_stab * k_on * C_assoc^m / (k_off + k_loss + k_stab)
```

where:

* `k_on` is the effective association coefficient,
* `C_assoc` is the association-weighted precursor descriptor,
* `m` is the apparent precursor-pool order,
* `k_off` is the dissociation coefficient,
* `k_loss` is the non-stabilizing loss coefficient,
* `k_stab` is the stabilization coefficient.

## Running the Script

After downloading or cloning the repository, run:

```bash
python scripts/ndms_zero_dimensional_model.py
```

No external Python packages are required for this first demonstration.

## Demonstration Cases

The script compares three illustrative cases:

1. **Rapid removal**
   Dissociation and loss dominate over stabilization.

2. **Comparable loss and stabilization**
   Stabilization competes with dissociation and loss.

3. **Strong stabilization**
   Stabilization dominates, leading to a high persistence probability.

## Expected Output

The script prints a table similar to:

```text
NDMS zero-dimensional persistence-stabilization demonstration
------------------------------------------------------------------------
Case                                      P_stab       S_NDMS
------------------------------------------------------------------------
Rapid removal                             0.0090       0.0090
Comparable loss and stabilization          0.5000       0.5000
Strong stabilization                       0.9901       0.9901
```

## Scientific Interpretation

The demonstration shows that transient clustering alone is not sufficient for nanoparticle inception.

Even when precursor association occurs, persistent particle formation depends on whether stabilization can compete successfully with dissociation and other losses.

This reflects the central idea of the NDMS persistence–stabilization closure: particle inception should be treated as a structured competition between reversible local densification and persistence-generating stabilization.

## Status

This is a first reduced demonstration. Future additions may include:

* parameter-sensitivity studies,
* plots of stabilization probability,
* Jupyter notebooks,
* comparison with direct empirical nucleation forms,
* links to population-balance or moment-method implementations.
