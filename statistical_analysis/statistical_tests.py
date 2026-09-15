import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Load the cleaned dataset
file_path = "../Data/cleaned/student_performance_cleaned.csv"
df = pd.read_csv(file_path)

print("Cleaned dataset loaded successfully.")
print("Dataset shape:", df.shape)

# --------------------------------------------------
# 1. ANOVA: Stress Level and Exam Score
# --------------------------------------------------

stress_groups = [
    group["ExamScore"].values
    for _, group in df.groupby("StressLevel")
]

stress_anova = stats.f_oneway(*stress_groups)

print("\nANOVA: Stress Level vs Exam Score")
print("F-statistic:", stress_anova.statistic)
print("p-value:", stress_anova.pvalue)

# Tukey HSD post-hoc test
tukey_stress = pairwise_tukeyhsd(
    endog=df["ExamScore"],
    groups=df["StressLevel"],
    alpha=0.05
)

print("\nTukey HSD: Stress Level")
print(tukey_stress)

# --------------------------------------------------
# 2. ANOVA: Motivation Level and Exam Score
# --------------------------------------------------

motivation_groups = [
    group["ExamScore"].values
    for _, group in df.groupby("Motivation")
]

motivation_anova = stats.f_oneway(*motivation_groups)

print("\nANOVA: Motivation Level vs Exam Score")
print("F-statistic:", motivation_anova.statistic)
print("p-value:", motivation_anova.pvalue)

print("\nStatistical analysis completed successfully.")
