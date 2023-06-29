import streamlit as st


st.title('Materiais Recomendados')
st.caption('desenvolvido para a disciplina Computador, Ética e Sociedade (MATA82) da UFBA - Universidade Federal da Bahia, em 2023.1')
st.caption('Autores: Indaiara Bonfim; Jade do Nascimento; Marcos dos Anjos; Matheus Cerqueira; Rômulo Chamusca')


st.divider()


st.header('Referências Utilizadas')
with st.expander('Referências Utilizadas'):
    st.write('')


st.header('Indicações de Leitura')
with st.expander('Indicações de Leitura'):
    st.write('https://www.perallis.com/news (Empresa especializada em cibersegurança)')
    st.write('https://www.olharldigital.com/ (Empresa especializada em cibersegurança)')
    st.write('https://www.tecmundo.com/ (Empresa especializada em cibersegurança)')

st.header('Indicações de Vídeos')
with st.expander('indicações de Vídeos'):
    st.subheader('Como Fazer Compras Pela internet Com Segurança? (Canal: Canaltech)')
    st.video('https://www.youtube.com/watch?v=QqqJtr-7DUk', format="video/mp4", start_time=0)


st.header('Boas práticas')
with st.expander('Ferramentas Úteis'):
    st.write('https://www.haveibeenpwned.com/ (Site que verifica se algum endereço de e-mail ou senha seus já foi vazado)')
    st.write('https://tosdr.org/pt_BR/frontpage/ (Site comunitário que analisa os termos de serviços de sites e aplicativos no mundo)')
    