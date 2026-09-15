Analysis of Student Learning Behavior and Academic Performance

Project Overview

This project analyzes student learning behavior and academic performance using a Kaggle dataset containing 14,003 student records and 16 attributes.

The analysis focuses on relationships between learning habits, engagement, resources, motivation, stress, and academic performance.

Objectives

Understand and prepare the student performance dataset

Analyze student learning and behavioral patterns

Investigate relationships between learning factors and exam performance

Examine the role of attendance, study hours, assignment completion, motivation, and stress

Identify factors showing meaningful relationships with academic performance

Present findings using statistical analysis and visualizations

Research Questions

How does study time relate to students' academic performance?

What relationship exists between attendance and exam scores?

Does assignment completion show an association with academic performance?

How are motivation and stress levels associated with student performance?

Which learning and behavioral factors show the strongest relationship with academic performance?

Dataset

Source: Kaggle – Student Performance and Learning Behavior Dataset

Original data: 14,003 records, 16 attributes

After cleaning: 12,469 records

The dataset contains variables related to study hours, attendance, resources, extracurricular activities, motivation, internet access, gender, age, learning style, online courses, discussions, assignment completion, exam score, educational technology usage, stress level, and final grade.

Methodology

The project follows this workflow:

Data Collection → Data Understanding → Data Cleaning → Exploratory Data Analysis → Correlation Analysis → Statistical Analysis → Regression → Visualization → Findings & Conclusion

Analysis Methods

Descriptive statistics

Exploratory Data Analysis (EDA)

Correlation analysis

ANOVA

Tukey HSD post-hoc testing

Multiple linear regression

Power BI visualization

Tools & Technologies

Python

Pandas

NumPy

Matplotlib

Seaborn

SciPy

Statsmodels

Scikit-learn

Kaggle Notebook

Power BI

GitHub

PowerPoint

Key Findings

The cleaned dataset contains 12,469 unique records.

Stress level shows a statistically significant difference in average exam scores, although the effect size is very small.

Assignment completion, discussions, and stress level show statistically significant relationships with exam performance in the analysis.

Study hours and attendance show very weak linear relationships with exam score in this dataset.

Multiple linear regression has weak predictive performance, with an R² of approximately 0.006.

Project Files

Data/
├── student_performance.csv
└── cleaned/
    └── student_performance_cleaned.csv

Documentation/
├── Project_Proposal.docx
├── Project_Gantt_Chart.png
└── Project_Mindmap.png

figures/
└── powerbi_dashboard.png

cleaning/
correlation/
eda/
regression/
statistical_analysis/

Student_Performance_Analysis.ipynb
README.md

Dashboard

An interactive Power BI dashboard was created to visualize student performance and learning behavior.

Limitations

The analysis is based on the available Kaggle dataset. The observed relationships are weak for many variables, so the results should not be interpreted as proof of causation or as a strong predictive model.

Project Deadline

Final submission: 16 September 2026
