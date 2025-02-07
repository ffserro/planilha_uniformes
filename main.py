import streamlit as st

st.title('Aquisição de uniformes')

with st.form('uniformes'):
  st.text_input('Digite o seu NIP:')
  
  
  st.form_submit_button('Enviar')
