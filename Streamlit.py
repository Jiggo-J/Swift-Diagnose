

import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Cardiovascular Disease Prediction", page_icon=":heart:")

st.title('Swift-Diagnose for your cardio-vascular health', )

age = st.number_input('What is you age in year?', min_value=0)
st.write('Your age in years is ', age)
age_in_days = round(age * 365)

gender = st.selectbox(
    'What is your gender?',
    ('Male', 'Female'))
if gender == 'Male':
    gender = 1
else:
    gender = 2

height = st.number_input('What is your height in cm?')
st.write('Your height in is ', height)

weight =st.number_input('What is your weight in kg?')
st.write('Your weight in kg is ', weight)

ap_hi = st.number_input('What is upper blood pressure level?')
st.write('Your upper blood pressure level is ', ap_hi)

ap_lo = st.number_input('What is your lower blood pressure level?')
st.write('Your lower blood pressure level is ', ap_lo)

cholesterol = st.selectbox(
    'What is your cholestorel level?',
    ('1: normal', '2: above normal', '3: well above normal'))
if cholesterol == '1: normal':
    cholesterol = 1
elif cholesterol == '2: above normal':
    cholesterol = 2
else:
    cholesterol = 3

 
gluc = st.selectbox(
    'What is your glucose level?',
    ('1: normal', '2: above normal', '3: well above normal'))
if gluc == '1: normal':
    gluc = 1
elif gluc == '2: above normal':
    gluc = 2
else:
    gluc = 3


smoke = st.selectbox(
    'Do you smoke?',
    ('Yes', 'No'))
if smoke == 'Yes':
    smoke = 1
else:
    smoke = 0


alco = st.selectbox(
    'Do you drink?',
    ('Yes', 'No'))
if alco == 'Yes':
    alco = 1
else:
    alco = 0


active = st.selectbox(
    'Are you active?',
    ('Yes', 'No'))
if active == 'Yes':
    active = 1
else:
    active = 0

url = "https://7c7ryl5ir0.execute-api.us-east-1.amazonaws.com/prod/cardio-getter?"
params =  f"age={age_in_days}&gender={gender}&height={height}&weight={weight}&ap_hi={ap_hi}&ap_lo={ap_lo}&cholesterol={cholesterol}&gluc={gluc}&smoke={smoke}&alco={alco}&active={active}"


response = requests.get(url + params)
#st.write(response.json())

prediction = response.json()["prediction"]

if float(prediction) > 0.6:
    st.success(f'Based on the provided data, you have a {float(prediction)*100}% chance of having a cardiovascular disease. You should visit a doctor, do more sport, quit smoking and alcohol, and do regular check-ups.')
else:
    st.info(f'Based on the provided data, you have a {float(prediction)*100}% chance of having a cardiovascular disease. You are fine.')