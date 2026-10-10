#!/bin/sh
# Reproduce all computations. Requires python3 (homology), python3 with scipy>=1.9 (MILP), SageMath (sage/).
set -e
cd "$(dirname "$0")"
echo "== homology: dimension 10 (Theorem A), independent implementation";  (cd homology && python3 m10_indep.py)
echo "== homology: dimension 10, profile calculator";                       (cd homology && python3 w10.py | grep "(0, 2) S torsion rank 1")
echo "== homology: dimension 16 (Remark), both implementations";           (cd homology && python3 x12.py | head -3 && python3 indep.py | head -2 && python3 surface_limit.py)
echo "== sage: Z/5-invariant web, nodes, invariant quintic";               (cd sage && sage q10.sage)
echo "== sage: Beauville's hypotheses (i),(ii)";                           (cd sage && sage beauville_ii.sage)
echo "== sage: defect of the double solid";                                (cd sage && sage defect2.sage)
echo "== sage: toric resolution of 1/5(1,1,4)";                            (cd sage && sage bF2.sage)
echo "== milp: dimensions 8,10,12 and necessity in dimension 10 (slow)";   (cd milp && python3 run_lp.py && python3 necessity.py)
