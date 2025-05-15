import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

project = pd.read_excel("project.xlsx")

median = project['culture'].median()

project['group'] = np.where(project['culture'] <= median, 'A', 'B')

project_A = project[project['group'] == 'A']
project_B = project[project['group'] == 'B']

dep_A = project_A['depression']
dep_B = project_B['depression']

data=[dep_A,dep_B]

ax = sns.boxplot(data=data, palette=["#071b4b", "#38e8a4"])

ax.set(xlabel='Cultural Group', ylabel='Depression')
ax.set_xticklabels(['Below median','Above median']) 

plt.legend(labels = ['Below median','Above median'])
plt.show()