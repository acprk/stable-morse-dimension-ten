# Upstream provenance

This repository contains no code or text copied from other repositories. Its mathematics builds
on two preprints in [OpenAI's mathematics repository](https://github.com/openai/math), at commit
[`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`](https://github.com/openai/math/tree/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints):

- *Hamiltonian Fixed Points Below the Stable Morse Number in Dimension Twenty-Two* (OpenAI,
  October 5, 2026), directory
  `preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-in-Dimension-Twenty-Two-October-5-2026`.
  We use its dynamical construction: perturbing a Hamiltonian involution so that its fixed set
  becomes the critical points of Morse functions on the fixed components (its Prop. 4.2,
  called `dyn:involution` in its source; we restate and generalize it to finite order). We
  also use the Kähler surface `Y` of its Prop. 4.3.
- *Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number* (OpenAI,
  October 5, 2026), directory
  `preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026`.

Both preprints construct counterexamples in real dimensions 22 and 3332. The paper here
gives a counterexample in real dimension 10 and an obstruction in dimension 6.
