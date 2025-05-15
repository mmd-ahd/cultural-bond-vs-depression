import pandas as pd
import numpy as np
from scipy import stats

project = pd.read_excel("project.xlsx")

median = project['culture'].median()

project['group'] = np.where(project['culture'] <= median, 'A', 'B')

project_A = project[project['group'] == 'A']
project_B = project[project['group'] == 'B']

dep_A = project_A['depression']
dep_B = project_B['depression']

f_stat, p_value = stats.f_oneway(dep_A,dep_B)

print("F-statistic", f_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("there is a significant difference between the groups.")
else:
    print("there is not a significant difference between the groups.")