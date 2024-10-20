import pandas as pd
import numpy as np

# Function to generate random binary values (yes/no)
def random_binary():
    return np.random.choice(['yes', 'no'])

# Generate Diabetic Retinopathy Detection Dataset
retinopathy_data = {
    'Patient ID': range(1, 1001),
    'Age': np.random.randint(20, 80, size=1000),
    'Gender': np.random.choice(['male', 'female'], size=1000),
    'Duration of Diabetes': np.random.randint(1, 30, size=1000),
    'Visual Acuity (VA)': np.random.uniform(0.1, 1.0, size=1000),
    'Presence of Microaneurysms': [random_binary() for _ in range(1000)],
    'Presence of Hemorrhages': [random_binary() for _ in range(1000)],
    'Presence of Exudates': [random_binary() for _ in range(1000)],
    'Neovascularization': [random_binary() for _ in range(1000)],
    'OCT Results': np.random.uniform(200, 500, size=1000),
    'Fluorescein Angiography Results': np.random.uniform(0, 10, size=1000),
    'Retinal Photography Results': np.random.uniform(0, 5, size=1000)
}

retinopathy_df = pd.DataFrame(retinopathy_data)

# Generate Diabetic Nephropathy Detection Dataset
nephropathy_data = {
    'Patient ID': range(1, 1001),
    'Age': np.random.randint(20, 80, size=1000),
    'Gender': np.random.choice(['male', 'female'], size=1000),
    'Duration of Diabetes': np.random.randint(1, 30, size=1000),
    'Blood Pressure (Systolic)': np.random.randint(90, 180, size=1000),
    'Blood Pressure (Diastolic)': np.random.randint(60, 110, size=1000),
    'Urinary Albumin-to-Creatinine Ratio (ACR)': np.random.uniform(0, 100, size=1000),
    'Serum Creatinine Level': np.random.uniform(0.5, 2.0, size=1000),
    'Glomerular Filtration Rate (GFR)': np.random.uniform(30, 150, size=1000),
    'Kidney Biopsy Results': [random_binary() for _ in range(1000)]
}

nephropathy_df = pd.DataFrame(nephropathy_data)

# Saving datasets to CSV files
retinopathy_df.to_csv('diabetic_retinopathy_dataset_1000.csv', index=False)
nephropathy_df.to_csv('diabetic_nephropathy_dataset_1000.csv', index=False)
