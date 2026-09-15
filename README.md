# Analysis of Student Learning Behavior and Academic Performance

## Project Overview

This project analyzes student learning behavior and its relationship with academic performance using a Kaggle dataset containing **14,003 student records and 16 attributes**.

The project examines learning habits, student engagement, access to resources, motivation, stress, and other behavioral factors in relation to **ExamScore**. The analysis combines data cleaning, exploratory data analysis, correlation analysis, statistical testing, regression analysis, and Power BI visualization.

## Problem Statement

Educational institutions collect large amounts of student-related data, but identifying which learning and behavioral factors are associated with academic performance can be challenging. Without systematic analysis, potentially useful patterns may remain unidentified.

This project analyzes student learning and engagement data to investigate relationships between factors such as study hours, attendance, assignment completion, motivation, stress, and academic performance.

## Objectives

- Understand and prepare the student performance dataset.
- Analyze student learning and behavioral patterns.
- Examine relationships between learning and engagement factors and exam performance.
- Investigate the relationships of study hours, attendance, assignment completion, motivation, and stress with ExamScore.
- Identify factors showing the strongest statistical relationships with academic performance.
- Present the findings through statistical analysis, visualizations, and an interactive Power BI dashboard.

## Research Questions

1. How does study time relate to students' academic performance?
2. What relationship exists between attendance and exam scores?
3. Does assignment completion show an association with academic performance?
4. How are motivation and stress levels associated with student performance?
5. Which learning and behavioral factors show the strongest relationship with academic performance?

## Dataset

**Dataset:** Student Performance and Learning Behavior Dataset  
**Source:** Kaggle  
**Original size:** 14,003 records × 16 attributes  
**Cleaned size:** 12,469 records × 16 attributes

### Main Variables

The dataset includes:

- StudyHours
- Attendance
- Resources
- Extracurricular
- Motivation
- Internet
- Gender
- Age
- LearningStyle
- OnlineCourses
- Discussions
- AssignmentCompletion
- ExamScore
- EduTech
- StressLevel
- FinalGrade

### Data Cleaning

The original dataset contains **1,534 exact duplicate rows**. These duplicate records were removed, resulting in **12,469 unique records** for the main analysis.

`FinalGrade` is treated as a derived outcome variable and is not used as an independent predictor in the regression model because it is strongly related to `ExamScore`.

## Methodology

The project follows this workflow:

**Data Collection → Data Understanding → Data Cleaning → Exploratory Data Analysis → Correlation Analysis → Statistical Analysis → Regression Analysis → Visualization → Findings & Conclusion**

### 1. Data Understanding

The dataset structure, variables, data types, ranges, distributions, and data quality were examined.

### 2. Data Cleaning

Duplicate records were identified and removed. The cleaned dataset was saved for further analysis.

### 3. Exploratory Data Analysis

Descriptive statistics and visualizations were used to examine:

- Exam score distribution
- Study hours and exam score
- Attendance and exam score
- Assignment completion and exam score
- Motivation and exam score
- Stress level and exam score

### 4. Correlation Analysis

Pearson correlation was used to examine the linear relationships between numerical variables and `ExamScore`.

### 5. Statistical Analysis

ANOVA was used to compare mean exam scores across selected groups. Tukey HSD post-hoc testing was used where appropriate to identify group differences.

### 6. Regression Analysis

Multiple linear regression was used to evaluate the combined relationship between selected learning and behavioral variables and `ExamScore`.

### 7. Visualization

Results were presented using Python visualizations and an interactive Power BI dashboard.

## Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **SciPy**
- **Statsmodels**
- **Scikit-learn**
- **Kaggle Notebook**
- **Power BI**
- **GitHub**
- **PowerPoint**

## Key Findings

- The dataset contains **14,003 original records** and **16 attributes**.
- After removing duplicate records, **12,469 unique records** remained.
- `StudyHours` and `Attendance` show very weak linear relationships with `ExamScore` in this dataset.
- `AssignmentCompletion`, `Discussions`, and `StressLevel` show statistically significant associations with `ExamScore`, although their effects are small.
- Stress level shows a statistically significant difference in average exam scores across groups, but the effect size is very small.
- The multiple linear regression model has **R² ≈ 0.006**, indicating weak overall predictive/explanatory power for `ExamScore`.

These findings should be interpreted as **associations rather than causal effects**.

## Power BI Dashboard

An interactive Power BI dashboard was created to present:

- Student and performance KPIs
- Study hours vs. exam score
- Attendance vs. exam score
- Assignment completion vs. exam score
- Exam score by motivation level
- Exam score by stress level
- Exam score by discussions
- Exam score by online courses
- Exam score by learning style
- Exam score by final grade

The dashboard also includes filters for **Motivation** and **StressLevel**.

## Project Structure

```text
57112524_Datascience120A/
│
├── Data/
│   ├── student_performance.csv
│   └── cleaned/
│       └── student_performance_cleaned.csv
│
├── Documentation/
│   ├── Project_Proposal.docx
│   ├── Project_Gantt_Chart.png
│   └── Project_Mindmap.png
│
├── figures/
│   └── powerbi_dashboard.png
│
├── cleaning/
├── correlation/
├── eda/
├── regression/
├── statistical_analysis/
│
├── Student_Performance_Analysis.ipynb
└── README.md
