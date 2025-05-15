import pandas as pd
import statsmodels.api as sm

project = pd.read_excel('project.xlsx')

x = sm.add_constant(project['culture'])
y = project['depression']

model = sm.OLS(y, x).fit()

print(model.summary())

t_test = model.t_test("culture = 0")

print("T-test:")
print("t-statistic:", t_test.tvalue)
print("p-value:", t_test.pvalue)

f_test = model.f_test("culture = 0")

print("F-test:")
print("F-statistic:", f_test.fvalue)
print("p-value:", f_test.pvalue)

if model.pvalues['culture'] < 0.05:
    print("The coefficient of 'culture' is significantly different from zero.")
else:
    print("The coefficient of 'culture' is not significantly different from zero.")
if f_test.pvalue < 0.05:
    print("The overall model is significant.")
else:
    print("The overall model is not significant.")    