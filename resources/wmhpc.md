# William & Mary HPC Cluster

Related pages: [Resources Home](./README.md) | [Unit 1 Resources](./unit-1-research-computing.md) | [Syllabus](../syllabus.md)

William & Mary provides high-performance computing (HPC) resources for projects that are too computationally intensive or data-intensive for a typical laptop. In this course, the cluster may become useful in Unit 2 and beyond when we move into larger calculations, repeated model fits, parameter sweeps, Monte Carlo studies, or other jobs that are better handled through batch processing.

## What It Is

The W&M research computing environment gives students, faculty, and staff access to shared compute resources managed by the university. The main-campus cluster is commonly referred to as `sciclone`, and W&M documentation describes it as part of the university's centrally administered research computing infrastructure.

## When You Might Use It In This Course

- A calculation takes too long on your laptop.
- You need to run the same analysis many times with different inputs or parameters.
- You want to submit a job and let it run in the background rather than keeping your own machine busy.
- You need a more reproducible workflow for larger-scale numerical work.

## Core Ideas

- You usually connect to the cluster from your own computer using `ssh`.
- You work from the command line rather than from a normal desktop-style interface.
- Long or computationally heavy work is typically submitted as a batch job rather than run directly in an interactive login session.
- W&M uses `Slurm` as the batch scheduler, so commands such as `sbatch`, `squeue`, and `scancel` are part of the normal workflow.

## Typical Workflow

1. Request HPC access if you do not already have it.
2. Log in from macOS Terminal or Windows Git Bash using `ssh`.
3. Move code or data to the cluster if needed.
4. Prepare a batch script that tells Slurm what resources your job needs.
5. Submit the job with `sbatch`.
6. Check progress with `squeue`.
7. Review output files and bring results back to your local machine when needed.

## Access And Prerequisites

- HPC access at W&M is by request rather than enabled automatically.
- According to the W&M Research Computing documentation, faculty, staff, and students with legitimate classroom or research needs can request access at no cost.
- You should be comfortable with the Unix/Linux command line before relying on the cluster for course work.
- On Mac, the built-in Terminal application works well for connecting.
- On Windows, Git Bash in the VS Code terminal is the course default for connecting with `ssh`; PowerShell also works if you already prefer it.

## Good Habits For Students

- Test your code locally on a small case before submitting a larger batch job.
- Keep scripts and inputs organized so you can reproduce a run later.
- Do not treat login nodes like personal desktops for long-running calculations.
- Save job scripts alongside your project so you can track exactly how a result was produced.

## Official References

- [Research Computing at W&M](https://www.wm.edu/offices/it/services/researchcomputing/atwm/)
- [Request an HPC account](https://www.wm.edu/offices/it/services/researchcomputing/acctreq/)
- [Using the W&M/VIMS HPC batch clusters](https://www.wm.edu/offices/it/services/researchcomputing/using/)
- [Logging in to HPC clusters](https://www.wm.edu/offices/it/services/researchcomputing/using/connecting/)
- [Running jobs with Slurm](https://www.wm.edu/offices/it/services/researchcomputing/using/running_jobs_slurm/)
- [W&M HPC tutorials](https://www.wm.edu/offices/it/services/researchcomputing/using/tutorials/)
