# Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols

This repository contains a paper on the closed-form hypergeometric representations of SU(2) 3nj symbols, with a focus on 12j symbols.

## Contents

- LaTeX source of the paper
- GitHub Pages website using Jekyll and MathJax
- PDF version of the paper
- Computational verification scripts

## Website

The paper is available as a GitHub Pages website at:
https://arcticoder.github.io/su2-3nj-uniform-closed-form/

## Computational Verification

The repository includes scripts that verify the theoretical results through symbolic and numerical computations:

### Taylor Expansion

The `symbolic_taylor_expansion.py` script constructs an explicit symbolic Taylor expansion of the universal generating functional around the origin. It includes terms for angular momentum values 0, 1/2, and 1, generating a series with 26 coefficients of the form `C_j12_j23_j34`.

### Hypergeometric Representation

The `match_simplest_hypergeometric.py` script demonstrates the correspondence between the simplest term in our expansion (j12=0, j23=0, j34=1/2) and the known hypergeometric representation of the 9j symbol in the form of a 4F3 hypergeometric function.

### Numerical Verification

Two scripts provide numerical validation of our approach:

- `verify_simple_9j_numeric.py`: Numerically verifies the simplest case (j12=0, j23=0, j34=1/2)
- `verify_additional_9j_numeric.py`: Verifies an additional case (j12=0, j23=1/2, j34=0) for robustness

All verification results are stored in the `data` directory as CSV files, confirming that our approach correctly reproduces known values for specific configurations of 9j symbols.