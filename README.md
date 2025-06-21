# Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://arcticoder.github.io/su2-3nj-uniform-closed-form/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)

This repository contains a comprehensive mathematical framework for the closed-form hypergeometric representations of SU(2) 3nj symbols, with particular focus on 12j symbols and their universal generating functional.

## 🔬 Mathematical Framework

Our work presents a **universal closed-form hypergeometric representation** that unifies all SU(2) 3nj recoupling coefficients under a single special-function framework. This breakthrough provides:

- **Exact symbolic expressions** for arbitrary 3nj symbols
- **Computational efficiency** through hypergeometric function evaluation
- **Mathematical rigor** with complete derivations and proofs
- **Numerical validation** across multiple test cases

## 📖 Contents

- **LaTeX Source**: Complete mathematical derivation and proofs
- **GitHub Pages Website**: Interactive presentation with MathJax rendering
- **PDF Documentation**: Publication-ready mathematical exposition
- **Computational Scripts**: Python implementation and verification tools
- **Validation Data**: Numerical verification results and benchmarks

## 🌐 Online Documentation

**📚 Read the paper online**: [https://arcticoder.github.io/su2-3nj-uniform-closed-form/](https://arcticoder.github.io/su2-3nj-uniform-closed-form/)

The website features:
- Complete mathematical exposition with interactive equations
- Downloadable PDF version
- Source code examples and usage instructions
- Cross-references to related work in the SU(2) 3nj series

## 🔬 Computational Verification

The theoretical framework is validated through comprehensive computational verification:

### 🔄 Taylor Expansion Analysis
**Script**: `symbolic_taylor_expansion.py`
- Constructs explicit symbolic Taylor expansion of the universal generating functional
- Generates series with 26 coefficients of the form `C_j12_j23_j34`
- Covers angular momentum values: 0, 1/2, and 1
- Provides symbolic verification of convergence properties

### ⚡ Hypergeometric Correspondence
**Script**: `match_simplest_hypergeometric.py`
- Demonstrates correspondence with known 9j symbol representations
- Validates 4F3 hypergeometric function equivalence
- Focuses on simplest case: (j12=0, j23=0, j34=1/2)
- Confirms theoretical predictions through symbolic computation

### 📊 Numerical Validation
**Primary**: `verify_simple_9j_numeric.py`
- Numerical verification of simplest case (j12=0, j23=0, j34=1/2)
- High-precision arithmetic validation
- Error analysis and convergence testing

**Extended**: `verify_additional_9j_numeric.py`
- Additional test case: (j12=0, j23=1/2, j34=0)
- Robustness verification across parameter space
- Cross-validation with established numerical libraries

**Output**: All results stored in `data/` directory as CSV files with complete numerical verification confirming theoretical accuracy.

## 🛠️ Installation & Usage

### Prerequisites
```bash
pip install sympy numpy scipy pandas matplotlib
```

### Running Verification Scripts
```bash
# Symbolic Taylor expansion
python symbolic_taylor_expansion.py

# Hypergeometric matching
python match_simplest_hypergeometric.py

# Numerical validation
python verify_simple_9j_numeric.py
python verify_additional_9j_numeric.py
```

## 🔗 Related Work

This repository is part of a comprehensive SU(2) 3nj symbol research series:

- **[su2-3nj-closedform](../su2-3nj-closedform)**: Closed-form hypergeometric product formula
- **[su2-3nj-recurrences](../su2-3nj-recurrences)**: Finite closed-form recurrence relations
- **[su2-3nj-generating-functional](../su2-3nj-generating-functional)**: Universal generating functional approach
- **[su2-node-matrix-elements](../su2-node-matrix-elements)**: Operator matrix elements for arbitrary-valence nodes

## 📝 Mathematical Background

### Core Theory
The universal representation unifies all 3nj symbols through:
```
3nj Symbol = Hypergeometric_Series(angular_momenta, coupling_structure)
```

### Key Innovations
- **Universal generating functional**: Single expression for all 3nj topologies
- **Closed-form hypergeometric**: Exact special function representation
- **Computational efficiency**: Direct evaluation without recursion
- **Mathematical elegance**: Unified framework for all recoupling coefficients

## 🎯 Applications

- **Quantum Mechanics**: Angular momentum coupling calculations
- **Computational Physics**: Efficient 3nj symbol evaluation
- **Mathematical Physics**: Special function theory and applications
- **Numerical Libraries**: High-performance recoupling coefficient computation

## 📄 Citation

```bibtex
@article{su2_3nj_uniform_closed_form,
  title={Universal Closed-Form Hypergeometric Representation of SU(2) 3nj Symbols},
  author={Arctic Coder},
  journal={GitHub Repository},
  year={2025},
  url={https://github.com/arcticoder/su2-3nj-uniform-closed-form}
}
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

⭐ **Star this repository** if you find it useful for your research or applications!