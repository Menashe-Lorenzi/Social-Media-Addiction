# Social-Media-Addiction
Social Media Addiction and Student Well-being: A Cross-Platform Statistical Analysis

**Project Overview**
This project delves into the multifaceted impact of social media usage on students' academic performance and mental health. Utilizing a comprehensive dataset, we analyze the interplay between the most frequently used social media platforms and levels of social media addiction to determine their combined influence on key student outcomes. The analysis focuses on common and well-represented platforms within the dataset to ensure robust statistical power and reliable subgroup comparisons.

## Research Questions
- How do specific social media platforms and varying levels of addiction jointly affect students' academic performance?
- Are there significant differences in mental health scores among students, influenced by their primary social media platform and their addiction levels?
- Do the relationships between platform use and academic/mental health outcomes change depending on the level of social media addiction?

## Dataset
The analysis utilizes a dataset containing information on students' social media habits, academic performance indicators, and mental health metrics. Key variables include:

- Most_Used_Platform: Nominal categorical variable (e.g., Instagram, TikTok, Facebook, WhatsApp, Twitter, LinkedIn).
- Addicted_Score: Ordinal numeric variable representing a student's social media addiction level.
- Affects_Academic_Performance: Binary outcome variable (e.g., Yes/No).
- Mental_Health_Score: Ordinal outcome variable.

## Methodology
This project employs a robust statistical approach to uncover nuanced relationships:

- Interaction Term Creation: An interaction term between Most_Used_Platform and Addicted_Score will be created to explore synergistic
effects.
- Logistic Regression: For the binary outcome variable (Affects_Academic_Performance), a logistic regression model will be utilized to assess the predictive power of platforms, addiction scores, and their interaction on the likelihood of academic impact.

**Analysis for Ordinal Outcome (Mental_Health_Score):**

- Ordinal Logistic Regression: If statistical assumptions are met, an ordinal logistic regression model will be employed to examine the influence of platforms, addiction, and their interaction on Mental_Health_Score.
- Mann–Whitney U Test: As an alternative, or to complement the ordinal logistic regression, Mann–Whitney U Test will be conducted. These non-parametric tests will be performed both within addiction strata (comparing platforms at specific addiction levels) and within platform strata (comparing addiction levels on specific platforms) to understand how differences in Mental_Health_Score manifest across these subgroups, especially given observed violations of homogeneity of variance.

## Expected Outcomes
This combined analysis aims to provide insights into:

- Whether certain platforms are more detrimental to academic performance or mental health, particularly at higher addiction levels.
- Whether the impact of social media addiction is consistent across different social media platforms.
- A deeper understanding of the joint effect of platform usage and addiction on student well-being, informing potential interventions or awareness campaigns.
___
Original dataset: Kaggle ([linked above](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)).
License
MIT License – feel free to use and modify.
___
Contact
LinkedIn: Menashe Lorenzi | Email: menashelorenzi@gmail.com
___
MIT License

Copyright (c) 2025 Menashe Lorenzi

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
