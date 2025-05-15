import pandas as pd
import numpy as np

project = pd.read_excel('project.xlsx')

culture_med = project['culture'].median()
depression_med = project['depression'].median()
project['culture_group'] = np.where(project['culture'] <= culture_med, 'Low', 'High')
project['depression_group'] = np.where(project['depression'] <= depression_med, 'Low', 'High')

crosstab = pd.crosstab(project['culture_group'], project['depression_group'])
print(crosstab)

HCifLD = crosstab.loc['High', 'Low'] / crosstab.loc['Low', 'Low']
HCifHD = crosstab.loc['High', 'High'] / crosstab.loc['Low', 'High']
HDifLC = crosstab.loc['Low', 'High'] / crosstab.loc['Low', 'Low']
HDifHC = crosstab.loc['High', 'High'] / crosstab.loc['High', 'Low']

print("Risk Ratio for High Culture if Low Depression:", HCifLD)
print("Risk Ratio for High Culture if High Depression:", HCifHD)
print("Risk Ratio for High Depression if Low Culture:", HDifLC)
print("Risk Ratio for High Depression if High Culture:", HDifHC)