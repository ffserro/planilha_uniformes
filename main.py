import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.session_state.conn = st.connection('gsheets', type=GSheetsConnection)

trip = pd.read_csv('./tripulacao.csv', delimiter=';')
trip['NIP'] = trip.NIP.str.replace('.', '')

st.title('AQUISIÇÃO DE UNIFORMES')

if 'logged' not in st.session_state:
  st.session_state['nip'] = st.text_input('Digite o seu NIP:')
  st.session_state['nip'] = st.session_state['nip'].replace('.', '')
  if st.button('Enviar'):
    st.session_state['logged'] = True
    st.session_state['inicio'] = False
    st.rerun()

else:
  mil = trip[trip.NIP==st.session_state['nip']]
  if len(mil) != 0 and not st.session_state['inicio']:
    st.markdown(f'<h2>Seja bem vindo, {mil.POSTO.iloc[0]} {mil.NOME.iloc[0]}.</h2>', unsafe_allow_html=True)
    st.write('A fim de realizar um levantamento da necessidade de aquisição de uniformes OP3 e novos bonés de viagem, concita-se a todos que preencham o formulário a seguir.')
    st.write('A indenização destes uniformes será realizada através de desconto em BP ou pagamento de GRU para Oficiais, suboficiais e sargentos; e através de CREDIFARDA para cabos e marinheiros.')
    st.session_state['inicio'] = st.button('Preencher formulário')
  elif st.session_state['inicio']:
    st.session_state['fim'] = False
    if not st.session_state.fim:
      with st.form('formulario'):
        tam_op3 = st.selectbox('Tamanho do Macacão Operativo OP3', ['-', 'P', 'M', 'G', 'GG', 'XG'])
        qtd_op3 = st.number_input('Quantidade de Macacões Operativos', step=1, format='%d')
        qtd_bon = st.number_input('Quantidade de Bonés de Viagem (Novo modelo)', step=1, format='%d')
        if st.form_submit_button('Enviar'):
          tabela = st.session_state.conn.read(worksheet='PLANILHA')
          tabela.iloc[len(tabela)] = [st.session_state.nip, mil.NOME.iloc[0], tam_op3, qtd_op3, mil.CIRCULO.iloc[0], qtd_bon]
          #data = pd.DataFrame({'NIP':[st.session_state.nip], 'NOME':[mil.NOME.iloc[0]], 'TAM_OP3':[tam_op3], 'QTD_OP3':[qtd_op3], 'CIRCULO':[mil.CIRCULO.iloc[0]], 'QTD_BON':[qtd_bon]})
          #tabela = pd.concat([tabela, data]).drop_duplicates(keep='last')
          st.session_state.conn.update(worksheet='PLANILHA', data=tabela)
          st.session_state['fim'] = True
          st.success('Os dados foram enviados com sucesso!')
    else:
      st.header('Muito obrigado pela participação!')
  else:
    st.markdown('<h2>Este NIP não pertence a nossa Organização Militar, mas agradecemos pelo interesse.</h2>', unsafe_allow_html=True)

