# forms.py
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class BloodPressureForm(forms.Form):
    level_of_hemoglobin = forms.FloatField(label='Level of Hemoglobin', initial=0)
    genetic_pedigree_coefficient = forms.FloatField(label='Genetic Pedigree Coefficient', initial=0)
    age = forms.IntegerField(label='Age', initial=0)
    bmi = forms.FloatField(label='BMI', initial=0)
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')], initial='male')
    smoking = forms.BooleanField(label='Smoking', initial=False, required=False)
    smoking_frequency = forms.IntegerField(label='Number of times smoked per day', initial=0, min_value=0)
    physical_activity = forms.ChoiceField(label='Physical Activity',
                                          choices=[('sedentary', 'Sedentary'),
                                                   ('lightly_active', 'Lightly Active'),
                                                   ('moderately_active', 'Moderately Active'),
                                                   ('very_active', 'Very Active')],
                                          initial='sedentary')
    salt_content_in_the_diet = forms.ChoiceField(label='Salt Content in the Diet',
                                                  choices=[('0.3g salt or less per 100g', '0.3g salt or less per 100g'),
                                                           ('between 1.5 and 2.3 grams of sodium per day', 'between 1.5 and 2.3 grams of sodium per day'),
                                                           ('more than 1.5g salt per 100g', 'more than 1.5g salt per 100g')],
                                                  initial='0.3g salt or less per 100g')
    alcohol_consumption_per_day = forms.ChoiceField(label='Alcohol Consumption per Day',
                                                    choices=[('none', 'None'),
                                                             ('moderate', 'Moderate (1-2 drinks per day)'),
                                                             ('heavy', 'Heavy (3 or more drinks per day)')],
                                                    initial='none')
    level_of_stress = forms.ChoiceField(label='Level of Stress',
                                        choices=[('low', 'Low'),
                                                 ('moderate', 'Moderate'),
                                                 ('high', 'High')],
                                        initial='low')
    chronic_kidney_disease = forms.BooleanField(label='Chronic Kidney Disease', initial=False, required=False)
    adrenal_and_thyroid_disorders = forms.BooleanField(label='Adrenal and Thyroid Disorders', initial=False, required=False)



class ThyroidForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[('male', 'Male'), ('female', 'Female')])
    on_thyroxine = forms.ChoiceField(label='On Thyroxine', choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    on_antithyroid_meds = forms.ChoiceField(label='On Antithyroid Medication', choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    sick = forms.ChoiceField(label='Sick',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    thyroid_surgery = forms.ChoiceField(label='Underwent Thyroid Surgery',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    I131_treatment = forms.ChoiceField(label='Undergoing Iodine 131 Treatment',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    query_hypothyroid = forms.ChoiceField(label='Query Hypothyroid',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    query_hyperthyroid = forms.ChoiceField(label='Query Hyperthyroid', choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')],required=False)
    lithium = forms.ChoiceField(label='Lithium',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    goitre = forms.ChoiceField(label='Goitre',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    tumor = forms.ChoiceField(label='Tumor',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    hypopituitary = forms.ChoiceField(label='Hypopituitary',choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')], required=False)
    psych = forms.BooleanField(label='Psych', required=False)
    TSH_measured = forms.BooleanField(label='TSH Measured', required=False)
    TSH = forms.FloatField(label='TSH', required=False)
    T3_measured = forms.BooleanField(label='T3 Measured', required=False)
    T3 = forms.FloatField(label='T3', required=False)
    TT4_measured = forms.BooleanField(label='TT4 Measured', required=False)
    TT4 = forms.FloatField(label='TT4', required=False)
    T4U_measured = forms.BooleanField(label='T4U Measured', required=False)
    T4U = forms.FloatField(label='T4U', required=False)
    FTI_measured = forms.BooleanField(label='FTI Measured', required=False)
    FTI = forms.FloatField(label='FTI', required=False)
    TBG_measured = forms.BooleanField(label='TBG Measured', required=False)
    TBG = forms.FloatField(label='TBG', required=False)



class DiabetesForm(forms.Form):
    glucose = forms.FloatField(label='Plasma Glucose Concentration (2 hours) in OGTT', min_value=50, max_value=250)
    blood_pressure = forms.FloatField(label='Diastolic Blood Pressure (mm Hg)', min_value=40, max_value=150)
    skin_thickness = forms.FloatField(label='Triceps Skin Fold Thickness (mm)', min_value=5, max_value=80)
    insulin = forms.FloatField(label='2-Hour Serum Insulin (mu U/ml)', min_value=0, max_value=1000)
    bmi = forms.FloatField(label='Body Mass Index (BMI)', min_value=10, max_value=60)
    diabetes_pedigree_function = forms.FloatField(label='Diabetes Pedigree Function', min_value=0, max_value=2)
    age = forms.IntegerField(label='Age', min_value=18, max_value=100)




class DiabetesFormRN(forms.Form):
    age = forms.IntegerField(label='Age', validators=[MinValueValidator(0), MaxValueValidator(150)])
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], label='Gender')
    blood_pressure_systolic = forms.IntegerField(label='Blood Pressure (Systolic)', validators=[MinValueValidator(0), MaxValueValidator(300)])
    blood_pressure_diastolic = forms.IntegerField(label='Blood Pressure (Diastolic)', validators=[MinValueValidator(0), MaxValueValidator(200)])
    urinary_ACR = forms.FloatField(label='Urinary Albumin-to-Creatinine Ratio (ACR)', validators=[MinValueValidator(0)])
    serum_creatinine = forms.FloatField(label='Serum Creatinine Level', validators=[MinValueValidator(0)])
    GFR = forms.FloatField(label='Glomerular Filtration Rate (GFR)', validators=[MinValueValidator(0)])
    kidney_biopsy_results = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Kidney Biopsy Results')
    visual_acuity = forms.FloatField(label='Visual Acuity (VA)', validators=[MinValueValidator(0)])
    presence_of_microaneurysms = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Presence of Microaneurysms')
    presence_of_hemorrhages = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Presence of Hemorrhages')
    presence_of_exudates = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Presence of Exudates')
    neovascularization = forms.ChoiceField(choices=[('no', 'No'), ('yes', 'Yes')], label='Neovascularization')
    OCT_results = forms.FloatField(label='OCT Results', validators=[MinValueValidator(0)])
    fluorescein_angiography_results = forms.FloatField(label='Fluorescein Angiography Results', validators=[MinValueValidator(0)])
    retinal_photography_results = forms.FloatField(label='Retinal Photography Results', validators=[MinValueValidator(0)])

