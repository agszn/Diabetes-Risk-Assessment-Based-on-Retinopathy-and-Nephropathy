from django.shortcuts import render
from diabetes_Thyroid_BP.forms import *

import serial
from django.shortcuts import render
import numpy as np
import serial
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib


def detect_blood_pressure(request):
    if request.method == 'POST':
        form = BloodPressureForm(request.POST)
        if form.is_valid():
            # Retrieve input values from the form
            level_of_hemoglobin = form.cleaned_data['level_of_hemoglobin']
            genetic_pedigree_coefficient = form.cleaned_data['genetic_pedigree_coefficient']
            age = form.cleaned_data['age']
            bmi = form.cleaned_data['bmi']
            sex = form.cleaned_data['sex']
            smoking = form.cleaned_data['smoking']
            smoking_frequency = form.cleaned_data['smoking_frequency']
            physical_activity = form.cleaned_data['physical_activity']
            salt_content_in_the_diet = form.cleaned_data['salt_content_in_the_diet']
            alcohol_consumption_per_day = form.cleaned_data['alcohol_consumption_per_day']
            level_of_stress = form.cleaned_data['level_of_stress']
            chronic_kidney_disease = form.cleaned_data['chronic_kidney_disease']
            adrenal_and_thyroid_disorders = form.cleaned_data['adrenal_and_thyroid_disorders']
            
            # Perform BP detection based on input values
            # Implement your logic here to detect high blood pressure
            # For example:
            if age > 40 and bmi > 25:
                has_high_bp = True
                bp_level = "High"
            else:
                has_high_bp = False
                bp_level = "Normal"
            
            # Suggest exercises based on physical activity level
            # Implement your logic here to suggest exercises
            suggested_exercises = []
            if physical_activity == 'sedentary':
                suggested_exercises.append("Walking for 30 minutes daily.")
            elif physical_activity == 'lightly_active':
                suggested_exercises.append("Brisk walking or cycling for 30 minutes daily.")
            elif physical_activity == 'moderately_active':
                suggested_exercises.append("Aerobic exercises like swimming or running for 30 minutes daily.")
            elif physical_activity == 'very_active':
                suggested_exercises.append("High-intensity interval training (HIIT) for 20 minutes, 3 times a week.")
            
            # Recommend doctors based on detected conditions
            recommended_doctors = []
            if has_high_bp:
                recommended_doctors.append("Cardiologist")
            if smoking:
                recommended_doctors.append("Pulmonologist")
            if chronic_kidney_disease:
                recommended_doctors.append("Nephrologist")
            if adrenal_and_thyroid_disorders:
                recommended_doctors.append("Endocrinologist")
            
            # Render the result page with detected information
            return render(request, 'blood_pressure_result.html', {
                'has_high_bp': has_high_bp,
                'bp_level': bp_level,
                'suggested_exercises': suggested_exercises,
                'recommended_doctors': recommended_doctors,
            })
    else:
        form = BloodPressureForm()
    
    return render(request, 'blood_pressure_form.html', {'form': form})

#thyroid

