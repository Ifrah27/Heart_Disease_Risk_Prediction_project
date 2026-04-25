import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease Clinical Assessment",
    layout="wide"
)

# Custom CSS for a professional human-developed dark theme
st.markdown("""
<style>
    /* Use a standard professional font stack */
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap');

    /* Background and global text color */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Professional header area */
    .header-container {
        padding: 2rem 0;
        border-bottom: 1px solid #333;
        margin-bottom: 2rem;
    }

    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }

    .sub-title {
        font-size: 1rem;
        color: #888888;
    }

    /* Section styling */
    .section-container {
        background-color: #1e1e1e;
        border: 1px solid #2d2d2d;
        border-radius: 4px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #bb86fc;
        margin-bottom: 1.2rem;
        text-transform: uppercase;
        letter-spacing: 0.05rem;
    }

    /* Button styling - professional solid color */
    .stButton > button {
        background-color: #6200ee !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: background-color 0.2s;
    }

    .stButton > button:hover {
        background-color: #3700b3 !important;
    }

    /* Custom result displays */
    .result-container {
        padding: 1.5rem;
        border-radius: 4px;
        margin-top: 1rem;
    }

    .result-positive {
        background-color: rgba(207, 102, 121, 0.1);
        border: 1px solid #cf6679;
        color: #cf6679;
    }

    .result-negative {
        background-color: rgba(3, 218, 198, 0.1);
        border: 1px solid #03dac6;
        color: #03dac6;
    }

    /* Clean progress bar */
    .stProgress > div > div > div > div {
        background-color: #6200ee !important;
    }

    /* Label tweaks */
    label {
        font-weight: 500 !important;
        color: #b0b0b0 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #555;
        font-size: 0.8rem;
        border-top: 1px solid #222;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Load model assets
@st.cache_resource
def load_model():
    try:
        model = joblib.load('KNN_heart.pkl')
        scaler = joblib.load('scaler.pkl')
        expected_columns = joblib.load('columns.pkl')
        return model, scaler, expected_columns
    except:
        return None, None, None

model, scaler, expected_columns = load_model()

# Header Section
st.markdown("""
<div class="header-container">
    <div class="main-title">Heart Disease Risk Assessment</div>
    <div class="sub-title">Clinical diagnostic tool based on K-Nearest Neighbors analysis</div>
</div>
""", unsafe_allow_html=True)

if model is None:
    st.error("Error: Model assets not found. Please ensure KNN_heart.pkl, scaler.pkl, and columns.pkl are in the project directory.")
else:
    # Layout with three main columns for the form
    with st.container():
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Patient Demographics and Vitals</div>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.number_input("Age", 18, 100, 45)
            sex = st.selectbox("Sex", ["Male", "Female"])
        
        with col2:
            resting_bp = st.number_input("Resting Blood Pressure (mmHg)", 80, 200, 120)
            cholesterol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
            
        with col3:
            fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
            max_heart_rate = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
        st.markdown('</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="section-container">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Cardiac Diagnostic Indicators</div>', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            chest_pain_type = st.selectbox(
                "Chest Pain Type", 
                ["ASY", "ATA", "NAP", "TA"],
                help="ASY: Asymptomatic, ATA: Atypical Angina, NAP: Non-Anginal Pain, TA: Typical Angina"
            )
            rest_ecg = st.selectbox("Resting Electrocardiogram", ["Normal", "ST", "LVH"])
            
        with col2:
            exercise_induced_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
            steep_slope = st.selectbox("Peak Exercise ST Segment Slope", ["Up", "Flat", "Down"])
        
        oldpeak = st.slider("ST depression induced by exercise (Oldpeak)", 0.0, 6.0, 1.0, 0.1)
        st.markdown('</div>', unsafe_allow_html=True)

    # Prediction Action Area
    col_pred, col_res = st.columns([1, 2])
    
    with col_pred:
        predict_btn = st.button("Generate Assessment")
    
    if predict_btn:
        # Preprocessing matching training data
        input_data = {
            "Age": age,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": 1 if fasting_blood_sugar == "Yes" else 0,
            "MaxHR": max_heart_rate,
            "Oldpeak": oldpeak,
            "Sex_M": 1 if sex == "Male" else 0,
            "ChestPainType_ATA": 1 if chest_pain_type == "ATA" else 0,
            "ChestPainType_NAP": 1 if chest_pain_type == "NAP" else 0,
            "ChestPainType_TA": 1 if chest_pain_type == "TA" else 0,
            "RestingECG_Normal": 1 if rest_ecg == "Normal" else 0,
            "RestingECG_ST": 1 if rest_ecg == "ST" else 0,
            "ExerciseAngina_Y": 1 if exercise_induced_angina == "Yes" else 0,
            "ST_Slope_Flat": 1 if steep_slope == "Flat" else 0,
            "ST_Slope_Up": 1 if steep_slope == "Up" else 0,
        }

        input_df = pd.DataFrame([input_data])
        input_df = input_df[expected_columns]
        input_df_scaled = scaler.transform(input_df)

        prediction = model.predict(input_df_scaled)[0]
        probability = model.predict_proba(input_df_scaled)[0][1]

        with col_res:
            if prediction == 1:
                st.markdown(f"""
                <div class="result-container result-positive">
                    <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.5rem;">Positive Screening - High Risk</div>
                    <div>Analysis suggests a high risk of heart disease. Clinical consultation is recommended.</div>
                    <div style="margin-top: 1rem; font-size: 0.9rem;">Model Confidence: {probability:.1%}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-container result-negative">
                    <div style="font-weight: 700; font-size: 1.2rem; margin-bottom: 0.5rem;">Negative Screening - Low Risk</div>
                    <div>Analysis suggests a low risk of heart disease based on provided clinical data.</div>
                    <div style="margin-top: 1rem; font-size: 0.9rem;">Model Confidence: {1-probability:.1%}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.progress(probability)

# Footer
st.markdown("""
<div class="footer">
    Clinical Data Analysis Tool | Heart Disease Prediction Project | Developed for Medical Information Support
    <br>Disclaimer: This tool is for research purposes only and does not constitute medical advice.
</div>
""", unsafe_allow_html=True)
