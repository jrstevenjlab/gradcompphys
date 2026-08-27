# Course Schedule

**PHYS690: Computational Methods for Physics Research**  
**Fall 2026 | Tuesdays and Thursdays, 2:00-3:20 p.m.**

## Semester At A Glance

| Weeks | Dates | Focus | Planned deliverables |
| --- | --- | --- | --- |
| 1-3 | Aug. 27-Sep. 10 | Unit 1: Research Computing Foundations | Assignment 1 |
| 4-6 | Sep. 15-Oct. 1 | Unit 2: Data Analysis, Model Fitting, and Uncertainty | Notebook Assignment 2; Unit 2 Project |
| 7-9 | Oct. 6-22 | Unit 3: Numerical Methods for Physical Systems | Notebook Assignment 3; Unit 3 Project |
| 10-12 | Oct. 27-Nov. 12 | Unit 4: Monte Carlo, Stochastic Methods, and Inference | Notebook Assignment 4; Unit 4 Project |
| 13-15 | Nov. 17-Dec. 3 | Unit 5: Capstone Project | Capstone proposal, progress review, and presentation rehearsal |
| Finals period | Dec. 7-16 | Capstone completion | Final repository/report and presentation |

The four unit assignments are primarily Jupyter notebooks with guided exercises and short written interpretations. The four unit projects are more open-ended and will be small enough to complete in one unit while giving students practice with a complete computational workflow.

## Unit 1: Research Computing Foundations

**Unit goal:** Build a reproducible project environment and use the core scientific Python workflow confidently.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Thu, Aug. 27 | Course orientation; computational research workflows; Unix/Linux and the shell | Introduce Assignment 1 |
| Tue, Sep. 1 | Command line: Files, paths, etc. and Git basics: commits, branches, etc. | Assignment 1: shell and project-organization exercises |
| Thu, Sep. 3 | Python environments; Jupyter notebooks versus scripts; NumPy arrays, SciPy routines, and basic computation | Assignment 1: Python, NumPy, and SciPy exercises |
| Tue, Sep. 8 | Matplotlib and pandas; readable notebooks; metadata, documentation, and reproducible outputs | Assignment 1: GitHub |
| Thu, Sep. 10 | Introduction to Unit 2 | Assignment 1 due |

**Assignment 1 plan:** A guided notebook that asks students to inspect a small dataset or starter calculation, organize a repository, use shell and Git operations, load and transform data with Python, create a figure, and document how to rerun the work.

**Project 1 plan:** A compact reproducible research workflow. Students may select a small analysis, a workflow reconstruction, or a research-code refactoring problem from the menu. The submission should include a working repository, a notebook or script, a short README, and a brief validation or sanity check.

<!-- 

## Unit 2: Data Analysis, Model Fitting, and Uncertainty

**Unit goal:** Connect physical models to data while treating residuals, covariance, and uncertainty as part of the result.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Sep. 15 | Data ingestion, cleaning, exploratory visualization, and honest plotting | Introduce Assignment 2 and a fitting project menu |
| Thu, Sep. 17 | Measurement uncertainty, residuals, covariance, and weighted least squares | Assignment 2: residual and covariance exercises |
| Tue, Sep. 22 | Nonlinear model fitting with SciPy; parameter identifiability and initial guesses | Assignment 2 workshop; Project 2 selection |
| Thu, Sep. 24 | Likelihoods, goodness of fit, model comparison, and communicating fitted parameters | Assignment 2 due; project planning |
| Tue, Sep. 29 | Bootstrap and jackknife resampling; uncertainty propagation; diagnosing fit failure | Project 2 proposal/checkpoint due; Project 2 studio |
| Thu, Oct. 1 | Fit review; interpreting results and limitations; short project presentations | Project 2 repository/report due |

**Assignment 2 plan:** A guided notebook that moves from data inspection to visualization, model fitting, residual analysis, covariance interpretation, and one resampling-based uncertainty estimate. Students should compare at least two reasonable modeling choices and explain what the comparison does and does not establish.

**Project 2 plan:** An open-ended data-analysis project such as model fitting and parameter extraction, histogram analysis and background estimation, image or spectral analysis, or an instrument-response workflow. The required emphasis is on a defensible analysis chain and uncertainty statement, not on using the most complicated model.

## Unit 3: Numerical Methods for Physical Systems

**Unit goal:** Implement numerical methods for physical systems and assess convergence, stability, boundary conditions, and discretization error.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Oct. 6 | Initial-value ODEs; Euler, midpoint, and Runge-Kutta methods; local and global error | Introduce Assignment 3 and numerical project options |
| Thu, Oct. 8 | Stability, step-size control, conserved quantities, and particle/trajectory integration | Assignment 3: ODE and stability exercises |
| Tue, Oct. 13 | Finite differences for boundary-value problems and PDEs; grids and boundary conditions | Assignment 3 workshop |
| Thu, Oct. 15 | Linear algebra and numerical eigensystems; conditioning and physical interpretation | Assignment 3 due; project planning |
| Tue, Oct. 20 | FFTs and spectral analysis; resolution, aliasing, and discretization choices | Project 3 proposal/checkpoint due; Project 3 studio |
| Thu, Oct. 22 | Verification versus validation; convergence studies; stability and error reporting | Project 3 repository/report due; short demonstrations |

