# Mock referee report 1 (hostile) on paperSM/main.tex (internal draft, 2026-10-09)

Referee stance: symplectic topology and algebraic geometry. I tried to break Theorems A, B and C. main.tex was not edited.
Fresh scripts in this directory: `mr1_web.sage` (+ `mr1_web.out`), `mr1_toric.sage`, `mr1_lambda.py`. None of them reuse q10.sage, lam.py, w10.py or indep.py.

## Summary verdict

**No FATAL issue found.** Theorem A (the dim-10 Kähler counterexample) survives every attack I tried. That covers the transverse center lemma, the Hamiltonian property, the homology bookkeeping, the 5-torsion vanishing, exactness of Tor H_2(F)=Z/2, S ⊂ F, and nondegeneracy/contractibility. Theorem C and Lemma H1 (`lem:perfect`) are correct as stated. Theorem B is correct but trivial.

The manuscript does overclaim in the abstract, in §6.4 ("Open problem: dimension eight") and in Table 1. The "minimal dimension is 8 or 10" statement needs two things the paper does not have: a simple-connectivity hypothesis, and a treatment of real dimensions 2 and 4. One directly relevant OpenAI preprint is not cited. Several remarks are inaccurate (the support remark is wrong for 2 of the 4 components). Recommendation: **minor-to-major revision**. The mathematics of A and C stands; the framing must be corrected.

## Issues

### MAJOR

**M1. "Minimal dimension of a counterexample is 8 or 10" is not proved.**
Locations: abstract (ll. 71–73), §6.4 "Open problem: dimension eight" (l. 1140), Table 1.
- Conjecture (eq:SMconj) is stated for all closed symplectic M. Theorem B covers only **simply connected** real-dim-6 M.
- Real dimensions **2 and 4 are never treated**.
- (a) Non-simply-connected case. In dims 4 and 6, SM(M) can exceed λ(M) (Damian). The Bai–Xu bound gives only λ_N(M). So nothing excludes a non-simply-connected counterexample in dim 4 or 6. The Sept 23 OpenAI preprint (see M2) shows that π_1 effects already break the Morse-number version.
- (b) Simply connected dim 4. M is torsion-free, so Bai–Xu gives #Fix_0 ≥ b(M) = λ(M). Excluding a counterexample also needs SM(M) = λ(M) for simply connected closed 4-manifolds. Smale's theorem does not apply in dim 4, and the paper gives no argument or reference.
- Fix:
  - restrict all such statements to "simply connected";
  - add a short paragraph for dim 2 (surfaces: SM = Morse = λ = 2g+2) and for simply connected dim 4;
  - for dim 4, either prove SM = λ (e.g. by relative handle cancellation in W×D^k, k ≥ 2, which is simply connected of dim ≥ 6) or cite it, or else downgrade the claim to "among simply connected manifolds of real dimension ≥ 6".
- Separately, "modulo ... Smale's theorem" is odd wording. Smale 1962 Thm 6.1 is a theorem; only the citation is unchecked. Also, the main agent has now confirmed the Bai–Xu form (arXiv:2209.08599 Thm A, any closed M, bound rank H_*(M;Q) + 2 Σ_{i∈Z/2N} τ_i^{(2N)}). So the "modulo Bai–Xu" hedge can become a plain citation.

**M2. Missing directly relevant prior work.**
- `openai-math/preprints/A-nondegenerate-counterexample-to-the-Morse-number-Arnold-bound-September-23-2026`: a nondegenerate counterexample to the **Morse-number** form, on a closed symplectic 12-manifold, with unbounded deficit.
- It is not cited. Yet §6.2 ("Relation to an earlier claim", the Ma remark) says Theorem A "contradicts that claim, as do the earlier examples", listing only the SM-papers. The Sept 23 paper is the first disproof of exactly the Ma-type statement and is lower-dimensional than OpenAI22.
- Fix: cite it in the introduction and in §6.2. State that Theorem A is the first example below the **stable** Morse number in dim < 22 and the first Morse-number counterexample in dim 10. Check whether the Sept 23 example is simply connected; if it is not, say so.

### MINOR

