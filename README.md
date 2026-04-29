# Heart Disease Risk Prediction System

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![ML](https://img.shields.io/badge/ML-K--Nearest%20Neighbors-orange.svg)

A professional-grade clinical diagnostic support tool that leverages Machine Learning to assess heart disease risk. Designed with a focus on clinical accuracy and user-friendly interaction, this system provides a reliable screening mechanism based on 11 key cardiovascular parameters.

## 📋 Project Overview

The **Heart Disease Risk Prediction System** is a data-driven application that utilizes the K-Nearest Neighbors (KNN) algorithm to analyze clinical data. It serves as a screening tool for medical professionals and researchers to identify potential cardiac risks early.

The application features a modern, professional dark-themed interface developed specifically for clinical environments, ensuring high readability and focus.

## ✨ Key Features

- **Precise Risk Assessment**: Utilizes a fine-tuned KNN model trained on comprehensive heart disease datasets.
- **Real-time Diagnostics**: Instant risk probability and screening results upon data entry.
- **Clinical UI/UX**: Professional, emoji-free dark theme designed for medical software environments.
- **Comprehensive Analysis**: Evaluates parameters including cholesterol levels, resting BP, ST depression (oldpeak), and chest pain types.
- **Interactive Visualizations**: Includes risk gauges and confidence metrics for better decision support.

## 🛠️ Technology Stack

- **Core Engine**: Python 3.x
- **Machine Learning**: Scikit-Learn (K-Nearest Neighbors)
- **Data Handling**: Pandas, NumPy
- **Interface**: Streamlit (Custom CSS styled)
- **Model Persistance**: Joblib

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ifrah27/Heart_Disease_Risk_Prediction_project.git
   cd Heart_Disease_Risk_Prediction_project
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit pandas joblib scikit-learn
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## 📊 Model Information

The system uses a **K-Nearest Neighbors (KNN)** classifier. The features are normalized using a `StandardScaler` to ensure optimal model performance. The categorical variables are one-hot encoded to match the diagnostic standards used during the training phase.

### Expected Input Parameters:
- **Demographics**: Age, Sex.
- **Vitals**: Resting Blood Pressure, Serum Cholesterol, Fasting Blood Sugar.
- **Cardiac Assessment**: Chest Pain Type (ASY, ATA, NAP, TA), Resting ECG, Max Heart Rate, Exercise Angina, ST Slope, and Oldpeak.

## ⚖️ Disclaimer

*This tool is intended for research and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions regarding a medical condition.*

---
Developed by [Ifrah](https://github.com/Ifrah27)
