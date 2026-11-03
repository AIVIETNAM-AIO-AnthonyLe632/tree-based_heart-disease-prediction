# Dictionary of the dataset

## 1. ChestPainType

This describes the character of chest pain, a powerful clinical indicator.
- TA — Typical Angina: Pain follows the classic pattern: triggered by exertion, relieved by rest, radiates to arm/jaw. Strongly associated with blocked coronary arteries.
- ATA — Atypical Angina: Some features resemble angina, others don’t. Less predictive but still concerning.
- NAP — Non-Anginal Pain: Pain unlikely to come from reduced blood flow (e.g., musculoskeletal, gastrointestinal).
- ASY — Asymptomatic: The patient reports no chest pain at all. Ironically, many serious cases sit here because silent ischemia is common.

## 2. RestingBP [mm Hg]

Resting blood pressure refers to the blood pressure reading taken when you are at rest, typically after sitting quietly for a few minutes.
According to the American Heart Association, the normal blood pressure reading for adults is generally considered to be **120/80 mm Hg**. Here’s a breakdown of the categories:

- Normal: Less than 120/80 mm Hg
- Elevated: 120-129/<80 mm Hg
- Hypertension Stage 1: 130-139/80-89 mm Hg
- Hypertension Stage 2: 140/90 mm Hg or higher.

High values signal strain on the cardiovascular system (hypertension)

## 3. Cholesterol [mm/dl]

Your cholesterol levels show how much cholesterol is circulating in your blood. Your HDL (“good” cholesterol) is the one number you want to be high (ideally 60 to 80). Your LDL (“bad” cholesterol) should be below 100. Your total should be below 200.
The serum total cholesterol ranges are as follows:

- Desirable: Below 200 mg/dL
- Borderline High: 200-239 mg/dL
- High: 240 mg/dL or above.
For adults, it is recommended to keep total cholesterol levels below **200 mg/dL**. Elevated cholesterol contributes to plaque buildup in arteries.

## 4. FastingBS > 120 mg/dl

  Fasting blood sugar refers to the measurement of glucose levels in your blood after not eating or drinking anything (except water) for 8 to 12 hours. This test is commonly used to screen for prediabetes, diabetes, or gestational diabetes.

- The normal fasting blood sugar range is typically between **70-99 mg/dL**.
- A fasting blood sugar level of **100-125 mg/dL** indicates prediabetes, while a level of **126 mg/dL** or higher suggests diabetes.

High fasting glucose hints at diabetes or pre-diabetes, both major cardiovascular risk factors.

## 5. RestingECG

Resting electrocardiogram results are like tiny electrical postcards from the heart. They capture how electrical signals travel through the chambers while the body is at rest. Each label below represents a pattern detected on that postcard, and each pattern hints at a different underlying story.

- Normal — expected waveform
- ST — ST-T wave abnormalities (e.g., inversion, elevation, depression) suggesting ischemia or repolarization issues
- LVH — signs of left-ventricular hypertrophy using Estes’ criteria, often from long-term high blood pressure

## 6. MaxHR

Maximum heart rate achieved during exercise stress test (range 60–202).
Lower-than-expected values may indicate chronotropic incompetence (the heart doesn’t speed up normally).
## 7. ExerciseAngina

Angina triggered by exercise.

- Y = Yes
- N = No

Exercise-induced symptoms strongly correlate with coronary artery blockages.

## 8. Oldpeak

Amount of ST segment depression during exercise compared to rest, measured in mm. Higher depression levels suggest worse ischemia during exertion.

- Positive values (oldpeak > 0): ST depression during exercise → classic sign of ischemia
- Zero (oldpeak = 0): No change from rest to exercise
- Negative values (oldpeak < 0): ST elevation during exercise → ST segment rises above baseline

## 9. ST_Slope

Shape of the ST segment at peak exercise:

- Up — Upsloping: Usually normal or low-risk; the ST segment rises gradually.
-  Flat — Flat ST segment: More concerning; often appears in ischemic patterns.
- Down — Downsloping: Strongly associated with reduced blood flow and higher risk.
- 