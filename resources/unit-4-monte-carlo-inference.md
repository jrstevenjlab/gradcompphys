# Unit 4 Resources: Monte Carlo, Stochastic Methods, and Inference

Related pages: [Resources Home](./README.md) | [Schedule](../schedule.md) | [Assignments](../assignments/README.md)

This unit uses one damped Ramsey experiment to connect Monte Carlo integration, stochastic simulation, uncertainty propagation, Bayesian inference, MCMC diagnostics, posterior predictive checks, and normalizing flows. The resources below are open documentation, open textbooks, or openly available papers used directly in Lectures 15-19.

## Random Sampling and Monte Carlo

- [NumPy random `Generator` documentation](https://numpy.org/doc/stable/reference/random/generator.html)  
  Primary API reference for reproducible pseudorandom streams used in Lectures 15-19.
- [NumPy probability-distribution methods](https://numpy.org/doc/stable/reference/random/generator.html#distributions)  
  Reference for uniform, normal, binomial, and multivariate-normal sampling.
- [SciPy quasi-Monte Carlo documentation](https://docs.scipy.org/doc/scipy/reference/stats.qmc.html)  
  Extends Lecture 15's stratified-sampling idea to Sobol and Halton point sets.
- [Mark Newman, *Computational Physics* resources](https://websites.umich.edu/~mejn/cp2/)  
  Computational-physics programs and supporting material on random processes and Monte Carlo methods.

## Uncertainty Propagation and Simulation

- [SciPy multivariate normal documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_normal.html)  
  Reference for correlated parameter models and covariance matrices.
- [NumPy binomial sampling documentation](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.binomial.html)  
  API used for finite-shot Ramsey experiments and posterior predictive simulation.

## Bayesian Inference

- [Allen Downey, *Think Bayes 2*](https://allendowney.github.io/ThinkBayes2/)  
  Open textbook with computational treatments of Bayes' theorem, grid methods, likelihoods, priors, and posterior prediction.
- [Johnson, Ott, and Dogucu, *Bayes Rules!*](https://www.bayesrulesbook.com/)  
  Open textbook emphasizing Bayesian reasoning, posterior summaries, regression, and model evaluation.
- [Hogg, Bovy, and Lang, *Data analysis recipes: Fitting a model to data*](https://arxiv.org/abs/1008.4686)  
  Connects the likelihood and generative-model framing in Lecture 17 with Unit 2.
- [SciPy binomial distribution documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html)  
  Probability mass function used to construct the Ramsey count likelihood.

## MCMC and Diagnostics

- [Hogg and Foreman-Mackey, *Data Analysis Recipes: Using Markov Chain Monte Carlo*](https://arxiv.org/abs/1710.06068)  
  Practical discussion of MCMC setup, initialization, troubleshooting, and reporting used in Lecture 18.
- [`emcee` documentation](https://emcee.readthedocs.io/en/stable/)  
  Production ensemble-MCMC implementation and workflow examples.
- [`emcee` autocorrelation tutorial](https://emcee.readthedocs.io/en/stable/tutorials/autocorr/)  
  Explanation of integrated autocorrelation time and effective sample size.
- [Stan Reference Manual: MCMC diagnostics](https://mc-stan.org/docs/reference-manual/analysis.html)  
  Reference for split $\widehat R$, effective sample size, and modern convergence diagnostics.
- [ArviZ diagnostics API](https://python.arviz.org/en/stable/api/diagnostics.html)  
  Open Python tools for $\widehat R$, ESS, Monte Carlo standard error, and related summaries.

## Bayesian Workflow and Model Checking

- [Gelman et al., *Bayesian Workflow*](https://arxiv.org/abs/2011.01808)  
  End-to-end framework for model building, computation, validation, sensitivity analysis, and communication.
- [Gabry et al., *Visualization in Bayesian workflow*](https://arxiv.org/abs/1709.01449)  
  Posterior predictive visualization and model-checking ideas used in Lecture 19.
- [ArviZ posterior predictive plotting](https://python.arviz.org/en/stable/api/generated/arviz.plot_ppc.html)  
  Production plotting reference corresponding to Lecture 19's explicit Matplotlib implementation.
- [PyMC documentation](https://www.pymc.io/projects/docs/en/stable/)  
  Probabilistic programming, posterior sampling, predictive simulation, and diagnostics.

## Normalizing Flows and Machine-Learning Extensions

- [Papamakarios et al., *Normalizing Flows for Probabilistic Modeling and Inference*](https://jmlr.org/papers/v22/19-1028.html)  
  Open review of change-of-variables densities, flow architectures, training objectives, and inference applications.
- [Rezende and Mohamed, *Variational Inference with Normalizing Flows*](https://proceedings.mlr.press/v37/rezende15.html)  
  Foundational open paper connecting normalizing flows to optimized posterior approximations.
- [Pyro transform documentation](https://docs.pyro.ai/en/stable/distributions.html#transforms)  
  Examples of invertible transforms and transformed distributions in a probabilistic-programming library.
- [`nflows` open-source library](https://github.com/bayesiains/nflows)  
  Reference implementations of common flow layers; useful beyond the affine demonstration in Lecture 19.

## Shared Physical Example

- [Qiskit Experiments `RamseyXY`](https://qiskit-community.github.io/qiskit-experiments/stubs/qiskit_experiments.library.characterization.RamseyXY.html)  
  Open documentation for a Ramsey experiment and damped-oscillation analysis.
- [Degen, Reinhard, and Cappellaro, *Quantum sensing*](https://arxiv.org/abs/1611.02427)  
  Open review connecting coherence measurements such as Ramsey spectroscopy to quantum sensing.

## Suggested Unit Practice

- Write the generative process before writing simulation or likelihood code.
- Keep Monte Carlo error, experimental variability, and parameter uncertainty separate.
- Normalize and test low-dimensional posteriors on a grid before using MCMC.
- Diagnose chains before quoting posterior summaries.
- Use posterior predictive checks that target plausible physical model failures.
- Compare scientifically defensible priors and report sensitivity.
- Treat optimized approximations such as normalizing flows as models that also require validation.
