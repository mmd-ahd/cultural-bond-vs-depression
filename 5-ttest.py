import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

project = pd.read_excel("project.xlsx")

median = project['culture'].median()

project['group'] = np.where(project['culture'] <= median, 'A', 'B')

project_A = project[project['group'] == 'A']
project_B = project[project['group'] == 'B']

dep_A = project_A['depression']
dep_B = project_B['depression']

t_stat, p_val = ttest_ind(dep_A, dep_B)
print("T-Statistic: ", t_stat)
print("p-value: ", p_val)

if p_val > 0.05:
    print("depression mean is equal in both groups")
else:
    print("depression mean is not equal between groups")