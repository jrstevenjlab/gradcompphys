# Course Schedule

**PHYS690: Computational Methods for Physics Research**  
**Fall 2026 | Tuesdays and Thursdays, 2:00-3:20 p.m.**

## Semester At A Glance

| Weeks | Dates | Focus | Planned deliverables |
| --- | --- | --- | --- |
| 1-3 | Aug. 27-Sep. 10 | Unit 1: Research Computing Foundations | Assignment 1 |
| 4-6 | Sep. 15-Oct. 1 | Unit 2: Data Analysis, Model Fitting, and Uncertainty | Assignment 2; Project 1 |
| 7-9 | Oct. 6-22 | Unit 3: Numerical Methods for Physical Systems | Notebook Assignment 3; Unit 3 Project |
| 10-13 | Oct. 27-Nov. 19 | Unit 4: Monte Carlo, Stochastic Methods, and Inference | Notebook Assignment 4; Project 2 |
| 14-15 | Nov. 24-Dec. 3 | Unit 5: Capstone Project Studio | Student-selected final project and presentation |
| Finals period | Dec. 7-16 | Capstone completion | Final repository/report and presentations |

The four unit assignments are primarily Jupyter notebooks with guided exercises and short written interpretations. The four unit projects are more open-ended and will be small enough to complete in one unit while giving students practice with a complete computational workflow.

## Unit 1: Research Computing Foundations

**Unit goal:** Build a reproducible project environment and use the core scientific Python workflow confidently.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Thu, Aug. 27 | [Course orientation and computational research workflows](./lectures/lecture01_8_27_26_workflows.ipynb) |  |
| Tue, Sep. 1 | [Command line, Python environments, notebooks/scripts, and Git basics](./lectures/lecture02_9_1_26_shell_python_git.ipynb) | Assignment 1: shell, Python, project-organization exercises |
| Thu, Sep. 3 | [NumPy arrays, Matplotlib, and pandas](./lectures/lecture03_9_3_26_numpy_scipy_matplotlib_pandas.ipynb) | Assignment 1: NumPy, pandas, and plotting exercises |
| Tue, Sep. 8 | [Least squares fitting in Scipy: measurement uncertainty, residuals, covariance](./lectures/lecture04_9_8_26_scipy_fitting_uncertainty.ipynb) | Assignment 1: SciPy exercises | 
| Thu, Sep. 10 | [Fitting failure modes lab: label switching, local minima, constraints, and underconstrained models](./lectures/lecture05_9_10_26_fit_failure_modes_lab.ipynb) | Assignment 1 due |

