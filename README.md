# PClub_SecyTasks2021

Task for PClub Secy Selection 2021.

## Regression Models with Julia

Implemented [Linear](./Models/linear_regression.ipynb) and [Polynomial](./Models/polynomial_regression.ipynb) Regression Models with non-usual Error functions in `JuliaLang`.  
All analysis are stored in files [linear_regression](./Models/linear_regression.csv) and [polynomial_regression](./Models/polynomial_regression.csv) for the respective models.  
I did include `step_size` for storage later on, so it's not mentioned in every output.  
I used `Stochastic regression approach` for both of the problem statements.  
Libraries used were `Plots` and `Noise` for Plotting graphs and introducing noise in the original functions.

### Best estimates (Not a good measure to compare error functions though)

- Linear Regression
  Original Function: `3x+4` (No Noise included)

  - Cubic Error Function:  
    final params: (3.1855654780384737, 4.049053086683707), loss: 1.1737328953775124e-8, initial params: (0, 4), error function: 3 _\*_
  - Linear Error Function:  
    final params: (3.0349490000000494, 0.060098000000039446), loss: 0.45500299999503113, initial params: (0, 0), error function: 1, step size: 1.0e-6

- Polynomial Regression
  Original Function: `2x²+3.6x+4.5` + Gaussian Noise (stddev = 1000)

  - Fourth Power Error Function:  
    final params: (1.847817797005682, 0.028828337506882587, 0.00048012740462221513), loss: 0.11337892676676484, initial params: (0, 0, 0), error function: 4, step size: 1.0e-17
  - Seventh Power Error Function:  
    final params: (1.6641170444045876, 0.020556864365351625, 0.0002609854087531852), loss: 0.00021225693481259639, initial params: (0, 0, 0), error function: 7, step size: 1.0e-30

\* - Step Size not stored.

## Scraping Mookit with Bs4

This scraper is based on the fact that you can copy HTML Code from your HelloIITK Course.  
To do so, Go to the Course Page of the course and open `Inspect Element` (Ctrl+Shift+I).  
Right-Click on the `<body>` tag and select `Edit as HTML`.  
Copy all the contents (Ctrl+A) and paste them in [input.html](./Scraping/input.html).  
Run `python scraper_bs4.py` and Enter relevant details asked, which are:

- Number of Latest Lectures to analyse
- Link to your course's page (Copy-Paste the link only, as this scripts modifies the original path)

Your course details which include:

- Index of Lecture (1-indexing followed)
- Duration of Lecture
- Week of Lecture
- Lecture Name
- Link to the Lecture Page (on Mookit)