**m1. Remark `rem:support` is false as written** (ll. 1063–1067).
- The diagonal circle has weights (1,1) at (0,0) and (−1,−1) at (∞,∞). So it acts **trivially** on E_00 and E_∞∞, and the circle action on C_1' and C_4' is trivial (each is itself a T-fixed component).
- On C_2' and C_3' (over E_0∞ and E_∞0) the T-fixed components are **F, F, S**, not "a copy of F and a copy of S":
  - the proper transform of F×{pole};
  - F×{other fixed point};
  - the section P(T_yE) ≅ S of the exceptional divisor;
  - the section P(N_S F) lies in the proper transform of F×{pole}.
- Consistency check I did: the T-fixed components of M contribute total Betti number 2·122 + 2·(40+40+42) = 488 = b(M), as rational perfectness requires.
- Within C_2', Σ_F λ(F) = 44+44+46 = 134 versus λ(C_2') = 130. The loss of 4 comes from the overlap of S (5-torsion, degrees 3,4) with the F's (2-torsion, degrees 2–5).
- Also Σ_{F⊂M^T} λ(F) = 528 ≥ λ(M) = 524, consistent with Step 1 of Theorem C.
- Fix: replace the todo with this explicit description.

**m2. Prop. `prop:AM5`: the deformation argument can be replaced, and is loosely written.**
- The main agent has verified Beauville §6.3 hypotheses (i) and (ii) for the explicit web over Q̄ (beauville_ii.sage). Theorem 6.3 can then be applied **directly** to AM_5, without the open-set/Ehresmann argument.
- If the deformation argument is kept, it needs:
  - a statement that the relative singular scheme is proper over the parameter space, so that finite-fibre length is upper semicontinuous on the open quasi-finite locus;
  - local triviality of the family of A_1 points, so that the blown-up family is smooth;
  - a reference for degree 10 and Cohen–Macaulayness of the corank-2 symmetric locus (Harris–Tu, "On symmetric and skew-symmetric determinantal varieties", 1984).
- b_2 = 11 and b_3 = 0 now follow independently from defect 0. Cite Clemens' defect formula for double solids and the check dim I_nodes(2) = 0 (confirmed again in mr1_web.out). Remove the todo at l. 495.

**m3. Prop. `prop:Fhom`, prime 5: two places need one more sentence.**
- (i) "the only possible differential into E_{0,2} comes from the finite group E^3_{3,0}". Add: "it is zero because E^2_{0,2} ≅ Z_(5)^3 is torsion-free."
- (ii) From Mayer–Vietoris alone, H_2(F)_(5) is an extension of ker(H_1(∂U) → H_1(U)) ≅ (Z/5)^3 by a free module. Torsion-freeness comes only from duality with H_3(F)_(5) = 0. Say this explicitly, because a reader will otherwise suspect a Z/5 in H_2.
- Everything else here I checked step by step (see V6) and it is correct, including the Lefschetz duality step H_3(U,∂U) ≅ H^3(U) for the oriented compact 6-manifold U.

**m4. Exactness of Tor H_2(F) = Z/2 (coordinator point 6). The argument is complete but scattered; collect it into one lemma.**
- The gap really is this fragile. mr1_lambda.py gives:
  - Tor H_2(F) = (Z/2)^2 ⇒ gap 0 (λ = 552 = 4·138);
  - an extra Z/5 in F ⇒ gap 0.
- The chain that makes it exact:
  1. Tor H_2(AM) ≅ Tor H^3(AM) = Z/2 **exactly**, from Beauville/Artin–Mumford.
  2. Mayer–Vietoris localized at 2: H_i(∂U)_(2) = 0 for i = 1, 2, 3, and H_*(R) is free. Hence Tor H_2(F)_(2) = Tor H_2(U)_(2).
  3. Cartan–Leray with |G| invertible: H_2(U;Z_(2)) ≅ H_2(X°;Z_(2))^G.
  4. Torsion of the invariants: H^1(G; Tor) = 0, so Tor(H^G) = (Tor H)^G = Z/2, since G acts trivially on Z/2.
  5. ℓ ∉ {2,5}: no ℓ-torsion.
  6. ℓ = 5: as in m3.
