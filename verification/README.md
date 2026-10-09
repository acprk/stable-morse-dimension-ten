# Verification records

## `mock-reviews/`

- `mock-review-1.md` is an adversarial referee report written by an **AI agent** (Claude) that
  did not write the paper. It is **not human peer review**. It found no fatal issue, two major
  issues (both about the scope of claims) and nine minor ones.
- `FIXES.md` lists each review item and how the paper was revised in response.

Earlier drafts and intermediate notes are not included.

## `scripts/`

These are the reviewer's own scripts. They were written independently of `computations/` and do
not reuse it.

- `mr1_web.sage`: exact checks over ℚ of the invariant web.
  - `det` agrees with the displayed `f`, and `f` is irreducible.
  - The singular scheme is reduced of degree 10 and equals the rank ≤ 2 scheme.
  - No member has rank ≤ 1, and the web has no base points.
  - The coordinate points are smooth points of `B`.
  - No quadric passes through the 10 nodes.
  - The invariant quintic is smooth, misses the coordinate points and the nodes, and meets
    `B` in a smooth curve of degree 20 and genus 51.
- `mr1_toric.sage`: a smooth fan resolving `1/5(1,1,4)`, with 7 rays and 9 maximal cones,
  giving `b(F) = 40`.
- `mr1_lambda.py`: an independent computation of `λ(M) = 524`, `Σ λ(C_j') = 520` and the cyclic
  Floer bound `520`.

```sh
cd verification/scripts && sage mr1_web.sage && sage mr1_toric.sage && python3 mr1_lambda.py
```
