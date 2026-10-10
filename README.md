# Hamiltonian fixed points below the stable Morse number in dimension ten

This repository contains a paper and the computations behind it. The main theorem gives a
simply connected closed **Kähler manifold of real dimension 10** with a nondegenerate Hamiltonian
diffeomorphism that has fewer fixed points than the stable Morse number. Earlier simply connected
examples, in two OpenAI preprints from October 2026, live in real dimensions 22 and 3332. We
also show that no simply connected example exists in real dimension 6. In real dimension 8 we
prove that every known construction method fails.

The results were found and checked by **Claude (Anthropic) agents** working under the
direction of the repository owner, [AUTHOR NAME]. **No human peer review has taken place, and
nothing here is formalized in Lean.** See [Status and caveats](#status-and-caveats) before you
rely on any statement.

**Paper:** [*Hamiltonian fixed points below the stable Morse number in dimension ten, and an
obstruction in dimension six*](paper/main.pdf) ([LaTeX source](paper/main.tex), [build
instructions](paper/README.md)).

## Background

For a closed manifold `W`, let `λ(W) = b(W) + 2 Σ_i d(Tor H_i(W;ℤ))`. Here `b` is the total
rational Betti number and `d` is the minimal number of generators. The stable Morse number
satisfies `SM(W) ≥ λ(W)`, and Smale's theorem gives equality for simply connected `W` of
dimension at least 6. The stable form of the Arnold conjecture asks whether every
nondegenerate Hamiltonian diffeomorphism has at least `SM(M)` fixed points (Golovko 2020,
Conj. 1.2). Bai and Xu proved the integral lower bound
`rank H_*(M;ℚ) + 2 Σ_{i ∈ ℤ/2N} τ_i^{(2N)}(M)`, where `N` is the minimal Chern number and
torsion in degrees congruent mod `2N` is lumped together. OpenAI's preprints showed that the
stable bound can fail.

## What is proved

| Real dim. | Statement | Kind of proof |
| --- | --- | --- |
| 6 | No simply connected counterexample: for simply connected `M⁶` the Bai–Xu bound equals `λ(M) = SM(M)` (**Proposition 3.1**). | paper; uses Bai–Xu and Smale |
| 8 | No counterexample from a **finite-order element of a Hamiltonian torus action, perturbed** (**Theorem B**). This covers all constructions known to us. For **any** Hamiltonian map of prime order, a counterexample needs a fixed component with `ℤ/PQ`-torsion in a single degree (**Proposition 6.8**, using Bai–Shelukhin–Wilkins–Xu). Real dimension 8 remains open in general. | paper |
| 10 | **Kähler counterexample**: `#Fix = λ(M) − 4 = 520 < 524 = λ(M) ≤ SM(M)`, all fixed points nondegenerate and contractible. `#Fix` equals the Bai–Xu bound, so that bound is attained (**Theorem A**). | paper, plus computations |
| 12, 16 | Further Kähler examples (remarks). | paper, plus computations |

So, **among simply connected closed symplectic manifolds of dimension at least 6, the minimal
real dimension of a counterexample is 8 or 10**. Dimension 2 is excluded (`S²`). In simply
connected dimension 4, the Bai–Xu bound equals `b(M) = λ(M)`, so a counterexample would need
`SM(M) > λ(M)`. We do not settle this.

For non-simply-connected manifolds, OpenAI's September 2026 preprint *A nondegenerate
counterexample to the Morse-number Arnold bound* already gives a 12-dimensional example with
`π₁ = A₅^k`, for the ordinary Morse number.

### The ten-dimensional example (Theorem A)

1. **A Brauer threefold with a Z/5 symmetry.** Take the web of quadrics in `P³` given by
   ```
   M(x) = [[6x₀, 5x₁, 4x₂, 0  ],
           [5x₁, 8x₂, 0,   4x₃],
           [4x₂, 0,   7x₃, 6x₀],
           [0,   4x₃, 6x₀, 5x₁]]
   ```
   It is invariant under `Z/5`, acting with weights `(0,4,3,1)`.
   - The quartic symmetroid `det M = 0` has exactly 10 nodes.
   - The web satisfies Beauville's hypotheses for the Artin–Mumford construction (checked
     exactly in Sage).
   - The resulting Artin–Mumford threefold `AM₅` has `Tor H³ = ℤ/2`, and `Z/5` acts on it with
     4 isolated fixed points.
