from json import load
import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.write("""
    # Penguin prediction app
    This app predicts the **Palmer penguins** species
    Data obtained from the [palmerpenguins library] by Allison Horst
""")

st.sidebar.header('User Input Features')
st.sidebar.markdown("""
    [Example CSV input]
""")

upload_file = st.sidebar.file_uploader('Upload your CSV file', type=['csv'])
if upload_file:
    input_df = pd.read_csv(upload_file)
else:
    def user_input_features():
        island = st.sidebar.selectbox(
            'Island', ['Biscoe', 'Dream', 'Torgersen'])
        sex = st.sidebar.selectbox('Sex', ['male', 'female'])
        bill_length_mm = st.sidebar.slider(
            'Bill length (mm)', 32.1, 59.6, 43.6)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.sidebar.slider(
            'Flipper length (mm)', 172.0, 231.0, 201.0)
        body_mass_g = st.sidebar.slider(
            'Body mass (g)', 2700.0, 6300.0, 4207.0)
        data = {
            'island': island,
            'sex': sex,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g
        }
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

penguins_raw = pd.read_csv(
    '/media/nagachi/Nagachi/Datasets/data-master/penguins_cleaned.csv')
penguins = penguins_raw.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1]  # Only for first row (One predictions)

st.subheader('User Input Features')

if upload_file:
    st.write(df)
else:
    st.write('Awaiting CSV file to be uploaded')
    st.write(df)

load_clf = pickle.load(
    open('/Basic-project/DataScienceApp/penguins_clf.pkl', 'rb'))

prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)

st.subheader('Predictions')
penguin_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])
st.write(penguin_species[prediction])

st.subheader('Prediction probability')
st.write(prediction_proba)
