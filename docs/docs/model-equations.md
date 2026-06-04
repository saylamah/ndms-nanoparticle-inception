# Model Equations

## NDMS Persistence–Stabilization Closure

This document summarizes the reduced mathematical structure of the transient nano-dense molecular state (NDMS) persistence–stabilization closure for combustion nanoparticle inception.

The purpose is to separate the early molecular-to-particle transition into physically interpretable steps rather than treating inception as a single empirical nucleation event.

## 1. Local Density Enhancement

An NDMS-like reservoir is associated with a local enhancement of precursor number density:

```math
\chi_{\rho} =
\frac{\rho_{P,\mathrm{NDMS}}}{\rho_{P,\mathrm{gas}}}
```

where:

* `rho_P,NDMS` is the effective precursor number density inside the transient locally dense ensemble,
* `rho_P,gas` is the surrounding gas-phase precursor number density,
* `chi_rho` is an operational local-density enhancement factor.

The NDMS condition may be written as:

```math
\chi_{\rho} > \chi_{\rho,\mathrm{crit}}
```

This criterion does not imply a new equilibrium condensed phase. It only indicates that precursor units experience a locally enhanced encounter environment relative to the surrounding gas phase.

## 2. Association-Weighted Precursor Descriptor

The precursor pool responsible for reversible association is represented by an association-weighted descriptor:

```math
C_P^{\mathrm{assoc}} =
\sum_i w_i^{\mathrm{assoc}} C_i
```

where:

* `C_i` is the concentration of precursor class `i`,
* `w_i_assoc` is the association weight of precursor class `i`,
* `C_P_assoc` controls the formation of the transient NDMS reservoir.

For soot, this descriptor may include compact PAHs, peri-condensed PAHs, high-mass aromatic species, and other species with strong dispersion or π-stacking interactions.

## 3. Stabilization-Weighted Precursor Descriptor

The precursor pool or reactive environment responsible for chemical or structural stabilization is represented by:

```math
C_P^{\mathrm{stab}} =
\sum_i w_i^{\mathrm{stab}} C_i
```

where:

* `w_i_stab` is the stabilization weight of precursor class `i`,
* `C_P_stab` controls conversion of transient clusters into persistent incipient particles.

For soot, this may emphasize radical PAHs, resonance-stabilized radicals, covalently linked intermediates, hydrogen-loss pathways, aromatization, and chemical aging.

## 4. Formation of the Transient NDMS Reservoir

A reduced reservoir formation rate can be written as:

```math
R_{\mathrm{form}} =
k_{\mathrm{on}} \left(C_P^{\mathrm{assoc}}\right)^m
```

where:

* `k_on` is an effective association coefficient,
* `m` is an apparent precursor-pool order,
* `R_form` is the net formation rate of the transient NDMS reservoir.

## 5. One-Reservoir NDMS Balance

In the simplest zero-dimensional form, the transient NDMS reservoir `Z` obeys:

```math
\frac{dZ}{dt}
=
k_{\mathrm{on}} \left(C_P^{\mathrm{assoc}}\right)^m
-
k_{\mathrm{off}} Z
-
k_{\mathrm{loss}} Z
-
k_{\mathrm{stab}} Z
```

or equivalently:

```math
\frac{dZ}{dt}
=
R_{\mathrm{form}}
-
R_{\mathrm{diss}}
-
R_{\mathrm{loss}}
-
R_{\mathrm{stab}}
```

where:

* `Z` is the transient NDMS reservoir,
* `k_off` is the effective dissociation coefficient,
* `k_loss` is the effective non-stabilizing loss coefficient,
* `k_stab` is the effective stabilization coefficient.

The key point is that transient clustering alone does not create persistent particles. Only the stabilization flux transfers material or number into the persistent particle population.

## 6. Persistence–Stabilization Number

The competition between stabilization and removal can be expressed using a persistence–stabilization number:

```math
Da_{\mathrm{PS}}
=
\frac{k_{\mathrm{stab}}}{k_{\mathrm{off}} + k_{\mathrm{loss}}}
```

Interpretation:

* If `Da_PS << 1`, dissociation and loss dominate. The transient reservoir disappears before significant particle inception.
* If `Da_PS >= 1`, stabilization competes effectively with dissociation and loss. Persistent particle formation becomes more likely.

## 7. Bounded Stabilization Probability

The corresponding bounded stabilization probability is:

```math
P_{\mathrm{stab}}
=
\frac{k_{\mathrm{stab}}}
{k_{\mathrm{off}} + k_{\mathrm{loss}} + k_{\mathrm{stab}}}
```

or:

```math
P_{\mathrm{stab}}
=
\frac{Da_{\mathrm{PS}}}{1 + Da_{\mathrm{PS}}}
```

This probability remains between 0 and 1 and provides a physically interpretable way to express the fraction of transient NDMS clusters that become persistent incipient particles.

## 8. Quasi-Steady Zero-Dimensional Source Term

Under a quasi-steady approximation for the transient reservoir:

```math
\frac{dZ}{dt} \approx 0
```

the reservoir becomes:

```math
Z =
\frac{
k_{\mathrm{on}} \left(C_P^{\mathrm{assoc}}\right)^m
}
{
k_{\mathrm{off}} + k_{\mathrm{loss}} + k_{\mathrm{stab}}
}
```

The NDMS-based inception source is then:

```math
S_{\mathrm{NDMS}}
=
k_{\mathrm{stab}} Z
```

or:

```math
S_{\mathrm{NDMS}}
=
\frac{
k_{\mathrm{stab}} k_{\mathrm{on}} \left(C_P^{\mathrm{assoc}}\right)^m
}
{
k_{\mathrm{off}} + k_{\mathrm{loss}} + k_{\mathrm{stab}}
}
```

This expression shows the central behavior of the NDMS closure: two systems with similar precursor association rates can produce different particle-inception sources if their dissociation, loss, and stabilization rates differ.

## 9. Conceptual Interpretation

The NDMS closure separates three levels:

1. **Gas-phase precursor descriptors**
   Association- and stabilization-weighted precursor pools.

2. **Transient NDMS reservoir**
   A reversible, locally dense, non-equilibrium pre-particle reservoir.

3. **Persistent incipient particle source**
   Formation of stable particles only through chemical or structural stabilization.

This structure allows the inception process to be represented as a competition between reversible clustering and persistence-generating stabilization.

## 10. Scope

The equations are intended as a reduced modeling framework. They are not proposed as universal kinetic constants or as proof of a new thermodynamic phase.

The parameters must be constrained for each system using suitable diagnostics, molecular simulations, detailed chemistry, population-balance modeling, or experimental particle-inception observables.
