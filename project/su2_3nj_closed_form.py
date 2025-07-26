# project/su2_3nj_closed_form.py

"""
Stub hypergeometric closed‐form for the Wigner 6-j symbol.

Currently delegates to SymPy’s wigner_6j for exact agreement.
Swap in your true 4F3 implementation later.
"""

try:
    import sympy as sp
except ImportError:
    print("ERROR: sympy is required for su2_3nj_closed_form. Please install it with 'pip install sympy'.")
    import sys
    sys.exit(2)

from sympy.physics.wigner import wigner_6j

def closed_form_3nj(j1, j2, j3, j4, j5, j6):
    # Convert to exact rationals
    js = list(map(sp.Rational, (j1, j2, j3, j4, j5, j6)))
    # Delegate to SymPy’s exact Racah sum
    return wigner_6j(*js)