- Freeness and evenness of H_*(R_k) (needed in step 2 and for H_3(R) = 0) still lacks a reference: Fulton, Introduction to Toric Varieties §5.2, applies to simplicial fans with convex support.

**m5. Lemma `lem:transverse` (d).** "Choose local holomorphic coordinates in which W and C_j are both linear" needs a justification (the clean-intersection normal form) or a different argument. Simpler alternative:
- Fix(ĝ) is a closed complex submanifold.
- (b) and (c) show it equals (C_j \ W) ∪ E|_{W∩C_j} as a set.
- The proper transform of C_j is a closed connected submanifold with the same underlying set (closure of C_j \ W plus its exceptional divisor P(N_{W∩C_j/C_j}) = E|_{W∩C_j}).

**m6. Theorem C, minor wording.**
- "If g = id" should be "if g acts trivially on M" (T need not act effectively).
- The abstract's "every construction of the type 'finite-order element ... plus a small invariant perturbation'" should say "of the type of Proposition `prop:perturb`".
- The proof never uses dim M = 8 except through dim C_j ≤ 6. State the general form: Σλ(C_j) ≥ λ(M) whenever every component of Fix(g) has real dimension ≤ 6.
- Lemma `lem:perfect`: I checked the argument and believe it is correct (details in V8). It deserves a precise citation for the F_p torus Smith inequality (Allday–Puppe, Cohomological Methods in Transformation Groups, Ch. 3; Bredon Ch. III for Z/p) instead of the current todos. A referee will ask whether it was previously known that moment maps are perfect over every F_p; do a literature search before claiming novelty.

**m7. Theorem B is a five-line corollary of Bai–Xu plus Poincaré duality.**
Under the project's own gate (CLAUDE.md, "专家一下午") it should be a Proposition or Remark, not a headline theorem. Recommendation: demote it, and merge it with the dims 2/4 discussion of M1.

**m8. Section 6.3 ("Dimensional limitation of transverse centers").**
- The argument "dim M ≥ 4+2+4 = 10" is a heuristic. It assumes the inserted torsion comes from a surface contained in the center.
- Likewise, the remark after Prop. `prop:nec8` ("one needs an ambient with Brauer-type torsion from the start") only applies to blow-up constructions.
- Label both as heuristics; do not say "This matches Theorem C".

**m9. Housekeeping.**
- Remark after the proof of Theorem A cites "8 in the R8 internal notes"; remove internal references.
- Remark `rem:absolute`: the todo on b(F) = 40 can be closed. My Sage check gives a smooth fan with 7 rays and 9 maximal cones, so each R_k has Betti numbers (1,4,4) and b_2(F) = 3+16 = 19.
- §5 refers to the free ranks "b(F)=8, b(S)=11 hard-coded" in m10_indep.py. That is fine, but state that the gap is independent of them.
- Lemma `lem:webfacts`: "f is irreducible" is checked over Q only. Absolute irreducibility follows because Sing(B) is finite: a reducible surface is singular along a curve. Add this sentence.

## Claims independently verified (and how)

**V1. The web** (fresh Sage, `mr1_web.sage` → `mr1_web.out`, exact arithmetic over Q):
- det A equals the displayed f;
- all monomials of f have weight 3 mod 5;
- f is irreducible over Q, hence absolutely irreducible by m9;
- A_0, ..., A_3 are linearly independent;
- the saturated Jacobian scheme is 0-dimensional of degree 10, radical, and equal to the saturated 3×3-minor (rank ≤ 2) scheme;
- **the 2×2-minor ideal saturates to the unit ideal, so no rank ≤ 1 member**;
- the web has no base points;
- the gradients at p_0..p_3 are as stated (p_k ∈ B and smooth);
- **dim H^0(I_nodes(2)) = 0**, so the nodes impose independent conditions on quadrics, the defect is 0, and b_3(AM_5) = 0, b_2 = 11. This is independent of the χ argument.

**V2. The quintic Q:**
- it is invariant and uses all 12 invariant monomials;
- it is smooth;
- Q(p_k) = 6, 9, 13, 5 ≠ 0;
- it misses the nodes;
- B ∩ {Q=0} is a smooth curve with Hilbert polynomial 20t − 50, i.e. degree 20 and genus 51, matching 2g−2 = 100.

