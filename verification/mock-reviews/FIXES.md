# FIXES for mock-review-1 (2026-10-09)

Snapshot before revision: `verification/main.pre-review1.tex`. Compiled result: `main.pdf`, 18 pages, no undefined references, no overfull boxes.

## MAJOR
- **M1 (minimal dimension).** Every minimal-dimension claim is now restricted to simply connected manifolds.
  - Corollary 1.1: among simply connected closed symplectic manifolds of real dimension ≥ 6, the minimal dimension is 8 or 10.
  - Abstract, Table 1 and §7.3 rewritten to match.
  - New §3 "Low dimensions":
    - dim 2: SM = Morse = λ = 2g+2; Bai–Xu with N = 2 (S^2) or N = ∞ (g ≥ 1) gives the bound.
    - simply connected dim 4: Bai–Xu gives #Fix ≥ b = λ, so a counterexample would need SM > λ. Explicitly left open; Smale does not apply.
  - The "modulo Bai–Xu / Smale" hedges are gone.
    - Theorem 2.4 states Bai–Xu Thm A verbatim (rank H_*(M;Q) + 2 Σ_{i∈Z/2N} τ_i^{(2N)}, any closed M; their N = 0 is our N = ∞).
    - Smale is cited as Amer. J. Math. 84 (1962) Thm 6.1, with a footnote that the wording was confirmed only via secondary sources.
- **M2 (missing prior work).** Cited [OpenAISept23] (real dim 12, π_1 = A_5^k, not simply connected, Morse-number version, Thm 1.1: #Fix = χ(M)+128 < Morse(M)):
  - in §1.1, in Previous work, and as a row of Table 1;
  - in the rewritten Ma remark (§7.2). Ma's assertion is already refuted there; Theorem A is the first simply connected example below SM in dim < 22 and refutes Ma in dim 10 Kähler.
  - Ma2013 is now a proper bib entry (arXiv:0808.0613v7, Thm 1.5).
  - Also cited [OpenAIDeg] for the degenerate six-dimensional quadric example. This replaces the internal "manuscript 347" pointer.

## MINOR
- **m1.** Remark rem:support rewritten as the reviewer describes:
  - the circle acts trivially on C_1', C_4';
  - on C_2', C_3' the T-fixed components are F, F, S;
  - Betti total 488 = b(M);
  - within C_2': 134 vs 130;
  - overall: Σ_F λ(F) = 528 ≥ 524 ≥ 520.
- **m2.**
  - Beauville §6.3 is applied directly. Hypotheses (i) base point free and (ii) are verified exactly over Q̄ (computations/sage/beauville_ii.sage; rank ≤ 1 members: none). This gives a nonzero 2-torsion class.
  - Exactness (Tor = Z/2) still comes from deformation to the general Artin–Mumford member. The text says explicitly that we do not know whether AM's computation covers every web satisfying (i),(ii).
  - The deformation argument is tightened: properness of the relative singular scheme, the quasi-finite locus, the étale locus, the holomorphic Morse lemma with parameters for local triviality, and Harris–Tu for degree 10 (todo on scheme-theoretic length).
  - b_2 = 11, b_3 = 0 now follow from defect 0 (Hilbert function 1,4,10,10,…; computations/sage/defect2.sage; Clemens 1983, todo for the page). The χ = 24 check is kept.
- **m3.** Both sentences added:
  - the d^3 differential vanishes because E^2_{0,2} ≅ Z_(5)^3 is torsion-free;
  - Mayer–Vietoris alone leaves an extension of (Z/5)^3 by a free module, and only duality excludes Z/5 in H_2.
- **m4.**
  - New Lemma lem:torF collects Steps 1–6 (input, localization, transfer, H^1(G; Tor) = 0, prime 5, duality at 5). Remark rem:5torsion now also records the (Z/2)^2 ⇒ gap 0 fragility.
  - The toric blocks cite Fulton, Introduction to Toric Varieties §5.2 (todo for the page).
- **m5.** Transverse lemma (d) no longer uses simultaneous linearization. It uses the strict transform = Bl_{W∩C}C (Hartshorne II.7.15; the scheme-theoretic intersection is smooth by cleanness), plus the isomorphism P(N_{W∩C/C}) ≅ E|_{W∩C} and the closed-submanifold argument.
- **m6.**
  - "g = id" replaced by "g acts trivially".
  - Theorem B (the old Theorem C) is stated in the general form: Σλ(C_j) ≥ λ(M) whenever all components of Fix(g) have real dimension ≤ 6. The proof notes that it uses neither dim M nor π_1(C).
  - The abstract says "of the type of Proposition prop:perturb".
  - Lemma lem:perfect cites Bredon Ch. III (Smith theory for Z/q) and Allday–Puppe Ch. 3 / Hsiang Ch. III. No novelty is claimed; a todo remains for theorem numbers and a literature search.
- **m7.** Old Theorem B (dim 6) is demoted to Proposition 3.1 and merged with the dim 2/4 discussion. The main theorems are now A and B.
- **m8.**
  - §6.4 is retitled "(heuristic)" and the "matches Theorem C" sentence is removed.
  - The remark after Prop. nec8 now says it is heuristic and applies only to blow-up constructions.
- **m9.**
  - All references to internal R8 notes are removed.
  - The b(F) = 40 todo is closed (computations/sage/bF2.sage plus the reviewer's independent fan: 7 rays, 9 cones).
  - The placeholder-rank sentence now states independence of the gap.
  - The absolute-irreducibility sentence is added to Lemma lem:webfacts.

## Coordinator items B/C
- Closed: Smale, b_2/b_3, b(F), λ = 524 / #Fix = 520, Li 2003 Thm 0.1 (Proc. AMS 131 no. 11), OpenAI22 numbering (Prop. 4.2, Prop. 4.3, Thm 2.4).
- Remark rem:rezchikov added: Rezchikov Thm 1 is a minimal-rank statement whose proof uses the 2N-periodized Morse complex (§2.1). It is consistent with Bai–Xu; read Z-graded, it would be contradicted by Theorem A.
- 16-dim cyclic bound recomputed: λ_1 = 1216 = #Fix. The todo is removed.
- All script paths are repository-relative (computations/homology, sage, milp).
- Author block: "[AUTHOR NAME]".
- AI-use statement added before the bibliography.
