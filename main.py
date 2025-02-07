import streamlit as st
import pandas as pd

trip = pd.read_csv('./tripulacao.csv', delimiter=';')
trip['NIP'] = trip.NIP.str.replace('.', '')

st.dataframe(trip)

st.title('Aquisição de uniformes')

if 'logged' not in st.session_state:
  st.session_state['nip'] = st.text_input('Digite o seu NIP:')
  st.session_state['nip'] = st.session_state['nip'].replace('.', '')
  if st.button('Enviar'):
    st.session_state['logged'] = True
    st.rerun()

else:
  mil = trip[trip.NIP==st.session_state['nip']]
  st.write(mil)
