import streamlit as st
import base64
import logging
import cartilhas
import extras

st.title('Cartilha: Segurança e Provacidade no Ambiente Digital')
st.caption('Desenvolvido para a disciplina Computador, Ética e Sociedade (MATA68) da UFBA - Universidade Federal da Bahia, em 2023.1')
st.caption('Autores: Indaiara Bonfim; Jade do Nascimento; Marcos dos Anjos; Matheus Cerqueira; Rômulo Chamusca')

def secao():
    col_1, col_2 = st.columns(2)
    with col_1:
        btn_cartilha = st.button("Ver Cartilha")
    with col_2:
        btn_material_complementar = st.button("Ver Material Complementar")
    secao = ('extra' if btn_material_complementar else 'cartilha')
    return secao


def cartilha():
    cartilhas.carrega_cartilha()
    return ''


def extra():
    extras.carrega_extras()
    return ''


def main():
    cartilha() if secao() == 'cartilha' else extra()
    return 


if __name__ == '__main__':
    main()