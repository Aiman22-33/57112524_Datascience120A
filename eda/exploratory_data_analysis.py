import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
file_path = "../Data/cleaned/student_performance_cleaned.csv"
df = pd.read_csv(file_path)

print("Cleaned dataset loaded successfully.")
print("Dataset shape:", df.shape)

# Basic descriptive statistics
print("\nDescriptive statistics:")
print(df.describe().T)

# 1. Distribution of Exam Scores
plt.figure(figsize=(10, 6))
sns.histplot(df["ExamScore"], bins=20, kde=True)
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

# 2. Study Hours vs Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="StudyHours", y="ExamScore", alpha=0.5)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# 3. Attendance vs Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Attendance", y="ExamScore", alpha=0.5)
plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# 4. Assignment Completion vs Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="AssignmentCompletion", y="ExamScore", alpha=0.5)
plt.title("Assignment Completion vs Exam Score")
plt.xlabel("Assignment Completion")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# 5. Motivation Level vs Exam Score
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Motivation", y="ExamScore", errorbar=None)
plt.title("Average Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.show()

# 6. Stress Level vs Exam Score
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="StressLevel", y="ExamScore", errorbar=None)
plt.title("Average Exam Score by Stress Level")
plt.xlabel("Stress Level")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.show()

print("\nEDA completed successfully.")