def detect_thyroid(request):
    if request.method == 'POST':
        form = ThyroidForm(request.POST)
        if form.is_valid():
            # Retrieve input values from the form
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            on_thyroxine = form.cleaned_data['on_thyroxine']
            on_antithyroid_meds = form.cleaned_data['on_antithyroid_meds']
            sick = form.cleaned_data['sick']
            thyroid_surgery = form.cleaned_data['thyroid_surgery']
            I131_treatment = form.cleaned_data['I131_treatment']
            query_hypothyroid = form.cleaned_data['query_hypothyroid']
            query_hyperthyroid = form.cleaned_data['query_hyperthyroid']
            lithium = form.cleaned_data['lithium']
            goitre = form.cleaned_data['goitre']
            tumor = form.cleaned_data['tumor']
            hypopituitary = form.cleaned_data['hypopituitary']
            psych = form.cleaned_data['psych']
            TSH_measured = form.cleaned_data['TSH_measured']
            TSH = form.cleaned_data['TSH']
            T3_measured = form.cleaned_data['T3_measured']
            T3 = form.cleaned_data['T3']
            TT4_measured = form.cleaned_data['TT4_measured']
            TT4 = form.cleaned_data['TT4']
            T4U_measured = form.cleaned_data['T4U_measured']
            T4U = form.cleaned_data['T4U']
            FTI_measured = form.cleaned_data['FTI_measured']
            FTI = form.cleaned_data['FTI']
            TBG_measured = form.cleaned_data['TBG_measured']
            TBG = form.cleaned_data['TBG']
            
            # Logic to detect thyroid issues
            has_thyroid_issues = False
            # Implement your logic to detect thyroid issues based on the input values
            # For example:
            if query_hypothyroid or query_hyperthyroid or TSH_measured and (TSH > 4.0 or TSH < 0.4):
                has_thyroid_issues = True
            
            # Suggest precautions and recommend doctors
            precautions = []
            recommended_doctors = []
            if has_thyroid_issues:
                precautions.append("Consult an endocrinologist for further evaluation.")
                precautions.append("Follow up with regular thyroid function tests.")

            if has_thyroid_issues:
                recommended_doctors.append("Dakshata Hospital Pvt Ltd: Tilakwadi Belgaum, Belgaum")
                recommended_doctors.append("VIVEKANAND MULTISPECIALITY HOSPITAL : Belgaum City, Belgaum")
            
            # Render the result page with detected information, precautions, and recommended doctors
            return render(request, 'thyroid_result.html', {
                'has_thyroid_issues': has_thyroid_issues,
                'precautions': precautions,
                'recommended_doctors': recommended_doctors,
            })
    else:
        form = ThyroidForm()
    
    return render(request, 'thyroid_form.html', {'form': form})


def predict_diabetes(request):
    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            # Get input values from the form
            glucose = form.cleaned_data['glucose']
            blood_pressure = form.cleaned_data['blood_pressure']
            skin_thickness = form.cleaned_data['skin_thickness']
            insulin = form.cleaned_data['insulin']
            bmi = form.cleaned_data['bmi']
            diabetes_pedigree_function = form.cleaned_data['diabetes_pedigree_function']
            age = form.cleaned_data['age']


            diabetes_score = (glucose + blood_pressure + skin_thickness + insulin + bmi +
                                        diabetes_pedigree_function + age) / 7

            if diabetes_score > 100:
                complexity = "High"
                suggestions = [
                    "Consult with a specialist immediately.",
                    "Strictly monitor blood sugar levels.",
                    "Follow a personalized diet plan.",
                ]
            elif diabetes_score > 50:
                complexity = "Medium"
                suggestions = [
                    "Exercise regularly and maintain a healthy lifestyle.",
                    "Consult with a healthcare professional for personalized advice.",
                    "Monitor blood sugar levels regularly.",
                ]
            else:
                complexity = "Low"
                suggestions = [
                    "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
                    "Regularly engage in physical activity.",
                    "Monitor blood sugar levels periodically.",
                ]
            # For demonstration purposes, let's assume a generic doctor recommendation
            recommended_doctors = [
                "Dr. John Doe - Endocrinologist",
                "Dr. Jane Smith - General Practitioner",
            ]

            # For demonstration purposes, let's assume a generic medication recommendation
            recommended_medications = [
                "Metformin - oral medication for type 2 diabetes",
                "Insulin injections (if required)",
            ]

            # Food recommendations based on diabetes status
            if glucose > 140:  # Example threshold, adjust as needed
                food_recommendations = {
                    'recommended': [
                        "Lean proteins (e.g., chicken, fish)",
                        "High-fiber foods (e.g., fruits, vegetables, whole grains)",
                        "Healthy fats (e.g., nuts, avocados)",
                        "Non-starchy vegetables (e.g., spinach, broccoli)",
                    ],
                    'avoid': [
                        "Sugary beverages (e.g., soda, fruit juices)",
                        "Processed foods high in refined carbohydrates (e.g., white bread, pastries)",
                        "Fried foods",
                        "Sugary snacks and desserts",
                    ]
                }
            else:
                food_recommendations = {
                    'recommended': [
                        "Lean proteins (e.g., chicken, fish)",
                        "High-fiber foods (e.g., fruits, vegetables, whole grains)",
                        "Healthy fats (e.g., nuts, avocados)",
                        "Non-starchy vegetables (e.g., spinach, broccoli)",
                    ],
                    'avoid': [
                        "Sugary beverages (e.g., soda, fruit juices)",
                        "Processed foods high in refined carbohydrates (e.g., white bread, pastries)",
                        "Fried foods",
                        "Sugary snacks and desserts",
                    ]
                }

            # Render the result page with predictions, recommendations, and food suggestions
            return render(request, 'diabetes_result.html', {
                'glucose': glucose,
                'blood_pressure': blood_pressure,
                'skin_thickness': skin_thickness,
                'insulin': insulin,
                'bmi': bmi,
                'diabetes_pedigree_function': diabetes_pedigree_function,
                'age': age,
                'suggestions': suggestions,
                'recommended_doctors': recommended_doctors,
                'recommended_medications': recommended_medications,
                'food_recommendations': food_recommendations,
                'complexity': complexity,
            })
    else:
        form = DiabetesForm()
    return render(request, 'diabetes_form.html', {'form': form})



