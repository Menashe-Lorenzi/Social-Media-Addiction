# Social-Media-Addiction

# Analysis of the Relationship Between Social Media Usage and Mental Health Among Students

## Project Description

[cite_start]This project was conducted as part of the "Statistical Theory" course. The objective is to investigate the complex relationship between social media usage habits and personal well-being metrics, particularly mental health, among students. Using tools of statistical inference and regression modeling, we aim to identify the most significant factors contributing to mental health and to quantify their impact.

The analysis seeks to "tell a story" about the challenges faced by young adults in the digital age, using data to move from intuition to evidence-based statistical insights.

### Central Research Question

What is the impact of social media usage habits on students' mental health, and which factors are the most significant predictors of a lower mental health score?

## Dataset

The analysis is based on the "Students' Social Media Addiction" dataset, available on Kaggle.

* **Dataset Link:** [Social Media Addiction vs Relationships](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)
* **Description:** The dataset contains data collected via a survey of students. It includes information on demographics, social media usage habits, sleep quality, relationship status, and mental health metrics.

## Statistical Methodology

[cite_start]The analysis was performed using the following tools, in accordance with the course requirements:

1.  **Descriptive Statistics and Visualization:**
    * Presenting the distributions of key variables using histograms and box plots.
    * Examining initial relationships between variables using scatter plots.

2.  **Hypothesis Testing:**
    * **Two-sample t-tests:** To compare the mean mental health scores between different groups (e.g., by gender or sleep quality).
    * **Pearson's correlation coefficient test:** To examine the linear relationship between quantitative variables (like usage hours and mental health score).
    * **Chi-squared ($\chi^2$) test:** To test for independence between categorical variables (such as relationship status and conflict levels).

3.  **Multiple Linear Regression Model:**
    * Building a model to predict the `Mental_Health_Score` dependent variable.
    * Testing the overall model significance using the **F-test**.
    * Testing the significance of each predictor using **t-tests**.
    * Interpreting coefficients and calculating 95% **Confidence Intervals**.
    * Evaluating model performance using metrics like **$R^2$** and **MSE**.
    * Checking model assumptions through **residual analysis**.

## Repository Structure

```
.
├── data/
│   └── social_media_addiction.csv    # The raw data file
├── notebooks/
│   └── Statistical_Analysis.ipynb    # Jupyter Notebook with the full analysis, code, and plots
├── Final_Report.pdf                  # The final summary project report
├── requirements.txt                  # List of required libraries to run the code
└── README.md                         # This file
```

## How to Reproduce the Analysis

To reproduce the full analysis, please follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your_username/your_repository_name.git](https://github.com/your_username/your_repository_name.git)
    cd your_repository_name
    ```

2.  **Install Dependencies:**
    Ensure you have Python 3 installed. Then, install all required libraries using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Analysis:**
    Open the `Statistical_Analysis.ipynb` notebook located in the `notebooks/` directory using Jupyter Notebook or JupyterLab, and run all cells in order.
    ```bash
    jupyter notebook notebooks/Statistical_Analysis.ipynb
    ```
The notebook contains all the detailed steps of the analysis, from data loading to the final model creation and visualizations.

## Summary of Findings

Our analysis reveals that behavioral factors related to social media use have a statistically significant relationship with mental health. The strongest predictors of a lower mental health score were found to be **fewer hours of sleep**, a **high average of daily usage hours**, and a **high level of conflict arising from social media use**.

The model we constructed successfully explains approximately XX% of the variance in mental health scores, providing valuable insights into the profiles of students at risk of diminished well-being. For complete details, please refer to the final report.

---
