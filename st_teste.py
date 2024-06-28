oimport streamlit as st
import requests

st.title('Consulta CEP')
st.markdown('Feito no SENAC com 💗')

cep = st.text_input(
    label='Digite um cep', 
    placeholder='Somente números'
    )

try:
    endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco = endereco.json()
    st.write(
        endereco['logradouro'], 
        '-', 
        endereco['bairro'], 
        '-', 
        endereco['localidade'],
        '/',
        endereco['uf']
        )
except:
    st.error('CEP Incorreto/Inexistente', icon='🚨')