import serial
def read_sensor_data(request):
    if request.method == 'GET':
        # Serial port configuration
        ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with your serial port
        ser.flushInput()

        try:
            sensor_data_list = []
            recommendations = []  # Initialize list to store recommendations

            while True:
                # Read a line from the serial port
                try:
                    line = ser.readline().decode('latin-1').strip()
                except UnicodeDecodeError as e:
                    print("Error decoding line:", e)
                    continue  # Skip processing this line
                
                sensor_data_list.append(line)
 
                # Limit the number of sensor data to be sent to the frontend for demonstration
                if len(sensor_data_list) >= 20:
                    break
                    
            
            return render(request, 'sensor_data.html', {'sensor_data_list': sensor_data_list})
                    
        except KeyboardInterrupt:
            print("Interrupted. Exiting...")
        finally:
            ser.close()
    
    return render(request, 'sensor_data.html', {'error': 'Invalid request method.'})

# Load the trained model
model = joblib.load(r'model\dibet\dib.pickle')

def read_sensor_data_val(request):
    if request.method == 'GET':
        # Serial port configuration
        ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with your serial port
        ser.flushInput()

        try:
            sensor_data_list = []
            while True:
                # Read a line from the serial port
                try:
                    line = ser.readline().decode('latin-1').strip()
                except UnicodeDecodeError as e:
                    print("Error decoding line:", e)
                    continue  # Skip processing this line
                
                sensor_data_list.append(float(line))  # Convert data to float
                
                # Limit the number of sensor data to be sent to the frontend for demonstration
                if len(sensor_data_list) >= 10:
                    break
            
            # Predict values based on sensor data
            predictions = model.predict(sensor_data_list)
            
            return render(request, 'sensor_data.html', {'sensor_data_list': sensor_data_list, 'predictions': predictions})
                    
        except KeyboardInterrupt:
            print("Interrupted. Exiting...")
        finally:
            ser.close()
    
    return render(request, 'sensor_data.html', {'error': 'Invalid request method.'})

from django.contrib.auth.decorators import login_required