2. **F and S.** Let `F = res(AM₅/Z₅)`.
   - `F` is simply connected, with `Tor H₂(F) = Tor H₃(F) = ℤ/2`. Proving that the
     5-torsion vanishes is the main topological step.
   - `F` contains a smooth divisor `S = π⁻¹(G)/Z₅` with `π₁(S) = ℤ/5`, where `G` is a
     `Z/5`-invariant quintic surface.
3. **A transverse center.**
   - Let `Y` be OpenAI's surface (`P¹×P¹` blown up at four points) and `M = Bl_W(F × Y)`,
     where `W = S × (L₀ ⊔ L₂)` and `L₀, L₂` are two disjoint invariant lines in `Y`.
   - Because `W` meets the fixed locus of the involution cleanly, along `S`, the blow-up
     creates no new fixed components.
   - Each fixed component becomes `Bl_{S×pt}(F × P¹)`. Inside it, the 2-torsion of `F` and
     the 5-torsion of `S` occupy the same degrees. In `M` they occupy different degrees.
     This saves 4 critical points.

## Repository layout

- `paper/`: LaTeX source, bibliography and PDF.
- `computations/`: everything the paper computes by machine. `computations/run_all.sh` runs it
  all.
  - `homology/`: integral homology and `λ` for the examples in real dimensions 10, 12 and 16.
    There are two independent implementations: a torsion-profile calculator (`lam.py`, `w10.py`,
    `x12.py`) and an explicit abelian-group calculation (`indep.py`, `m10_indep.py`).
  - `sage/`: the invariant web and its 10 nodes (`q10.sage`); Beauville's hypotheses
    (`beauville_ii.sage`); defect 0 of the double solid, giving `b₂(AM₅) = 11`
    (`defect2.sage`); the toric resolution of `1/5(1,1,4)`, giving `b(F) = 40` (`bF2.sage`);
    the search over invariant webs (`symm.sage`).
  - `milp/`: a mixed-integer classification of the fixed-point torsion data that the
    torus-action method can produce (Appendix A). It is corroboration only, not part of any
    proof.
- `verification/`: mock reviews by AI agents and the fixes applied in response.

Requirements: Python 3 (homology), Python 3 with SciPy ≥ 1.9 (MILP), SageMath ≥ 9.5 (sage).

## Status and caveats

- **No human peer review.** The paper has not been submitted or refereed. The reviews in
  [`verification/`](verification/) were written by AI agents and are not peer review.
- **Not formalized.** The proofs rest on results that Mathlib does not contain:
  - blow-up homology and Smith theory;
  - Smale's handle theorem;
  - Bai–Xu's integral Floer bound;
  - Artin–Mumford/Beauville;
  - Li's π₁ theorem.

  Only finite computations are machine-checked, by the scripts above.
- **Inputs taken from the literature.**
  - Theorem A uses Smale's theorem in dimension 8 (Amer. J. Math. 84 (1962), Thm 6.1). We know
    its statement from secondary sources and have not seen the original wording.
  - `Tor H³(AM₅) ⊇ ℤ/2` follows from Beauville's §6.3, whose hypotheses we verify exactly.
    Exactness (`= ℤ/2`) uses Artin–Mumford's computation. The gap of 4 needs exactly `ℤ/2`:
    with `(ℤ/2)²` it would be 0.
  - `b₂(AM₅) = 11` uses Clemens' defect formula for double solids. We computed the defect
    to be 0.
- **Contested status of the problem.** VibeMathed lists the stable-Morse question as
  "Contested", citing an unpublished 2013 preprint by Ma which asserts that the minimal number
  of fixed points always equals the Morse number. OpenAI's September 2026 preprint (real
  dimension 12, not simply connected) already contradicts that assertion. Our example
  contradicts it for a simply connected Kähler manifold of real dimension 10: `Morse(M) = λ(M)`
  by Smale, and `#Fix = λ(M) − 4`.
- **No historical-priority claim.** "New" means "not found in the literature we were able to
  read".

## AI attribution

The results in this repository were found, verified and written up by Claude (Anthropic)
agents working under the direction of the repository owner, [AUTHOR NAME]. This covers the
theorems, their proofs, the computations and the paper text. The mock reviews were also
produced by AI agents. The human owner directed the work and is responsible for its release.

## Citation

See [`CITATION.cff`](CITATION.cff). Please also cite the OpenAI preprints listed in
[`UPSTREAM.md`](UPSTREAM.md).
