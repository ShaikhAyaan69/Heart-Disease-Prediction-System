import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Prediction','About Us'],
        icons=['house','book','envelope','list'],
        styles={
            "container":{"background-color":"#EC7063"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#CB4335",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#F8F521"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:red;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE HEART DISEASE PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    file_=open("heart.gif","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="Heart gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
    . paragraph {
        font-size:20px !important;
        text-align: justify;
        }
    </style>
        """, unsafe_allow_html=True)

    st.markdown(' <p class="paragraph"> Heart Disease is one of the leading causes of death in the world, in fact in the India this disease is there leading cause of death their heart failure is commonly known as (CAD) or coronary artery disease. The term "heart disease" refers to several type of heart condition, a type of disease that affects the heart or blood vessels. There are several factors that might increase your chance of having this disease is by smoking, high blood pressure, high cholesterol, unhealthy diet, lack of exercise and obesity but you can reduce this risk through lifestyle change and in some cases medicine. </p>',
    unsafe_allow_html=True)

    if st.checkbox("Systolic Blood Pressure"):
        st.markdown("""
        <style>
        .systolic {
            font-size:17px !important;
            text-align:justify;
            }
        </style>
            """,unsafe_allow_html=True)
        st.markdown('<p class="systolic">Blood pressure is measured using two numbers: The first number, called systolic blood pressure, it measures the pressure in your arteries when your heart beats. This indicates how much pressure your blood is exerting against your artery walls when the heart beats.</p>',unsafe_allow_html=True)

    if st.checkbox("Diastolic Blood Pressure"):
        st.markdown("""
        <style>
        .systolic1{
            font-size:17px !important;
            text-align:justify;
        }
        </style>
        """,unsafe_allow_html=True)
        st.markdown('<p class="systolic1"> The second number, called diastolic blood pressure, it measures the pressure in your arteries when your heart rests between beats! This indicates how much pressure your blood is exerting against your artery walls while the heart is resting between beats.</p>',unsafe_allow_html=True)

if selected=='Prediction':
    image=Image.open('icon.png')
    
    st.image(image,width=200,use_column_width=True)

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('heart_disease.sav','rb'))

    def heart_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'This Person is Healthy Dont have Heart Disease'
        else:
            return 'This Person has heart disease'
    def main(): 

    # giving title 
        #st.title('HEART DISEASE PREDICTION SYSTEM')
        st.markdown("<h1 style='text-align: center; color: black;'>HEART DISEASE PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,col3,col4=st.columns(4)


        with co1:
            age= st.number_input('Enter the age',min_value=0)
            sex=st.selectbox('Enter Your Gender as Male:0 Female:1',(0,1),index=0)
            cp=st.selectbox('Enter the Chest Pain  0: asymptomatic,1: atypical angina,2: non-anginal pain,3: typical angina',(0,1,2,3))

        with col2:
            trestbps=st.number_input('Blood Pressure in mm of Hg',min_value=0)
            chol=st.number_input('Enter Cholesterol Level in mg/dl',min_value=0)
            fbs=st.selectbox('Enter Fasting Blood Sugar Level True:1, False:0',(0,1))

        with col3:
            restecg=st.selectbox("Enter Electrocardiographic results 0: 'Probable', 1: 'Normal' ,2:'ST-wave abnormality'",(0,1,2))
            thalach=st.number_input('Enter Maxixmum Heart Rate Achived',min_value=0)
            exang=st.selectbox('Enter Exercise include angina Yes:1 , No:0 ',(0,1),index=0)

        with col4:
            oldpeak=st.number_input('Enter ST depression induced by exercise relative to rest',min_value=0.0,format="%.2f")
            slope=st.selectbox("Enter Slope of ST Segment 0:'Downsloping', 1:'Flat', 2:'upsloping'",(0,1,2),index=0)
            ca=st.selectbox('Enter the number of major vessels 0 – 3',(0,1,2,3),index=0)
            thal=st.selectbox("Enter blood disorder called thalassemia Value 0:'Null', 1:'Fixed', 2:'Normal', 3:'Reversible'",(0,1,2,3),index=0)

        
    
        #code for the prediction 
    
        diagnosis=''
    
    
        #creating a button for prediction 
        if st.button('Heart Disease Prediction Test Result'):
            diagnosis = heart_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()

if selected == "About Us":
    st.markdown("""
    <style>
    .big-font1 {
        font-size:30px !important;
        color: red;
        text-align:center;
        font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font2 {
        font-size:20px !important;
        color: black;
        text-align:center;
        font-weight:bold;
        }
    </style>
    """, unsafe_allow_html=True)

    

    st.markdown('<p class="big-font1"> Group 16',unsafe_allow_html=True)

    st.markdown('<p class="big-font2"> Khan Moin Hayat B180844232 ',unsafe_allow_html=True)

    st.markdown('<p class="big-font2"> Shaikh Ayaan Shakil B190844237 ',unsafe_allow_html=True)

    st.markdown('<p class="big-font2"> Kanade Samruddhi B190844230 ',unsafe_allow_html=True)










