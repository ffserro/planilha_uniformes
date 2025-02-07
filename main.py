import streamlit as st
import pandas as pd

trip = pd.read_csv('./tripulacao.csv', delimiter=';')

st.dataframe(trip)

st.title('Aquisição de uniformes')

with st.form('uniformes'):
  st.text_input('Digite o seu NIP:')
  
  
  st.form_submit_button('Enviar')
