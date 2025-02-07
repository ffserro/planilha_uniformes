import streamlit as st
import pandas as pd

trip = pd.read_csv('./tripulacao.csv', delimiter=';')

st.title('Aquisição de uniformes')

if 'logged' not in st.session_state:
  st.session_state['nip'] = st.text_input('Digite o seu NIP:')
  if st.button('Enviar'):
    st.session_state['logged'] = True
    st.rerun()

else:
  st.write(st.session_state['nip'])
