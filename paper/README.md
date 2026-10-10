# Paper

`main.tex` is the manuscript (21 pages); `main.pdf` is the compiled version. Build with
`./build.sh` (pdflatex + biber, biblatex). The author block is a placeholder.

Citation-level details were completed in a second round (see
`../verification/mock-reviews/FIXES.md`, "Round 2: citations"). Two `\todo` markers remain:

- a generic status-line marker;
- one point of provenance. Exactness `Tor H³(AM₅) = ℤ/2` is obtained by deforming to the
  Artin–Mumford example, whose torsion is `ℤ/2` (Deligne, Bourbaki exp. 402). Beauville §6.3
  identifies that example with a double solid over a quartic symmetroid satisfying his
  hypotheses (i) and (ii). We have not checked this identification in the original
  Artin–Mumford paper.

Weaker points that carry no marker: the Clemens defect formula is quoted via Cynk
(arXiv:math/0702114), the Harris–Tu degree via Blekherman–Hauenstein–Ottem–Ranestad–Sturmfels
(arXiv:1107.1846), and the Fulton page range is taken from the table of contents.
