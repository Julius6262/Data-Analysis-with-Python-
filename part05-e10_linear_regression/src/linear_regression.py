#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    """Template for creating a linear regression model. fit_intercept=True includes intercept"""
    model = LinearRegression(fit_intercept=True)
    """Fit the model to the data.
    The method fit() expects x to be a 2D array, so we reshape it using x[:, np.newaxis],
    which transforms the 1D array x into a 2D column vector.
    This ensures that each value in the original x array is treated as a separate data point.
    In other words, it takes the values of the row in x and turns them into a new column.
    The target variable y is expected to be a 1D array, which it already is."""
    model_2 = model.fit(x[:, np.newaxis], y)
    
    """acessing the fit attribues. coef_ is an array, so to acess the value we need the index[0]"""
    return model_2.coef_[0], model_2.intercept_
    
def main():
    n=20   # Number of data points
    # Creates n = 20 equaly spaced points between 0 and 10
    x=np.linspace(0, 10, n)
    y=x*2 + 1 + 1*np.random.randn(n) # Standard deviation 1
    # Fit the line
    coef, intercept = fit_line(x, y)
    
    # Print the results
    print("Slope:", coef)
    print("Intercept:", intercept)
    
    xfit=np.linspace(0,10,100)
    # same as  y = ax +b 
    yfit = coef*xfit + intercept
    # plt.plot asumes it is a straighline to plot, when given two coordinates we make it black
    plt.plot(xfit,yfit, color="black")
    # 'o' for circle as plotpoints
    plt.plot(x,y, 'o')
    
    
    # Display the plot
    plt.show()
if __name__ == "__main__":
    main()
