# How to Use This Repository

This repository provides companion materials for the transient nano-dense molecular state (NDMS) hypothesis and the persistence–stabilization closure for combustion nanoparticle inception.

## Installation

The standalone Python script requires only the standard Python interpreter.

The Jupyter notebook uses:

* `numpy`
* `pandas`
* `matplotlib`

To install the required packages, run:

```bash
pip install -r requirements.txt
```

## Current Script

```text
scripts/ndms_zero_dimensional_model.py
```

This script demonstrates how the particle-inception source depends on the competition between:

* transient precursor association,
* cluster dissociation,
* non-stabilizing loss,
* chemical or structural stabilization.

## Running the Script

After downloading or cloning the repository, run:

```bash
python scripts/ndms_zero_dimensional_model.py
```

No external Python packages are required for the standalone script.

## Current Notebook

```text
notebooks/01_persistence_stabilization_demo.ipynb
```

The notebook provides an interactive demonstration of the same reduced NDMS persistence–stabilization model. It includes equations, illustrative cases, and plots.

## Model Quantities

The demonstration evaluates the bounded stabilization probability:

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

## Demonstration Cases

The examples compare three illustrative regimes:

1. **Rapid removal**
   Dissociation and loss dominate over stabilization.

2. **Comparable loss and stabilization**
   Stabilization competes with dissociation and loss.

3. **Strong stabilization**
   Stabilization dominates, leading to a high persistence probability.

## Scientific Interpretation

The demonstration shows that transient clustering alone is not sufficient for nanoparticle inception.

Even when precursor association occurs, persistent particle formation depends on whether stabilization can compete successfully with dissociation and other losses.

This reflects the central idea of the NDMS persistence–stabilization closure: particle inception should be treated as a structured competition between reversible local densification and persistence-generating stabilization.

## Status

This is a first reduced demonstration. Future additions may include:

* parameter-sensitivity studies,
* additional plots of stabilization probability,
* comparison with direct empirical nucleation forms,
* population-balance or moment-method extensions.
