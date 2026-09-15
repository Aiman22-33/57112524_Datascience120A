import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import numpy as np

# Load the cleaned dataset
file_path = "../Data/cleaned/student_performance_cleaned.csv"
df = pd.read_csv(file_path)

print("Cleaned dataset loaded successfully.")
print("Dataset shape:", df.shape)

# Use ExamScore as the target variable
# FinalGrade is excluded because it is a derived outcome
X = df.drop(columns=["ExamScore", "FinalGrade"])
y = df["ExamScore"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Create and train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict ExamScore
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nMultiple Linear Regression Results")
print("R²:", round(r2, 4))
print("RMSE:", round(rmse, 2))

# Display coefficients
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nRegression coefficients:")
print(coefficients)

print("\nRegression analysis completed successfully.")
