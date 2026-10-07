# Kata library

Canonical copy. Transferable methods, not facts. Test before adding: could this be pattern-matched onto an unrelated object and still tell you what to look for.

Tier 1, structural kata: cross-theory proof patterns. Format: trigger, steps, what each step buys, known instances, epistemic status of the synthesis.
Tier 2, technique kata: standard calculation moves. One line: trigger -> move -> why.

Epistemic marks: ⊢ proved, ⊨ source-supported, ≃ inference, ∃? unverified, ↦ proposed method, ⊥ error.

## Tier 1

### Signed-point-count invariant (Fredholm triad)

Trigger: a topological invariant defined by counting points in a moduli space with signs.

1. Elliptic linearization of the defining equations. Fredholm index gives dim(moduli space) via index theorem or spectral flow.
2. Weitzenböck-type identity. Buys compactness, so the count is finite and independent of auxiliary choices.
3. Trivialize the determinant line of the linearized operator (complex orientation, Ray-Singer-Quillen, or spectral flow along a path). Gives the sign of each point.

Why: (1) right dimension for a point count; (2) without it the count diverges or depends on metric/perturbation; (3) without it ∂²=0 and orientability fail.

Instances ⊨:
- Morse homology: Hessian index, Morse-Smale transversality, orientations of descending manifolds. Hutchings, *Lecture notes on Morse homology*, 2002, §2-5.
- Seiberg-Witten on 4-manifolds: Dirac index, Weitzenböck identity, Ray-Singer-Quillen sign. Witten, *Monopoles and Four-Manifolds*, hep-th/9411102.
- Hamiltonian/Lagrangian Floer: Conley-Zehnder index via spectral flow, Gromov compactness, coherent orientations (Floer-Hofer 1993).
- ECH: ECH index, obstruction bundle gluing.
- Instanton/SW Floer on 3-manifolds: spectral flow along trajectories. Kronheimer-Mrowka ch.14.2; Robbin-Salamon, *The spectral flow and the Maslov index*, 1995.

Status ≃: instances are individually source-confirmed; the three-step unification is a generated synthesis. Open test: Gromov-Witten invariants.

## Tier 2

- Nonlinear ODE/PDE, cubic or quintic term, traveling-wave reduction -> ansatz A·tanh(Bξ) or sech(Bξ) -> tanh' = 1 - tanh², sech' = -sech·tanh close the derivatives, nonlinear terms become polynomial in one variable.
- Integral with √(a²-x²), √(a²+x²), √(x²-a²) -> x = a·sinθ, a·tanθ, a·secθ -> the radical becomes a single trig factor.
- Definite integral on [-a,a] -> check parity first -> odd gives 0, even gives 2∫₀ᵃ.
- Oscillatory integral with a stationary phase point -> stationary phase / saddle point -> contribution localizes at critical points of the phase; same machinery as WKB.

## Prompts and agent specs

See RULES_for_other_models.txt.

## Changelog

- 2026-10-06 repo created. Tier 1: Fredholm triad. Tier 2: four entries.
