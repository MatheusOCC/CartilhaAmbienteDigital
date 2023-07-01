import streamlit as st
import base64


st.title('Materiais Recomendados')
st.caption('desenvolvido para a disciplina Computador, Ética e Sociedade (MATA82) da UFBA - Universidade Federal da Bahia, em 2023.1')
st.caption('Autores: Indaiara Bonfim; Jade do Nascimento; Marcos dos Anjos; Matheus Cerqueira; Rômulo Chamusca')


st.divider()


st.header("Cartilha Ambiente Digital")
# st.download_button('Baixar Cartilha', '')
# with st.expander('Clique para ler'):
#     with open('CartilhaCOMPUSOC.pdf',"rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#         pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
#         st.markdown(pdf_display, unsafe_allow_html=True)

st.header('Referências Utilizadas')
with st.expander('Referências Utilizadas'):
    st.write('https://fia.com.br/blog/cyberbullying/')
    st.write('https://brasilescola.uol.com.br/sociologia/cyberbullying.htm')
    st.write('https://olhardigital.com.br/2022/04/29/tira-duvidas/sinais-perfil-falso-redes-sociais/')


st.header('Indicações de Leitura')
with st.expander('Indicações de Leitura'):
    st.write('https://www.perallis.com/news (Empresa especializada em cibersegurança)')
    st.write('https://www.olharldigital.com/ (Empresa especializada em cibersegurança)')
    st.write('https://www.tecmundo.com.br/seguranca (Empresa especializada em tecnologia, com notícias de cibersegurança)')
    st.write('https://lupa.uol.com.br/ (Agência de notícias com foco em desinformação)')
with st.expander('Notícias Importantes'):
    st.write('https://canaltech.com.br/hacker/hackers-chineses-invadem-entidades-governamentais-pelo-mundo-brasil-na-lista-158443/')
    st.write('https://vejario.abril.com.br/coluna/fabio-barbirato/como-evitar-que-seu-filho-seja-vitima-de-crimes-na-internet/')
    st.write('https://www.adrenaline.com.br/seguranca/windows-11-coleta-e-envia-dados-de-usuarios-para-varias-empresas-denuncia-youtuber/')
    st.write('https://olhardigital.com.br/2019/08/09/dicas-e-tutoriais/como-dificultar-a-coleta-de-dados-no-computador-e-no-celular/')
    st.write('https://www.techtudo.com.br/noticias/2022/03/golpe-do-perfil-fake-em-relacoes-virtuais-atinge-1-a-cada-4-brasileiros.ghtml')
    st.write('https://www.bbc.com/portuguese/brasil-42172146')
    st.write('https://arquivo.canaltech.com.br/comportamento/pesquisa-da-intel-revela-dados-sobre-cyberbullying-no-brasil-46105/')
with st.expander('Explicando conceitos'):
    st.subheader('Software Livre vs proprietário')
    st.write('https://g1.globo.com/tecnologia/blog/tira-duvidas-de-tecnologia/post/software-livre-vale-pena-ser-substituido-por-programas-pagos.html')
    st.write('https://www.gnu.org/philosophy/free-sw.pt-br.html (Definição original de Software livre)')


st.header('Indicações de Vídeos')
with st.expander('indicações de Vídeos'):
    st.subheader('Como Fazer Compras Pela internet Com Segurança? (Canal: Canaltech)')
    st.video('https://www.youtube.com/watch?v=QqqJtr-7DUk', format="video/mp4", start_time=0)
    st.subheader(' Por onde vem a internet? Seguimos a fibra até sua casa! #Boravê 🔵Manual do Mundo (Canal: Manual do Mundo)')
    st.video('https://www.youtube.com/watch?v=fYJl-7jRzuw&pp=ygUYY29tbyBmdW5jaW9uYSBhIGludGVybmV0', format="video/mp4", start_time=0)
    st.subheader('Hackers contam como enganam vítimas no golpe do Pix; saiba como se proteger (Canal: BBC News Brasil)')
    st.video('https://www.youtube.com/watch?v=JEP9pmN2GEM', format="video/mp4", start_time=0)


st.header('Boas práticas')
with st.expander('Ferramentas Úteis'):
    st.write('https://www.haveibeenpwned.com/ (Site que verifica se algum endereço de e-mail ou senha seus já foi vazado)')
    st.write('https://tosdr.org/pt_BR/frontpage/ (Site comunitário que analisa os termos de serviços de sites e aplicativos no mundo)')
    st.write('https://www.boatos.org/ e https://www.e-farsas.com/ (Sites que checam a veracidade de boatos viralizados recentemente)')
    st.write('https://www.techtudo.com.br/dicas-e-tutoriais/2023/03/como-ativar-monitoramento-parental-nas-redes-sociais-e-proteger-seu-filho-edapps.ghtml (Site ensinando como ativar o monitoramento parental)')
    