**Assignment 1:**  Reproducible Neutrino Workflow [assignment1-template](https://github.com/WM-PHYS690-Fall2026/assignment1-template)

## Unit 2: Data Analysis, Model Fitting, and Uncertainty

**Unit goal:** Connect physical models to data while treating residuals, covariance, and uncertainty as part of the result.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Sep. 15 | [What's under the hood? Gradient descent, minimizers, and analytic derivatives](./lectures/lecture06_9_15_26_minimizers_gradients_derivatives.ipynb) |  |
| Thu, Sep. 17 | [Goodness of fit, model comparison, and hypothesis testing](./lectures/lecture07_9_17_26_goodness_model_comparison_hypothesis_testing.ipynb) | Introduce [Assignment 2](https://github.com/WM-PHYS690-Fall2026/assignment2-template) |
| Tue, Sep. 22 | [Likelihood fits, bootstrap and jackknife resampling; uncertainty propagation](./lectures/lecture08_9_22_26_bootstrap_jackknife_uncertainty.ipynb) | Introduce [Project 1](https://github.com/WM-PHYS690-Fall2026/project1-template) |
| Thu, Sep. 24 | [HPC workflow and resources](./lectures/lecture09_9_24_26_wm_hpc.ipynb) | Assignment 2 due |
| Tue, Sep. 29 | [Initial-value ODEs; Euler, midpoint, and Runge-Kutta methods; local and global error](./lectures/lecture10_9_29_26_ivp_ode.ipynb) |  |
| Thu, Oct. 1 | No lecture (GlueX Collaboration Meeting) | Project 1 repository due |

**Assignment 2:** Fitting Pantheon Supernova [assignment2-template](https://github.com/WM-PHYS690-Fall2026/assignment2-template)

**Project 1:** Fitting Bottomonium from CMS [project1-template](https://github.com/WM-PHYS690-Fall2026/project1-template)

## Unit 3: Numerical Methods for Physical Systems

**Unit goal:** Implement numerical methods for physical systems and assess convergence, stability, boundary conditions, and discretization error.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Oct. 6 | [Finite differences for boundary-value problems and PDEs; grids and boundary conditions](./lectures/lecture11_10_6_26_bvp_pde.ipynb) |  |
| Thu, Oct. 8 | No lecture (Fall Break) |  |
| Tue, Oct. 13 | No lecture (JLab workshop) |  |
| Thu, Oct. 15 | [Applications of initial- and boundary-value problems to fields and particles](./lectures/lecture12_10_15_26.ipynb) | Assignment 3 available |
| Tue, Oct. 20 | [Hermitian quantum eigensystems; harmonic oscillators, convergence, and near-degeneracy](./lectures/lecture13_eigen_10_20_26.ipynb) |  |
| Thu, Oct. 22 | [FFT fundamentals and periodic field solvers; time-angular-frequency analysis and Fourier-space Poisson equations](./lectures/lecture14_fft_10_22_26.ipynb) | Assignment 3 due Oct. 23 |

**Assignment 3:** Particle Charge Deposition and a Poisson Field Solver [assignment3-template](https://github.com/WM-PHYS690-Fall2026/assignment3-template).  Due: Friday, October 23

<!--
**Project 2 plan:** An open-ended numerical-methods project such as a field or wave-equation solver, particle or trajectory integrator, numerical eigensystem problem, or spectral analysis of time-series or field data. Students must show how algorithmic choices affect the result and include a quantitative convergence, stability, or benchmark study.
-->

## Unit 4: Monte Carlo, Stochastic Methods, and Inference

**Unit goal:** Use random sampling and probabilistic models to simulate systems, propagate uncertainty, and draw calibrated inferences.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Oct. 27 | [Monte Carlo sampling and integration; pseudorandom generators, error scaling, and variance reduction](./lectures/lecture15_10_27_26_monte_carlo.ipynb) |  |
| Thu, Oct. 29 | [Stochastic Ramsey experiments and Monte Carlo uncertainty propagation](./lectures/lecture16_10_29_26_stochastic_uncertainty.ipynb) |  |
| Tue, Nov. 3 | No lecture (Election Day) |  |
| Thu, Nov. 5 | [Bayesian inference on a grid: binomial likelihood, priors, probabilities, marginalization, confidence intervals](./lectures/lecture17_11_5_26_bayesian_inference.ipynb) | Assignment 4 available |
| Tue, Nov. 10 | [Metropolis-Hastings MCMC and using `emcee`](./lectures/lecture18_11_10_26_mcmc.ipynb) |  |
| Thu, Nov. 12 | No lecture (Assignment 4 work time) | Assignment 4 due Friday, Nov. 13 |
| Tue, Nov. 17 | [MCMC diagnostics with the production `emcee` sampler](./lectures/lecture19_11_17_26_mcmc_diagnostics.ipynb) |  |
| Thu, Nov. 19 | [Normalizing flows, generative AI, and final-project planning](./lectures/lecture20_11_19_26_normalizing_flows.ipynb) | Final formal lecture; completes Unit 4 |


**Assignment 4:** Simulation of cosmic-ray trigger design [assignment4-template](https://github.com/WM-PHYS690-Fall2026/assignment4-template).  Due: Friday, November 13

**Project 2:** Bayesian constraints on dark energy using Pantheon+ supernova data, comparing constant and time-varying dark-energy models [project2-template](https://github.com/WM-PHYS690-Fall2026/project2-template).  Due: Tuesday, December 3

## Unit 5: Capstone Project Studio

**Unit goal:** Apply the course toolkit to a focused, computational physics question in the research area of your choice.

November 19 is the final formal lecture. Remaining class meetings are project work sessions and consultations.

| Date | Project focus | Milestone |
| --- | --- | --- |
| Tue, Nov. 24 | No lecture (Project planning: define the question, minimum complete result, and computational risks) | Submit one-page project scope and validation plan |
| Thu, Nov. 26 | No lecture (Thanksgiving break) |  |
| Tue, Dec. 1 | No lecture (Final project work time) |  |
| Thu, Dec. 3 | No lecture (Final project work time) |  |

<!--
### Finals Period: December 7-16

- **Mon, Dec. 7:** Final project work period and instructor questions.
- **Wed, Dec. 9, 5:00 p.m.:** Final repository and short report due.
- **Thu, Dec. 10-Tue, Dec. 15:** Capstone presentations; exact presentation slots assigned by the instructor.
- **Wed, Dec. 16:** Final revisions and reflection due, if needed after presentation feedback.

The capstone uses the [project template](./projects/project-template.md) and [project rubric](./projects/rubrics.md). The final submission should include the physics question, computational method, data or model description, validation strategy, uncertainty analysis, figures, reproducibility instructions, results, and reflection.
-->

## Assignment and Project Rhythm

Each three-week unit follows the same rhythm:

1. **Week 1:** Introduce the method and show how the method appears in a research workflow.
2. **Week 2:** Work through the assignment, discuss failure modes, and submit the notebook assignment on Thursday.
3. **Week 3:** Submit the project checkpoint on Tuesday, then use class time for project work, code review, validation, and concise demonstrations before the Thursday project submission.

The notebook assignments are intentionally scaffolded. The projects ask students to make more of the scientific and computational decisions themselves, while still requiring the same standards of validation, uncertainty analysis, documentation, and reproducibility. Unit 5 is a capstone project studio rather than another three-week instructional unit.
