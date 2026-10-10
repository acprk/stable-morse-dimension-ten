"""Remark rem:surfacelimit: with surface-type centers in a torsion-free ambient,
the product construction X x Y gives no deficit for dim_C X = 4, 5."""
from lam import *
import itertools
mx = 0
for ka, kb, kc, kd in itertools.product(range(0, 4), repeat=4):   # n = 5
    TX = add(*([blowup_add(surf(2, 2), 3)] * ka + [blowup_add(times_free(surf(2, 2), CP1), 2)] * kb
               + [blowup_add(surf(3), 3)] * kc + [blowup_add(times_free(surf(3), CP1), 2)] * kd))
    if TX: mx = max(mx, abs(gap(TX)))
print('n=5: max |lambda(XxY) - 4 lambda(XxP1)| =', mx)
mx = 0
for ka, kc in itertools.product(range(0, 5), repeat=2):            # n = 4
    TX = add(*([blowup_add(surf(2, 2), 2)] * ka + [blowup_add(surf(3), 2)] * kc))
    if TX: mx = max(mx, abs(gap(TX)))
print('n=4: max |lambda(XxY) - 4 lambda(XxP1)| =', mx)
