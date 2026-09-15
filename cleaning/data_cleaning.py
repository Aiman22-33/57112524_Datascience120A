import pandas as pd

# Load the original dataset
file_path = "student_performance.csv"
df = pd.read_csv(file_path)

print("Original dataset shape:", df.shape)

# Check for missing values
missing_values = df.isnull().sum()

print("\nMissing values:")
print(missing_values)

# Check for duplicate records
duplicate_count = df.duplicated().sum()

print("\nNumber of duplicate records:", duplicate_count)

# Remove exact duplicate records
df_clean = df.drop_duplicates().copy()

print("\nCleaned dataset shape:", df_clean.shape)

# Verify that duplicates and missing values have been removed
print("\nRemaining duplicate records:", df_clean.duplicated().sum())
print("Remaining missing values:", df_clean.isnull().sum().sum())

# Save cleaned dataset
df_clean.to_csv("student_performance_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")
