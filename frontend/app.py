import streamlit as st
import requests

# Give the Name of the Application
st.title('Telco Customer Churn')

# Create Submit Form
with st.form(key='form_parameters'):
    gender = st.selectbox(label='gender', options=['Male', 'Female'], key=0)
    SeniorCitizen = st.number_input(label='SeniorCitizen', min_value=0, max_value=1, value=0, step=1)
    Partner = st.selectbox(label='Partner', options=['No', 'Yes'], key=1)
    Dependents = st.selectbox(label='Dependents', options=['No', 'Yes'])
    tenure = st.number_input(label='tenure', min_value=0, max_value=72, value=12, step=1)
    PhoneService = st.selectbox(label='PhoneService', options=['No', 'Yes'])
    MultipleLines = st.selectbox(label='MultipleLines', options=['No', 'Yes', 'No phone service'])
    InternetService = st.selectbox(label='InternetService', options=['Fiber optic', 'DSL', 'No'])
    OnlineSecurity = st.selectbox(label='OnlineSecurity', options=['No', 'Yes', 'No internet service'])
    OnlineBackup = st.selectbox(label='OnlineBackup', options=['No', 'Yes', 'No internet service'])
    DeviceProtection = st.selectbox(label='DeviceProtection', options=['No', 'Yes', 'No internet service'])
    TechSupport = st.selectbox(label='TechSupport', options=['No', 'Yes', 'No internet service'])
    StreamingTV = st.selectbox(label='StreamingTV', options=['No', 'Yes', 'No internet service'])
    StreamingMovies = st.selectbox(label='StreamingMovies', options=['No', 'Yes', 'No internet service'])
    Contract = st.selectbox(label='Contract', options=['Month-to-month', 'Two year', 'One year'])
    PaperlessBilling = st.selectbox(label='PaperlessBilling', options=['No', 'Yes'])
    PaymentMethod = st.selectbox(label='PaymentMethod', options=['Electronic check', 'Mailed check', 'Bank transfer (automatic)','Credit card (automatic)'])
    MonthlyCharges = st.slider(label='MonthlyCharges', min_value=18.250, max_value=118.750, value=20.000, step=1.000)
    TotalCharges = st.slider(label='TotalCharges', min_value=18.850, max_value=8684.800, value=1000.000, step=1.000)

    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'http://deploy-p2m1-ropiudin16.koyeb.app/predict'
    param = {'gender':gender,
      'SeniorCitizen':SeniorCitizen, 
      'Partner':Partner, 
      'Dependents':Dependents,
      'tenure'  :tenure,
      'PhoneService' :PhoneService,
      'MultipleLines' :MultipleLines,
      'InternetService' :InternetService,
      'OnlineSecurity' :OnlineSecurity,
      'OnlineBackup' :OnlineBackup,
      'DeviceProtection' :DeviceProtection,
      'TechSupport' :TechSupport,
      'StreamingTV' :StreamingTV,
      'StreamingMovies' :StreamingMovies,
      'Contract' :Contract,
      'PaperlessBilling' :PaperlessBilling,
      'PaymentMethod' :PaymentMethod,
      'MonthlyCharges' :MonthlyCharges,
      'TotalCharges' :TotalCharges}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)