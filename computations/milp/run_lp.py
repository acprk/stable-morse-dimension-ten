import sys
from lpsearch2 import search
for K in (2,3):
    for n in (4,5,6):
        print("forbid_C_H1tors=True", end=" "); search(n,K,forbid_C_sc=True)
for n in (4,5):
    print("K=3 unrestricted", end=" "); search(n,3)