**V3. Fixed points.**
- By hand: local weights at p_0..p_3 are (4,4,1), (1,1,4), (3,2,3), (2,3,2), all of type 1/5(1,1,4).
- Fresh Sage (`mr1_toric.sage`): star subdivision at (1,1,4)/5, ..., (4,4,1)/5 gives a smooth fan with 7 rays and 9 maximal cones.
- Hence χ(R_k) = 9, χ(F) = 8 + 32 = 40, b_2(F) = 19, b(F) = 40.

**V4. S.** By hand: χ(quintic) = 55, 2g(Δ)−2 = 4H·5H = 100, χ(S̃) = 210, χ(S) = 42, b_2(S) = 40. π_1(Σ\Δ) = Z/4 because H is primitive (H² = 5 is squarefree), so 4H has divisibility exactly 4. The Nori argument then gives π_1(S̃) = 1.

**V5. λ bookkeeping** (fresh `mr1_lambda.py`, degreewise groups with Künneth including Tor terms):
- λ(M) = 524, Σλ(C_j') = 520, λ_1(M) = 520 (so the Bai–Xu bound is attained);
- the gap is 4 for (a, β) ∈ {(3,5), (19,40), (50,7)};
- the gap is 0 if Tor H_2(F) = (Z/2)^2 or if F has extra 5-torsion.
- By hand: Table `tab:torsion` (ll. 808–823) is correct (Σt(M) = 18, Σt(C') = 4). The dim-12 Remark `rem:dim12` is also correct (gap 8, λ = 1400, #Fix = 1392).

**V6. 5-torsion vanishing**, re-derived step by step:
- the pairing matrix diag(2, −1, ..., −1) gives index | 2;
- H_2(X;Z_(5)) ≅ Z_(5) ⊕ Z_(5)[G]^2;
- Cartan–Leray gives E^∞_{0,2} = Z_(5)^3 and H_2(U)_(5) free;
- H^3(U)_(5) = 0, hence H_3(U,∂U)_(5) = 0 by Lefschetz duality (6−3 = 3, U oriented);
- H_3(∂U) → H_3(U) is onto at 5, so H_3(F)_(5) = 0 (H_2(∂U) = 0, H_3(R) = 0);
- duality gives Tor H_2(F)_(5) = 0;
- |H_3(U)_(5)| = 25 is consistent (E^∞_{1,2} = Z/5, E^∞_{3,0} = Z/5).
- The 2-part argument is in m4.

**V7. Transverse lemma and fixed locus of ĝ:**
- each E_j contains exactly one pole;
- T_pA/T_pW ≅ N_{S/F} ⊕ T_yE carries dĝ = id, so the exceptional P^1-fibres over S×{pole} are pointwise fixed;
- the C_j' are simply connected and of real dimension 8;
- the circle action lifts; an averaged Kähler form together with H^1 = 0 makes it Hamiltonian;
- minimal Chern number 1 via {x}×E_00 with x ∉ S;
- Prop. `prop:perturb` (finite-order version) checked: Φ^k = ψ^{kε}, and the normal block tends to d_xg|_{E≠} − I, which is invertible.

**V8. Theorem C:**
- Step 1: max of sums ≤ sum of maxes, using Corollary `cor:torsionformula`.
- Step 2: in a 6-dimensional C, 4-dimensional fixed components are extremal and unique by Atiyah–Guillemin–Sternberg connectedness, so the torsion supports {1,2} and {3,4} are disjoint.
- Lemma `lem:perfect`:
  - "≤" holds by Morse–Bott with complex (hence F_q-oriented) negative bundles;
  - "≥" holds by the iterated Smith inequality along Z/q^n (the fixed set of Z/q^{n+1}/Z/q^n on X_n is X_{n+1}) together with finiteness of isotropy types;
  - equality of total dimensions forces degeneration of the Morse–Bott spectral sequence.
  - I found no counterexample: rational perfectness plus this argument is consistent with every example I checked (CP^1 with weight q, the C_j' above).
- Non-simply-connected C_j are covered, since nothing in Step 2 uses π_1.

**V9. Prop. `prop:nec8` and Prop. `prop:productfail`:** both formulas re-derived by hand.