**Assignment 3 plan:** A guided notebook comparing numerical methods on an ODE or finite-difference problem. Exercises will require students to vary resolution or step size, examine stability and convergence, compare with an analytic or benchmark solution, and interpret an eigensystem or FFT result.

**Project 3 plan:** An open-ended numerical-methods project such as a field or wave-equation solver, particle or trajectory integrator, numerical eigensystem problem, or spectral analysis of time-series or field data. Students must show how algorithmic choices affect the result and include a quantitative convergence, stability, or benchmark study.

## Unit 4: Monte Carlo, Stochastic Methods, and Inference

**Unit goal:** Use random sampling and probabilistic models to simulate systems, propagate uncertainty, and draw calibrated inferences.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Oct. 27 | Pseudorandom numbers, sampling, Monte Carlo integration, and error scaling | Introduce Assignment 4 and inference project options |
| Thu, Oct. 29 | Stochastic simulation and Monte Carlo uncertainty propagation | Assignment 4: sampling and propagation exercises |
| Tue, Nov. 3 | Likelihoods and priors; posterior distributions; credible intervals and posterior visualization | Assignment 4 workshop |
| Thu, Nov. 5 | MCMC algorithms, autocorrelation, effective sample size, and convergence diagnostics | Assignment 4 due; project planning |
| Tue, Nov. 10 | Bayesian model checking, sensitivity to priors, and communicating posterior results | Project 4 proposal/checkpoint due; Project 4 studio |
| Thu, Nov. 12 | Comparing stochastic methods; failure modes; short project presentations | Project 4 repository/report due |

**Assignment 4 plan:** A guided notebook that estimates an integral or physical quantity by sampling, propagates uncertain inputs through a nonlinear model, and uses a small MCMC analysis to visualize and diagnose a posterior. Students should report sampling error and discuss at least one diagnostic limitation.

**Project 4 plan:** An open-ended Monte Carlo or inference project such as Monte Carlo uncertainty propagation or Bayesian inference for a physics model. The project should state the sampling or inference target, justify the likelihood and any priors, show posterior or output diagnostics, and distinguish numerical sampling uncertainty from physical or measurement uncertainty.

## Unit 5: Capstone Project

**Unit goal:** Integrate the course methods into a focused, research-style computational project.

| Date | Lecture and working focus | Milestone |
| --- | --- | --- |
| Tue, Nov. 17 | Capstone kickoff; choosing a tractable question from the project menu; scope and risk assessment | Project idea and initial scope due |
| Thu, Nov. 19 | Proposal design: physics question, method, data/model, validation, and uncertainty plan | Capstone proposal due; proposal feedback |
| Tue, Nov. 24 | Computational design review; validation tests; uncertainty and reproducibility planning | Progress checkpoint and work session |
| Thu, Nov. 26 | Thanksgiving break | No regular class; independent project work |
| Tue, Dec. 1 | Scientific figures, documentation, interpretation, and repository cleanup | Draft results and figures for peer review |
| Thu, Dec. 3 | Presentation structure, rehearsal, peer feedback, and final submission checklist | Presentation rehearsal; final work plan |

### Finals Period: December 7-16

- **Mon, Dec. 7:** Final project work period and instructor questions.
- **Wed, Dec. 9, 5:00 p.m.:** Final repository and short report due.
- **Thu, Dec. 10-Tue, Dec. 15:** Capstone presentations; exact presentation slots assigned by the instructor.
- **Wed, Dec. 16:** Final revisions and reflection due, if needed after presentation feedback.

The capstone uses the [project template](./projects/project-template.md) and [project rubric](./projects/rubrics.md). The final submission should include the physics question, computational method, data or model description, validation strategy, uncertainty analysis, figures, reproducibility instructions, results, and reflection.

-->

## Assignment and Project Rhythm

Each three-week unit follows the same rhythm:

1. **Week 1:** Introduce the method, release the notebook assignment on Tuesday, and show how the method appears in a research workflow.
2. **Week 2:** Work through the assignment, discuss failure modes, and submit the notebook assignment on Thursday.
3. **Week 3:** Submit the project checkpoint on Tuesday, then use class time for project studios, code review, validation, and concise demonstrations before the Thursday project submission.

The notebook assignments are intentionally scaffolded. The projects ask students to make more of the scientific and computational decisions themselves, while still requiring the same standards of validation, uncertainty analysis, documentation, and reproducibility.
