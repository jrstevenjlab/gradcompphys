# Data Files

## `cms_dimuon_jpsi_3000.csv`

A lightweight teaching subset derived from the CMS Run2010B dimuon open-data CSV used in the ROOT CSV data-source tutorial.

Source dataset citation:

- Thomas McCauley, *Dimuon event information derived from the Run2010B public Mu dataset*, CERN Open Data Portal (2014), DOI: 10.7483/OPENDATA.CMS.CB8H.MFFA.

Original CSV URL used to prepare the subset:

- https://root.cern/files/tutorials/df014_CsvDataSource_MuRun2010B.csv

Reduction applied for this course repository:

- selected opposite-sign dimuon events,
- selected 2.6 < dimuon invariant mass < 3.6 GeV,
- selected dimuon pair transverse momentum below 30 GeV,
- sampled 3000 events with random seed 20260922,
- retained a small set of columns needed for Lecture 8.

This reduced file is for teaching likelihood modeling and resampling workflows. It is not suitable for a publication-quality CMS physics analysis.
