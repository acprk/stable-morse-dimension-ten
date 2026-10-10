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

## Round 2: citations (2026-10-09)
Sources were fetched: arXiv 0808.0613v7, 1507.02476, 2209.11165, math/0702114, 1604.08273, 1012.3530, Voisin's Inventiones PDF, and Deligne's Bourbaki exposé 402 from numdam.
- **Clemens defect formula.** Original page not consulted. The paper cites Cynk, arXiv:math/0702114, §1 and Cor. 5.1, which states verbatim h^{1,1}(Ỹ) = 1+μ+δ and h^{1,2}(Ỹ) = C(3d/2−1,3) − 4C(d/2,3) − μ + δ, with δ the dependent conditions on forms of degree 3d/2−4. For d=4, μ=10, δ=0 this gives b_2 = 11 and b_3 = 0. The text says the Clemens page was not consulted. Todo closed.
- **Harris–Tu.** Theorem number not located. The degree formula ∏ binom(n+j,n−r−j)/binom(2j+1,j) and "irreducible, arithmetically Cohen–Macaulay" are cited as quoted in Blekherman–Hauenstein–Ottem–Ranestad–Sturmfels (arXiv:1107.1846, §1). Since the variety is CM, a proper linear section has length equal to the degree, which is 10. Todo closed.
- **Fulton.** Now cited only for the complete case (§5.2, pp. 101–103; page range from the Google Books table of contents). The paper gives a self-contained argument for R_k:
  - R_k retracts onto the chain D_1 ∪ … ∪ D_4 of smooth complete toric surfaces;
  - the fan adjacencies come from bF2.sage (maximal cones listed in the text);
  - invariant curves are primitive;
  - Mayer–Vietoris then shows the homology is free and even.
  Todo closed.
- **Nori.** Cited as Prop. 3.27 (D = Δ smooth, r = 0, E = ∅; kernel finitely generated abelian), via the statement quoted in Libgober arXiv:2108.02812, Cor. 2.5. Todo closed.
- **Smith inequality.** Cited as tom Dieck, Transformation Groups, Prop. III.4.16, via Franz arXiv:1604.08273, Prop. 2.1 (smooth (Z_p)^r-manifolds, dim H*(X^G) ≤ dim H*(X)). Bredon Ch. III kept as a general reference.
  - Literature search: no explicit statement found that moment maps are F_p-perfect.
  - The text says so, and explains why Kirwan's Euler-class argument fails when p divides an isotropy weight.
  - No novelty is claimed. Todo closed.
- **Ma 2013 Thm 1.5.** Quoted verbatim from arXiv:0808.0613v7: "Let (M,ω) be a close symplectic manifold with symplectic form ω. Then Arn(M,ω) = Crit(M) and Arn_s(M,ω) = Crit_m(M)".
  - The definitions of Arn, Arn_s, Crit and Crit_m are given in the text.
  - There are no hypotheses, and all fixed points are counted.
  - The first equality is refuted by [OpenAIDeg]; the second by [OpenAISept23] and by Theorem A. Todo closed.
- **Bibliography.**
  - Armstrong: issue no. 2 and DOI 10.1017/S0305004100042845 added.
  - Rezchikov: title "Integral Arnol'd Conjecture" confirmed. Remark rem:rezchikov now quotes §2.1 Remark 2 ("integrally graded Floer groups, which we will avoid in this paper").
  - Nori: DOI added.
  - New entries: Cynk, Endraß 1999, Voisin 2015, Deligne 1973, BHORS, tom Dieck, Franz.
- **Substantive point (exactness of Tor H^3 = Z/2 for every web with (i),(ii)): no source found.**
  - Beauville §6.3 (Thm 6 and its proof) gives, under (i),(ii): Δ has exactly 10 ODPs, V is unirational (so π_1 = 1 without deformation), and Tor H^3 ≠ 0.
  - Voisin (proof of Cor. 2.6) gives that the torsion is killed by 2.
  - Endraß, Lemma 1.2, embeds the torsion into a group of even node sets; not computed for our web.
  - Exactness is therefore still obtained by deformation, inside the open set U_0, which contains every (i),(ii)-web, to the Artin–Mumford example. That example has Tor H^3 ≅ Z/2 by Deligne, Bourbaki 402, Constr. 2.2, and Tor H^3 is a birational invariant (Deligne Prop. 2.1).
  - Remaining todo: confirm that the AM/Deligne example is birational to an (i),(ii)-symmetroid double solid. Beauville §6.3 and Cossec assert this.

## Round 3: arbitrary Hamiltonian maps of prime order (dimension 8)

- New §6.4 / Proposition `prop:primeorder`, with its proof. It applies to every simply connected
  closed symplectic 8-manifold and every `g ∈ Ham` of prime order, whether or not `g` lies in a
  torus action. If perturbing `g` beats `λ(M)`, then some fixed component carries `ℤ/PQ`-torsion
  in a single degree, where `P` and `Q` are the dominant primes of `Tor H₂(M)` and `Tor H₃(M)`.
  The proof uses three inputs: the vanishing theorem of Bai–Shelukhin–Wilkins–Xu
  (arXiv:2607.25960, Prop. C.17(1)), which gives equality of rational Betti numbers; the
  Morse–Bott spectral-sequence inequality for every `𝔽_p`; and a short counting argument.
- New remark: Atallah–Shelukhin (monotone case); Chiang–Kessler / Li–Li–Wu (the only known
  non-extendable Hamiltonian involution, in dimension 4; higher dimensions open,
  Li–Li–Wu Q. 1.10).
- Open problem §7.3 updated accordingly.
- Long `\texttt` script paths replaced by `\nolinkurl`; `\emergencystretch` added.
