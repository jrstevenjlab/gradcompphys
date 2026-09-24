# Unit 3 Resources: Numerical Methods for Physical Systems

Related pages: [Resources Home](./README.md) | [Syllabus](../syllabus.md) | [Assignments](../assignments/README.md)

This unit focuses on numerical solutions of physical models: ODEs, PDEs, finite differences, linear algebra, eigensystems, FFT-based analysis, convergence studies, stability, boundary conditions, and discretization error.

## Essential

- [Mark Newman, *Computational Physics* resources](https://websites.umich.edu/~mejn/cp2/)  
  A very accessible starting point for practical computational physics with code, exercises, and worked examples.
- [SciPy integration tutorial](https://docs.scipy.org/doc/scipy/tutorial/integrate.html)  
  Useful for ODE workflows with `solve_ivp`, solver tolerances, and comparison to known solutions.
- [SciPy linear algebra documentation](https://docs.scipy.org/doc/scipy/reference/linalg.html)  
  Core reference for matrix factorizations, linear systems, and eigensystem-related workflows.
- [SciPy FFT documentation](https://docs.scipy.org/doc/scipy/reference/fft.html)  
  Useful for spectral analysis, frequency-space reasoning, and resolution/aliasing discussions.
- [LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*](https://faculty.washington.edu/rjl/fdmbook/)  
  A strong methods-first reference for consistency, stability, convergence, and boundary-value problems.
- [MIT OpenCourseWare: Numerical Methods for Partial Differential Equations readings](https://ocw.mit.edu/courses/18-336-numerical-methods-for-partial-differential-equations-spring-2009/resources/readings/)  
  Good supplementary reading for wave equations, absorbing layers, level-set methods, and PDE thinking.

## Recommended

- [Giordano and Nakanishi, *Computational Physics*](https://www.physics.purdue.edu/~hisao/book/)  
  Broad coverage of numerical algorithms and physical examples, especially useful for building intuition.
- [Landau, Paez, and Bordeianu, *Computational Physics: Problem Solving with Python*](https://www.compadre.org/PICUP/c/LandauPaez/)  
  A wide-ranging text with extensive computational examples and Python-oriented support material.
- [Heath, *Scientific Computing: An Introductory Survey*](https://heath.cs.illinois.edu/scicomp/pubdata/index.html)  
  Especially useful for linear algebra, eigenvalue problems, ODEs, PDEs, FFTs, and numerical error analysis.

## Optional Deeper Reading

- [MIT OpenCourseWare lecture notes for numerical PDEs](https://mitocw.ups.edu.ec/courses/mathematics/18-336-numerical-methods-for-partial-differential-equations-spring-2009/lecture-notes)  
  Helpful for a more mathematical treatment of finite differences, Fourier methods, and stability ideas.
- [Newman programs and data archive](https://websites.umich.edu/~mejn/cp2/programs.html)  
  Useful when you want compact code examples to compare against your own implementations.
- [LeVeque book page and exercises](https://faculty.washington.edu/rjl/fdmbook/)  
  Good for extra practice with boundary conditions, accuracy checks, and steady-state versus time-dependent problems.

## Suggested Unit Focus

- Check every solver against a limiting case, conserved quantity, or known analytic result.
- Separate physical behavior from numerical artifacts by changing timestep, grid spacing, or basis size.
- Treat convergence and stability studies as part of the scientific result, not as optional appendices.
- Make boundary conditions explicit in both code and documentation.
