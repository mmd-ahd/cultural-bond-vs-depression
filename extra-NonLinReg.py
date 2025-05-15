import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

project = pd.read_excel('project.xlsx')

def nonlinear_function(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

x = project['culture'] 
y = project['depression']

popt, pcov = curve_fit(nonlinear_function, x, y, maxfev=9999)

y_pred = nonlinear_function(x, *popt)
print(y_pred)

ss_res = np.sum((y - y_pred) ** 2)
ss_tot = np.sum((y - np.mean(y)) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print('R^2:', r_squared)

plt.scatter(x, y, label='Original data', color="#071b4b")
plt.scatter(x, y_pred, label='Prediction data', color="#38e8a4")
plt.plot(x, y_pred, label='Nonlinear Regression', color="#38e8a4")
plt.xlabel('Culture')
plt.ylabel('Depression')
plt.legend()
plt.show()