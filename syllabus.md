# PHYS690: Computational Methods for Physics Research

**Instructor:** Justin Stevens  
***Office:*** Small Hall 343C  
***Email:*** jrstevens01@wm.edu  

**Fall 2026:** August 27-December 4, with capstone work and presentations during finals week, December 7-16.  
**Meeting time:** Tuesdays and Thursdays, 2:00-3:20 p.m.  
**Office Hours:** TBD and by appointment (in-person or Zoom).  I am often at Jefferson Lab for research, so not always available in-person at W&M.

Related pages: [Course Home](./README.md) | [Schedule](./schedule.md) | [Resources](./resources/README.md) | [Assignments](./assignments/README.md)

## Course Description

This graduate course develops practical computational skills for physics research. Students will design, implement, validate, and communicate computational workflows that connect physical models, data, and numerical methods. The course emphasizes reproducibility, numerical reliability, uncertainty quantification, and clear scientific communication.

The organization of the course is method-focused rather than subfield-focused. Students will work through projects in data analysis, model fitting, numerical simulation and stochastic methods. By the end of the semester, students should be able to take a physics problem from raw data or mathematical model to tested code, quantitative results, uncertainty estimates, and publication-quality figures.

## Learning Goals

By the end of the course, students should be able to:

1. Use Unix/Linux tools, version control, and reproducible project organization in a research workflow.
2. Analyze scientific data, visualize trends, and diagnose data-quality issues.
3. Fit models to data and evaluate parameter uncertainties using covariance methods, resampling, likelihoods, and goodness-of-fit diagnostics.
4. Implement and validate numerical methods for differential equations, linear algebra, eigensystems, and spectral problems.
5. Apply Monte Carlo and stochastic methods to simulation, uncertainty propagation, and inference.
6. Use the [W&M HPC cluster](./resources/wmhpc.md) for larger-scale calculations, including batch processing and parallel job submission.
7. Communicate computational results through readable code, documentation, figures, short reports, and oral presentations.

## Course Units

### Unit 1: Research Computing Foundations

Practical foundation for research computing: Unix/Linux command-line work, Python environments, Jupyter versus scripts, Git workflows, project organization, documentation, and reproducibility.

### Unit 2: Data Analysis, Model Fitting, and Uncertainty

Work with scientific datasets using visualization, residual analysis, nonlinear fitting, covariance matrices, bootstrap and jackknife methods, likelihood functions, and model comparison.

### Unit 3: Numerical Methods for Physical Systems

Implement and test numerical methods for ordinary and partial differential equations, boundary-value problems, finite-difference methods, eigensystems, FFT-based analysis, and convergence and stability studies.

### Unit 4: Monte Carlo, Stochastic Methods, and Inference

Random sampling, Monte Carlo integration, stochastic simulation, uncertainty propagation, Markov-chain Monte Carlo, and Bayesian summaries to study physical systems and quantify uncertainty.

### Unit 5: Capstone Project

Each student or small team completes a computational research project in their field of interest. The capstone requires a clear physics question, a documented computational method, validation tests, uncertainty analysis, reproducibility instructions, and a final presentation.

## Assessment

| Component | Weight |
| --- | ---: |
| Unit assignments | 30% |
| Unit projects | 30% |
| Final capstone project | 30% |
| Participation and code review | 10% |

Project grades emphasize both scientific correctness and computational practice. Strong work should demonstrate clear code, reproducibility, validation, uncertainty analysis, thoughtful interpretation, and effective figures.

The four unit assignments are primarily Jupyter notebooks with guided exercises. There will also be open-ended projects to complete for Units 2-5. The [course schedule](./schedule.md) lists release dates, workshops, checkpoints, and due dates. 

## Course Schedule

The semester is organized into five three-week units.  Unit 5 is reserved for the capstone, which continues through finals week.  See the [lecture-by-lecture schedule](./schedule.md) for the complete calendar. There is no regular class meeting on the following dates:
- GlueX Collaboration Meeting, Thu, Oct. 1
- Fall Break, Thu, Oct. 8
- Election Day, Thu, Nov. 3
- Thanksgiving, Thu, Nov. 26

The final capstone projects will be presented on Thu, Dec. 10 from 2-5 pm during the final exam time slot.

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

## Generative AI Use

Generative AI tools are welcome in this course when they support learning, debugging, and understanding. Appropriate uses include asking for explanations of unfamiliar code, interpreting error messages, brainstorming debugging strategies, clarifying Python or Unix syntax, and discussing alternative ways to organize or test your work.

Generative AI should not be used to complete assignments or projects on your behalf. Do not paste a full assignment or project prompt into an AI system and ask it to produce a standalone solution, notebook, report, or repository. The scientific choices, code structure, interpretation, validation, and written explanations you submit must be your own work and must be work you can explain.

If you use AI in a substantial way while completing an assignment or project, include a brief note describing how it helped. For example, it is fine to say that AI helped you understand an error message, debug a plotting problem, or compare possible implementations. It is not acceptable to submit AI-generated work that you do not understand or that bypasses the intended learning goals of the task.

## Course Philosophy

Computation is now part of everyday research practice in physics. This course is not only about writing code or applying isolated algorithms. It is about developing judgment: choosing an appropriate method, testing an implementation, estimating uncertainty, recognizing failure modes, and communicating results clearly enough that another researcher can understand and reuse the work.

Students should leave the course with a portfolio of small but complete computational projects and one substantial capstone project that demonstrates an end-to-end research workflow.

## Accommodations

It is the policy of William & Mary to accommodate students with disabilities and qualifying diagnosed conditions in accordance with federal and state laws. Any student who feels they may need an accommodation based on the impact of a learning, psychiatric, physical, or chronic health diagnosis should contact the Student Accessibility Services staff at 757-221-2509 or at sas@wm.edu. SAS staff will work with you to determine if accommodations are warranted, and if so, to help you obtain an official letter of accommodation. For more information, please see [Student Accessibility Services](https://www.wm.edu/offices/studentsuccess/studentaccessibilityservices/).

## Mental and Physical Well-Being: 

William & Mary recognizes that students juggle different responsibilities and can face challenges that make learning difficult.  There are many resources available at W&M to help students navigate emotional/psychological, physical/medical, material/accessibility concerns, including:  
* The [W&M Counseling Center](https://www.wm.edu/offices/wellness/counselingcenter/students/) at (757) 221-3620.  
* The [W&M Health Center](https://www.wm.edu/offices/wellness/healthcenter/) at (757) 221-4386. 
* A list of other wellness resources available to students can be found at: https://www.wm.edu/offices/wellness/resources/
