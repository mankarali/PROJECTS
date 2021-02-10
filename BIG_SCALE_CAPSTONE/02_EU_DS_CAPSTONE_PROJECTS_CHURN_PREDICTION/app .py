# streamlit run app.py

import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# st.title('Employee Churn Prediction')
# st.markdown("<h1 style='text-align: center; color: black;'>Employee Churn Prediction</h1>", unsafe_allow_html=True)
im = Image.open("image.png")
st.image(im, width=700)

# html_temp = """
# <div style="width:700px;background-color:maroon;padding:10px">
# <h1 style="color:white;text-align:center;">Churn Prediction ML App. (Demo)</h1>
# </div>"""
# st.markdown(html_temp,unsafe_allow_html=True)


# @st.cache
# bir buyuk bir datatyi read_csv ile tekrar tekrar okutmamak icin hafuzada tutmasi icin st.cache kullanilir.
xgb_model = pickle.load(open("XGBoost.pkl","rb"))
rfr_model = pickle.load(open("RandomForest.pkl","rb"))

# Features: ['satisfaction_level', 'last_evaluation', 'number_project',
#        'average_montly_hours', 'time_spend_company', 'Work_accident', 'left',
#        'promotion_last_5years', 'Departments', 'salary']


departments = ['sales','technical','support','IT','product_mng','marketing','RandD','accounting','hr','management']
salary_level = ['low', 'medium','high']
work_accidents = ['Yes','No']
promotions= ['Yes','No']
# satisfaction_level: 0.0-1.0
# last_evaluation: 0.0-1.0
# number_project:2-7
# average_montly_hours:96-310
# time_spend_company:2-10


st.sidebar.header("Configure the Employee Features:")
department = st.sidebar.selectbox("What is the department of the employee?", (departments))
salary = st.sidebar.selectbox("What is the salary of the employee?",(salary_level))
work_accident = st.sidebar.selectbox("Has the employee ever had a work accident?",(work_accidents))
promotion = st.sidebar.selectbox("Has the employee been promoted in the last five years?",(promotions))

satisfaction = st.sidebar.slider("What is the percentage of the satisfaction level?",0,100,50,1)
evaluation = st.sidebar.slider("What is the percentage of the employer's last evaluation level?",0,100,50, step=1)
project_count= st.sidebar.slider("How many projects does the employee work on?",2,7,3, step=1)
montly_hours= st.sidebar.slider("What is the employee's monthly working hours?",96,310,200, step=1)
spend_time= st.sidebar.slider("How many years has the employee been with the company?",2,10,3, step=1)

department_encode={  'sales':7, 
                     'technical':9, 
                     'support':8, 
                     'IT':0, 
                     'product_mng':6, 
                     'marketing':5,
                     'RandD':1, 
                     'accounting':2, 
                     'hr':3, 
                     'management':4}

salary_encode = {'low':1,
                 'medium':2,
                 'high':3}

yes_no_encode = {'Yes':1, 'No':0}

my_dict = {'satisfaction_level':satisfaction/100, 
           'last_evaluation':evaluation/100, 
           'number_project':project_count,
           'average_montly_hours':montly_hours, 
           'time_spend_company':spend_time, 
           'Work_accident':yes_no_encode[work_accident],
           'promotion_last_5years':yes_no_encode[promotion], 
           'Departments':department_encode[department], 
           'salary':salary_encode[salary],
            }

df = pd.DataFrame.from_dict([my_dict])
st.write('')
st.dataframe(data=df, width=700, height=400)
st.write('')

st.subheader("Choose an ML Model:")
model = st.radio('',['XGBoost Classifier', 
                     'Random Forest Classifier'])

# Button
if st.button("Submit"):
    import time
    with st.spinner("ML Model is loading..."):
        my_bar=st.progress(0)
        for p in range(0,101,10):
            my_bar.progress(p)
            time.sleep(0.1)

        if model=='Random Forest Classifier':
            churn_probability = rfr_model.predict_proba(df)
            is_churn= rfr_model.predict(df)
        elif model=='XGBoost Classifier':
            churn_probability= xgb_model.predict_proba(df)
            is_churn= xgb_model.predict(df)
    
        st.success(f'The Probability of the Employee Churn is %{round(churn_probability[0][1]*100,1)}')
        
        if is_churn[0]:
            st.warning("The Employee is CHURN")
        else:
            st.success("The Employee is NOT CHURN")