@login_required
def predict_diabetesRN(request):
    if request.method == 'POST':
        form = DiabetesFormRN(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            blood_pressure_systolic = form.cleaned_data['blood_pressure_systolic']
            blood_pressure_diastolic = form.cleaned_data['blood_pressure_diastolic']
            urinary_ACR = form.cleaned_data['urinary_ACR']
            serum_creatinine = form.cleaned_data['serum_creatinine']
            GFR = form.cleaned_data['GFR']
            kidney_biopsy_results = form.cleaned_data['kidney_biopsy_results']
            visual_acuity = form.cleaned_data['visual_acuity']
            presence_of_microaneurysms = form.cleaned_data['presence_of_microaneurysms']
            presence_of_hemorrhages = form.cleaned_data['presence_of_hemorrhages']
            presence_of_exudates = form.cleaned_data['presence_of_exudates']
            neovascularization = form.cleaned_data['neovascularization']
            OCT_results = form.cleaned_data['OCT_results']
            fluorescein_angiography_results = form.cleaned_data['fluorescein_angiography_results']
            retinal_photography_results = form.cleaned_data['retinal_photography_results']

            # Your diabetes detection logic goes here
            # This is just a placeholder
            has_diabetes = False  # Placeholder for the detection logic
            if age > 30 and blood_pressure_systolic > 120 and blood_pressure_diastolic > 80:
                has_diabetes = True


                if age > 50 and age < 60 and blood_pressure_systolic > 120 and blood_pressure_diastolic > 80:
                    diabetes_stage = "DCBD vascular complications - Stage 4"
                    doctor_recommendation = "Consult Dr Venkatesh H : KLE : 9874563210"
                    foods_to_avoid = "Avoid sugary and processed foods. Such as Waffers, Fried"
                    foods_to_eat = "Include plenty of vegetables, fruits, whole grains, and lean proteins in your diet."
                    exercises = "Engage in regular physical activity like walking, swimming, or cycling. Aim for at least 30 minutes a day."
                elif age > 40 and age < 50 and blood_pressure_systolic > 120 and blood_pressure_diastolic > 80:
                    diabetes_stage = "DCBD type 2 diabetes - Stage 3"
                    doctor_recommendation = "Consult Dr Praveen M : Lakeview Hospital : 8542137692"
                    foods_to_avoid = "Avoid sugary and processed foods."
                    foods_to_eat = "Include plenty of vegetables, fruits, whole grains, and lean proteins in your diet."
                    exercises = "Engage in regular physical activity like walking, swimming, or cycling. Aim for at least 30 minutes a day."
                elif age > 30 and age < 40 and blood_pressure_systolic > 120 and blood_pressure_diastolic > 80:
                    diabetes_stage = "DCBD prediabetes - Stage 2 "
                    doctor_recommendation = "Consult Dr Rudrapa Shintri : Arihant Hospital: 9632587410"
                    foods_to_avoid = "Avoid sugary and processed foods."
                    foods_to_eat = "Include plenty of vegetables, fruits, whole grains, and lean proteins in your diet."
                    exercises = "Engage in regular physical activity like walking, swimming, or cycling. Aim for at least 30 minutes a day."
                elif age > 20 and age < 30 and blood_pressure_systolic > 120 and blood_pressure_diastolic > 80:
                    diabetes_stage = "DCBD insulin resistance - Stage 1"
                    doctor_recommendation = "Consult Dr Patil : Civil Hospital : 7539514268"
                    foods_to_avoid = "Avoid sugary and processed foods."
                    foods_to_eat = "Include plenty of vegetables, fruits, whole grains, and lean proteins in your diet."
                    exercises = "Engage in regular physical activity like walking, swimming, or cycling. Aim for at least 30 minutes a day."
                else:
                    diabetes_stage = "Your results show signs of Diabetes"
                    doctor_recommendation = "Consult Dr Shivraj : Venugram Hospital : 8520147963"
                    foods_to_avoid = "Avoid sugary and processed foods."
                    foods_to_eat = "Include plenty of vegetables, fruits, whole grains, and lean proteins in your diet."
                    exercises = "Engage in regular physical activity like walking, swimming, or cycling. Aim for at least 30 minutes a day."


                return render(request, 'diabetesRNresult.html', {
                    'has_diabetes': has_diabetes,
                    'doctor_recommendation': doctor_recommendation,
                    'foods_to_avoid': foods_to_avoid,
                    'foods_to_eat':foods_to_eat,
                    'exercises': exercises,
                    'diabetes_stage': diabetes_stage,
                    
                })
            else:
                # Render a template for non-diabetic users
                return render(request, 'diabetesRNresult.html', {'has_diabetes': has_diabetes})
    else:
        form = DiabetesFormRN()
    
    return render(request, 'diabetesRNform.html', {'form': form})
