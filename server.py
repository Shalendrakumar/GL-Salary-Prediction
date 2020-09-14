import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle
import util
import pickle
import json

st.markdown(f"<h1 style='text-align: center; color: green;'><u>GL Salary Prediction App</u></h1>This app will predicts the <b>Estimate Average Salary</b> of Employee! ", unsafe_allow_html=True)

#st.subheader("This app will predicts the **Estimate Average Salary** of Employee! ")
st.info('Please select the required details at Sidebar to check the *** Average Salary ***')

st.sidebar.header('User Input Features')

util.load_saved_artifacts()

hourly_status = st.radio("Hourly Salary:",('No','Yes'))
if hourly_status == 'Yes':
	hourly=1
else:
	hourly=0

rating = st.sidebar.slider('Rating:',1,5,3)
python_status = st.sidebar.radio('Python:',('No','Yes'))
if python_status == 'Yes':
	python_yn=1
else:
	python_yn=0
spark_status = st.sidebar.radio('Spark:',('No','Yes'))
if spark_status == 'Yes':
	spark=1
else:
	spark=0
aws_status = st.sidebar.radio('AWS:',('No','Yes'))
if aws_status == 'Yes':
	aws=1
else:
	aws=0


__job_simp=util.replace_designation_string()
designation_status = st.sidebar.selectbox('Designation',(__job_simp))
if designation_status is not None:
    job_simp="job_simp_"+designation_status.lower()

__seniority=util.replace_seniority_string()
seniority_status = st.sidebar.selectbox('Seniority',(__seniority))
if seniority_status is not None:
    seniority="seniority_"+seniority_status.lower()

    
__size=util.replace_size_string()
size_status = st.sidebar.selectbox('Size of Company',(__size))
if size_status is not None:
    size="size_"+size_status
    
__type_of_ownership=util.replace_too_string()   
type_ow_status = st.sidebar.selectbox('Type of Ownership',(__type_of_ownership))
if type_ow_status is not None:
    type_ow="type of ownership_"+type_ow_status.lower()

__sector=util.replace_sector_string()
sector_status = st.sidebar.selectbox('Sector',(__sector))
if sector_status == "none":
    sector = "sector_-1"
else:
    sector="sector_"+sector_status.lower()

__revenue=util.replace_revenue_string()
revenue_status = st.sidebar.selectbox('Revenue',(__revenue))
if revenue_status is not None:
    revenue="revenue_"+revenue_status

__job_state=util.replace_job_state_string()
job_state_status = st.sidebar.selectbox('Job State',(__job_state))
if job_state_status is not None:
    job_state="job_state_"+job_state_status.lower()

age = st.sidebar.text_input('Age of Company:',10)
age=int(age)
  
response = util.predict_salary(rating,hourly,age,python_yn,spark,aws,size,type_ow,sector,revenue,job_state,job_simp,seniority)

st.write('')
st.write("As per your selection you want salary on hourly basis :**",hourly_status,"** want to work in python : **"
,python_status,"**, Spark : **",spark_status,"**, AWS : **",aws_status,"** and on sector : **",sector_status
,"** designation as a **",designation_status,"** and on Label : **",seniority_status,"**position")

st.write("Company is **",age,"** years older and type of company ownership is **",type_ow_status,"** that has No of Emp : **"
,size_status,"** and Revenue : **",revenue_status,"** with company rating **",rating,"** & in Location : **",job_state_status,"**")

#st.write("Then **Average Salary will be ",response," Thousand( USD ) Yearly**")
st.markdown(f"<h2 style='color: blue;'>Average Salary <b>{response:.2f}</b> Thousand(USD) Yearly</h2>",unsafe_allow_html=True)
#st.markdown(f"The mean is **{response:.2f}** and there are **{response:,}**.")
st.write('')
st.write('')
st.write('')
st.write("*By-   Shalendra Kumar*")
img = Image.open("shalendra.png")
st.image(img,width=120,caption='Thanks !!')

