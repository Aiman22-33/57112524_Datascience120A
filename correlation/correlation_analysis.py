import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "../Data/cleaned/student_performance_cleaned.csv"
df = pd.read_csv(file_path)

print("Cleaned dataset loaded successfully.")
print("Dataset shape:", df.shape)

# Calculate correlations with ExamScore
correlations = (
    df.corr(numeric_only=True)["ExamScore"]
    .drop("ExamScore")
    .sort_values(ascending=False)
)

print("\nCorrelation with ExamScore:")
print(correlations)

# Correlation heatmap
plt.figure(figsize=(12, 9))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Display the strongest relationships
print("\nStrongest positive/negative relationships with ExamScore:")
print(correlations)
