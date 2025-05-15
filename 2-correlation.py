import numpy as np
import pandas as pd
from scipy.stats import pearsonr

project = pd.read_excel('project.xlsx')

x = np.array(project['culture'])
y = np.array(project['depression'])

correlation, p_value = pearsonr(x, y)

print("Correlation:", correlation)
print("P-value:", p_value)

if p_value < 0.05:
    print("The correlation is statistically significant")
else:
    print("The correlation is not statistically significant")