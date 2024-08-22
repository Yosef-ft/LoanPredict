import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

model = joblib.load('saved_pipeline.pkl')

st.title("Apply for loans")
st.markdown("Insert the necessary information to successfully get the financial aid you need.")


age = st.number_input('Enter age', step=1, min_value=18 )
Income = st.number_input('Enter your income:', step=1, min_value=1 )
LoanAmount = st.number_input('Enter the loan amount:', step=1 )
MonthsInBusiness = st.number_input('Months in business: ', step=1)
NumCreditLines = st.number_input('Number of opened credit lines:', step=1 )
LoanTerm = st.number_input('Loan term in months: ', step=1)
Education = st.selectbox('Highest education level achieved: ', ['High School', 'Bachelor\'s', 'Master\'s', 'PhD'])
bussinesType = st.selectbox('How do you discribe your business or how often you work: ', ['Full-time', 'Part-time', 'Self-employed', 'Unemployed'])
MaritalStatus = st.selectbox('Are you married:', ['Married', 'Divorced','Single'])
HasMortgage = st.selectbox('Do you have mortgate:', ['Yes', 'No'])
HasDependents = st.selectbox('Do you have dependants', ['Yes', 'No'])
LoanPurpose = st.selectbox('What is the purpose of the loan', ['Business', 'Home','Auto', 'Education', 'Other'])
HasCoSigner = st.selectbox('Does the loan have a co-signer', ['Yes', 'No'])
InterestRate = 12
st.text(f'Interest rate is {InterestRate} %')

result_placeholder = st.empty()

def predict():
    columns = ['Age', 'Income', 'LoanAmount', 'MonthsEmployed', 'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 'Education', 'EmploymentType', 'MaritalStatus', 'HasMortgage', 'HasDependents', 'LoanPurpose', 'HasCoSigner']
    rows = np.array([age, Income, LoanAmount, MonthsInBusiness, NumCreditLines, InterestRate, LoanTerm, (LoanAmount / Income), Education, bussinesType, MaritalStatus, HasMortgage, HasDependents, LoanPurpose, HasCoSigner])
    data = pd.Series(rows, index= columns)

    predicted = model.predict(pd.DataFrame(data).transpose())

    if predicted == 0:
        result_placeholder.success('You are eligible for a loan we will contact you soon :thumbsup:')
    else:
        result_placeholder.error('You are not eligible for a loan :thumbsdown:')

    time.sleep(30)  # Adjust the sleep duration as needed
    result_placeholder.empty()        


st.button("Check Eligibility for Loan", on_click=predict)

