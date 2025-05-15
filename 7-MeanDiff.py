import pandas as pd
import numpy as np

project = pd.read_excel("project.xlsx")

median = project['culture'].median()

project['group'] = np.where(project['culture'] <= median, 'A', 'B')

project_A = project[project['group'] == 'A']
project_B = project[project['group'] == 'B']

dep_A = project_A['depression']
dep_B = project_B['depression']

mean_A = np.mean(dep_A)
mean_B = np.mean(dep_B)

nA = len(dep_A)
nB = len(dep_B)

pooled_std = np.sqrt(((nA-1)*np.std(dep_A)**2 + (nB-1)*np.std(dep_B)**2)/(nA+nB-2))

diff = mean_A - mean_B
se = pooled_std*np.sqrt(1/nA + 1/nB) 

print("Difference in Means: ", diff)
print("Standard Error: ", se)
print("Our answer is within range", (diff-se, diff+se))