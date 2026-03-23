import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))
st.title("salary Prediction App")
exp=st.number_import("Enter Experience",min_value=0,max_value=50,value=1)
if st.button("Perdict"):
    result=model.predict([[exp]])
    st.write(f"Predicted salary : {int(result[0][0])}")