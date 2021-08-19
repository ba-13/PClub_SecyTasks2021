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
  Original Function: 3x+4

  - Cubic Error Function:  
    final params: (3.1855654780384737, 4.049053086683707), loss: 1.1737328953775124e-8, initial params: (0, 4), error function: 3 _\*_
  - Linear Error Function:  
    final params: (3.0349490000000494, 0.060098000000039446), loss: 0.45500299999503113, initial params: (0, 0), error function: 1, step size: 1.0e-6

- Polynomial Regression
  Original Function: 2x²+3.6x+4.5

  - Fourth Power Error Function:  
    final params: (2.0360512590738673, 0.030346234384101382, 0.0004756004902345417), loss: 0.8224581171799286, initial params: (0, 0, 0), error function: 4, step size: 1.0e-17
  - Seventh Power Error Function:  
    final params: (2.3511610277618087, 0.829923854026342, 0.3077725997535397), loss: 0.06645167983891893, initial params: (0, 0, 0), error function: 7, step size: 1.0e-10

\* - Step Size not stored.
