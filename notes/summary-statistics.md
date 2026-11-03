Cholesterol = 0 accounts for 18.74% of the dataset.

It's impossible for a person to have 0 cholesterol => this should be missingness

Restingbp = 0 => also a missingness => should be filled up

Restingbp lower than normal condition? I don't know what to do yet

Population of female in this dataset is less, female with heart disease is even less

Categories that have hight percentage of heart disease:

- Exerciseangina = Y
- Flat st_slope
- ASY chestpaintype
- Male
- Normal RestingECG

Heart disease tends to increase by age, and more prevalent in male, in people with high resting blood pressure, and in people with oldpeak > 0, and in people with low maxhr

- Resting blood pressure tends to increase by age, no matter having heart disease or not
- Max heart rate skews left in those who have heart disease => low max heart rate may signify an increased risk of heart diseases or other medical condition
  - [What is a normal heart rate?](https://www.health.harvard.edu/heart-health/what-your-heart-rate-is-telling-you)
- People with oldpeak > 0 tends to have heart disease
- High cholesterol + >0 oldpeak tend to have heart disease
- HIhg resting blood pressure + > 0 oldpeak tend to have heart disease