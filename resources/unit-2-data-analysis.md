# Unit 2 Resources: Data Analysis, Model Fitting, and Uncertainty

Related pages: [Resources Home](./README.md) | [Syllabus](../syllabus.md) | [Assignments](../assignments/README.md)

This unit focuses on extracting physics from data with appropriate statistical care. The main themes are visualization, residuals, fitting, covariance, uncertainty propagation, resampling, likelihood-based reasoning, and model comparison.

## Essential

- [Hogg, Bovy, and Lang, *Data Analysis Recipes: Fitting a Model to Data*](https://arxiv.org/abs/1008.4686)  
  A concise and highly useful guide to fitting, uncertainty assumptions, outliers, covariance, and model criticism.
- [SciPy `optimize` documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)  
  The main reference for minimization, least-squares solvers, curve fitting, and constrained optimization.
- [SciPy `stats` documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)  
  Useful for probability distributions, summary statistics, hypothesis tests, and resampling-adjacent workflows.
- [SciPy `curve_fit` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)  
  Especially useful for nonlinear least-squares fitting and interpreting parameter covariance matrices.

## Recommended

- [Bevington and Robinson, *Data Reduction and Error Analysis for the Physical Sciences*](https://books.google.com/books/about/Data_reduction_and_error_analysis_for_th.html?id=oAovAQAAIAAJ)  
  A classic reference for fitting, weighting, chi-square methods, and data-analysis practice in physics.
- [Glen Cowan, *Statistical Data Analysis*](https://academic.oup.com/book/54868)  
  A strong reference for likelihoods, estimation, confidence intervals, and hypothesis testing in the physical sciences.
- [SciPy `least_squares` documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)  
  Helpful for robust residual-based fitting and understanding solver behavior more directly.

## Optional Deeper Reading

- [Taylor, *An Introduction to Error Analysis*](https://mitpress.mit.edu/9780935702750/introduction-to-error-analysis/)  
  Revisit the sections on correlated uncertainties and propagation when covariance becomes important.
- [Cowan, *Statistical Data Analysis*](https://academic.oup.com/book/54868)  
  Particularly useful for likelihood-based inference and model comparison beyond least squares.

## Suggested Unit Focus

- Always inspect data before fitting.
- Treat residuals as a diagnostic tool, not just a final plot.
- Report what assumptions underlie an uncertainty estimate.
- Distinguish parameter uncertainty from model inadequacy.
- Use bootstrap or jackknife methods when analytic estimates are fragile or unclear.
