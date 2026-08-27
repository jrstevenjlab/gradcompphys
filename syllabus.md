# PHYS690: Computational Methods for Physics Research

**Graduate Project-Based Course**  
**Physics Department, William & Mary**

**Meeting time:** Tuesdays and Thursdays, 2:00-3:20 p.m.  
**Fall 2026:** August 27-December 4, with capstone work and presentations during finals week, December 7-16.

Related pages: [Course Home](./README.md) | [Schedule](./schedule.md) | [Resources](./resources/README.md) | [Assignments](./assignments/README.md)

## Course Description

This graduate course develops practical computational skills for physics research. Students will design, implement, validate, and communicate computational workflows that connect physical models, data, and numerical methods. The course emphasizes reproducibility, numerical reliability, uncertainty quantification, and clear scientific communication.

The organization of the course is method-focused rather than subfield-focused. Students will work through projects in data analysis, model fitting, numerical simulation, stochastic methods, and professional research-computing practice. By the end of the semester, students should be able to take a physics problem from raw data or mathematical model to tested code, quantitative results, uncertainty estimates, and publication-quality figures.

## Learning Goals

By the end of the course, students should be able to:

1. Use Unix/Linux tools, version control, and reproducible project organization in a research workflow.
2. Analyze scientific data, visualize trends, and diagnose data-quality issues.
3. Fit models to data and evaluate parameter uncertainties using covariance methods, resampling, likelihoods, and goodness-of-fit diagnostics.
4. Implement and validate numerical methods for differential equations, linear algebra, eigensystems, and spectral problems.
5. Apply Monte Carlo and stochastic methods to simulation, uncertainty propagation, and inference.
6. Communicate computational results through readable code, documentation, figures, short reports, and oral presentations.

## Course Units

### Unit 1: Research Computing Foundations

Students build the practical foundation for research computing: Unix/Linux command-line work, Python environments, Jupyter versus scripts, Git workflows, project organization, documentation, and reproducibility.

### Unit 2: Data Analysis, Model Fitting, and Uncertainty

Students work with scientific datasets using visualization, residual analysis, nonlinear fitting, covariance matrices, bootstrap and jackknife methods, likelihood functions, and model comparison.

### Unit 3: Numerical Methods for Physical Systems

Students implement and test numerical methods for ordinary and partial differential equations, boundary-value problems, finite-difference methods, eigensystems, FFT-based analysis, and convergence and stability studies.

### Unit 4: Monte Carlo, Stochastic Methods, and Inference

Students use random sampling, Monte Carlo integration, stochastic simulation, uncertainty propagation, Markov-chain Monte Carlo, and Bayesian summaries to study physical systems and quantify uncertainty.

### Unit 5: Capstone Project

Each student or small team completes a research-style computational project. The capstone requires a clear physics question, a documented computational method, validation tests, uncertainty analysis, reproducibility instructions, and a final presentation.

## Assessment

| Component | Weight |
| --- | ---: |
| Short computational assignments | 25% |
| Unit projects | 35% |
| Participation and code review | 10% |
| Final capstone project | 25% |

Project grades emphasize both scientific correctness and computational practice. Strong work should demonstrate clear code, reproducibility, validation, uncertainty analysis, thoughtful interpretation, and effective figures.

The four unit assignments are primarily Jupyter notebooks with guided exercises. Each unit also includes one open-ended project selected from the [project menu](./projects/project-menu.md). The [course schedule](./schedule.md) lists release dates, workshops, checkpoints, and due dates. The capstone project uses the [project template](./projects/project-template.md) and [project rubric](./projects/rubrics.md).

## Course Schedule

The semester is organized into five three-week units. Units 1-4 each pair a scaffolded notebook assignment with an open-ended computational project. Unit 5 is reserved for the capstone, which continues through finals week.

| Unit | Dates | Main focus |
| --- | --- | --- |
| 1. Research Computing Foundations | Aug. 27-Sep. 10 | Reproducible workflows, Unix/Linux, Git, Python, and project organization |
| 2. Data Analysis, Model Fitting, and Uncertainty | Sep. 15-Oct. 1 | Data workflows, fitting, residuals, covariance, resampling, and model comparison |
| 3. Numerical Methods for Physical Systems | Oct. 6-22 | ODEs, PDEs, eigensystems, FFTs, convergence, stability, and discretization error |
| 4. Monte Carlo, Stochastic Methods, and Inference | Oct. 27-Nov. 12 | Sampling, stochastic simulation, uncertainty propagation, MCMC, and Bayesian inference |
| 5. Capstone Project | Nov. 17-Dec. 16 | Proposal, implementation, validation, communication, and final presentation |

See the [lecture-by-lecture schedule](./schedule.md) for the complete calendar. There is no regular class meeting on Thanksgiving, Thursday, November 26.

## Software and Tools

The course will primarily use open-source tools:

- Python
- NumPy, SciPy, Matplotlib
- `pandas` or equivalent data-analysis tools
- Jupyter notebooks and plain Python scripts
- Git and GitHub
- Unix/Linux command-line tools
- Additional specialized libraries as needed for particular projects

Students may use other languages or tools with instructor approval, provided the workflow remains reproducible, well documented, and appropriate for the project goals.

## Course Philosophy

Computation is now part of everyday research practice in physics. This course is not only about writing code or applying isolated algorithms. It is about developing judgment: choosing an appropriate method, testing an implementation, estimating uncertainty, recognizing failure modes, and communicating results clearly enough that another researcher can understand and reuse the work.

Students should leave the course with a portfolio of small but complete computational projects and one substantial capstone project that demonstrates an end-to-end research workflow.
