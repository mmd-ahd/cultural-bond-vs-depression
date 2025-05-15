# Cultural Bond & Depression Tendency  
**Course:** Bio-Statistics & Probability  
**Supervised by:** Dr. Mehrdad Saviz  
**Authors:**  
- Mohammad Ahadzadeh 
- Mohammad Nima Madankar  
- Sina Sahami

**Date:** May 2024  

---

## Project Overview  
This project investigates the statistical relationship between an individual’s **cultural bond** (sense of belonging and engagement with their cultural values and practices) and their **tendency toward depression**. We apply a suite of classical statistical methods—correlation analysis, linear and non‑linear regression, ANOVA, t‑tests, χ² contingency tables, and relative‑risk estimation—to survey data collected from student participants (ages 18–30).

---

## Objectives  
1. **Test for correlation** between cultural bond and depression tendency (Pearson’s r).  
2. **Build a regression model** (linear & non‑linear) to quantify how cultural bond predicts depression scores.  
3. **Compare groups** (high vs. low cultural bond) using ANOVA and independent‑samples t‑tests.  
4. **Assess categorical risk** via χ² tables and compute relative‑risk ratios.  
5. **Provide evidence‑based recommendations** to strengthen cultural engagement as a protective factor against depression.

---

## Data  
- **Source:** Survey responses collected from 75 students (ages 18–30).  
- **Variables:**  
  - `Culture` — continuous score of cultural bond  
  - `Depression` — continuous depression tendency score  
- **Preprocessing:**  
  - Imported into pandas DataFrame  
  - Median split to create “High” vs. “Low” groups  

---

## Tools & Libraries  
- **Python 3.x**  
  - pandas, NumPy, SciPy, statsmodels  
  - Matplotlib  
- **MS Excel** (initial data cleaning & cross‑validation)  
- **Jupyter Notebook** (analysis walkthrough)  

---

## Statistical Methods  

| Method                      | Purpose                                            |
|-----------------------------|----------------------------------------------------|
| **Pearson Correlation**     | Test H₀: ρ=0 vs. H₁: ρ≠0                           |
| **Linear Regression (OLS)** | Estimate β coefficient; t‑ and F‑tests for significance |
| **Non‑Linear Regression**   | Curve‑fit alternative model for `Depression ~ Culture` |
| **One‑Way ANOVA**           | Compare group means across “High” vs. “Low” Culture |
| **Independent t‑Test**      | Compare two group means (α=0.05)                   |
| **χ² Contingency Table**    | Crosstab of categorical splits; compute relative‑risk |
| **Relative‑Risk**           | Quantify risk ratio of Low vs. High culture groups |
