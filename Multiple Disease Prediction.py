# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model
diabetes_model= pickle.load(open('C:/Users/Shveta/OneDrive/Desktop/Python/Disease Prediction/diabetes_model.sav','rb'))
breast_cancer_model= pickle.load(open('C:/Users/Shveta/OneDrive/Desktop/Python/Disease Prediction/breast_cancer_model.sav','rb'))

#sidebar to navigate

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Breast Cancer Prediction'],default_index=0)
    
# Diabetes page
if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction with ML')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    # Predicting the code
    diabetes_diagnosis = ''
    
    # Creating a button for the prediction
     
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis = 'You are Diabetic'
            
        else:
            diabetes_diagnosis = 'You are not Diabetic'
            
    st.success(diabetes_diagnosis)
    
    
# Breast Cancer page
if(selected == 'Breast Cancer Prediction'):
   st.title('Breast Cancer Prediction with ML')
        
# Getting the input data from the user
   col1, col2, col3, col4, col5 = st.columns(5)
 
 
   with col1:  
         meanradius = st.text_input('Mean Radius')
   with col2:
         meantexture = st.text_input('Mean Texture')
   with col3:
         meanperimeter = st.text_input('Mean Perimeter')
   with col4:
         meanarea = st.text_input('Mean Area')
   with col5:
         meansmoothness = st.text_input('Mean Smoothness')
   with col1:
         meancompactness = st.text_input('Mean Compactness')
   with col2:
         meanconcavity = st.text_input('Mean Concavity')
   with col3:
         meanconcavepoints = st.text_input('Mean Concave Points')
   with col4:
         meansymmetry  = st.text_input('Mean Symmetry')
   with col5:
         meanfractaldimension = st.text_input('Mean Fractal Dimension')
   with col1:
         radiuserror = st.text_input('Radius Error')
   with col2:
         textureerror = st.text_input('Texture Error')
   with col3:
         perimetererror = st.text_input(' perimeter error')
   with col4:
         areaerror = st.text_input('area error')
   with col5:
         smoothnesserror = st.text_input('smoothness error')
   with col1:
         compactnesserror = st.text_input('compactness error')
   with col2:
         concavityerror = st.text_input('concavity error')
   with col3:
         concavepointserror = st.text_input('concave points error')
   with col4:
         symmetryerror = st.text_input('symmetry error')
   with col5:
         fractaldimensionerror = st.text_input('fractal dimension error')
   with col1: 
         worstradius = st.text_input('worst radius')    
   with col2:
         worsttexture = st.text_input('worst texture')
   with col3:
         worstperimeter  = st.text_input('worst perimeter')
   with col4:
         worstarea = st.text_input('worst area')
   with col5:
         worstsmoothness = st.text_input('worst smoothness')
   with col1: 
         worstcompactness = st.text_input('worst compactness')
   with col2:
         worstconcavity = st.text_input('worst concavity')
   with col3:
         worstconcavepoints = st.text_input('worst concave points')
   with col4:
         worstsymmetry = st.text_input('worst symmetry')
   with col5:
         worstfractaldimension = st.text_input('worst fractal dimension')
        
        # Predicting the code
   breast_cancer_diagnosis = ''
   
   user_input = [meantexture, meanperimeter, meanarea, meansmoothness, meancompactness, meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror, textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror, concavityerror, concavepointserror, symmetryerror, fractaldimensionerror, worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness, worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]
   user_input = [float(x) for x in user_input]
   
     
        # Creating a button for the prediction
         
   if st.button('Breast Cancer Test Result'):
            breast_cancer_prediction = breast_cancer_model.predict([user_input])
            if(breast_cancer_prediction[0]==1):
                breast_cancer_diagnosis = 'You have a Breast Cancer'
                
            else:
                breast_cancer_prediction_diagnosis = 'You Donot have Breast Cancer'
                
   st.success(breast_cancer_diagnosis)
        