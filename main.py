import streamlit as st
import pandas as pd

trip = pd.read_csv('./tripulacao.csv', delimiter=';')
trip['NIP'] = trip.NIP.str.replace('.', '')

st.title('Aquisição de uniformes')

if 'logged' not in st.session_state:
  st.session_state['nip'] = st.text_input('Digite o seu NIP:')
  st.session_state['nip'] = st.session_state['nip'].replace('.', '')
  if st.button('Enviar'):
    st.session_state['logged'] = True
    st.rerun()

else:
  mil = trip[trip.NIP==st.session_state['nip']]
  st.markdown(f'<h2>Seja bem vindo, {mil.POSTO.iloc[0]} {mil.NOME.iloc[0]}.</h2>', unsafe_allow_html=True)
