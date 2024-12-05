import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# โหลดโมเดลที่ฝึกเสร็จแล้ว
model = load_model('heart_disease .h5')  # ระบุที่อยู่ของไฟล์โมเดล

# สร้างฟังก์ชันสำหรับการทำนาย
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    # รับข้อมูลจากผู้ใช้ในรูปแบบ numpy array
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    # ทำนายผลลัพธ์จากโมเดล
    prediction = model.predict(input_data)
    return prediction[0][0]  # คืนค่าความน่าจะเป็น

# ส่วนติดต่อผู้ใช้ (UI)
st.title("Heart Disease Prediction Web App")
st.write("กรุณากรอกข้อมูลเพื่อทำนายความเสี่ยงโรคหัวใจ")

# รับข้อมูลจากผู้ใช้
age = st.number_input("Age", min_value=0, max_value=120, value=50)
sex = st.selectbox("Sex (0: Female, 1: Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=120)
chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)", [0, 1])
restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=0, max_value=220, value=150)
exang = st.selectbox("Exercise-Induced Angina (0: No, 1: Yes)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0)
slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (0-3)", [0, 1, 2, 3])

# คำนวณผลเมื่อกดปุ่ม
if st.button("Predict"):
    result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    if result > 0.5:
        st.write(f"ผลการทำนาย: คุณมีความเสี่ยงโรคหัวใจ (ความน่าจะเป็น: {result:.2f})")
    else:
        st.write(f"ผลการทำนาย: คุณไม่มีความเสี่ยงโรคหัวใจ (ความน่าจะเป็น: {result:.2f})")
