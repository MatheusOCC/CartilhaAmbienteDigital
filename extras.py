
import streamlit as st


def carrega_extras():
        
    st.divider()

    st.title('Materiais Recomendados')


    st.header('Referências Utilizadas')
    with st.expander('Referências Utilizadas'):
        st.write('https://fia.com.br/blog/cyberbullying/')
        st.write('https://brasilescola.uol.com.br/sociologia/cyberbullying.htm')
        st.write('https://olhardigital.com.br/2022/04/29/tira-duvidas/sinais-perfil-falso-redes-sociais/')
        st.write('https://www.kaspersky.com.br/resource-center/preemptive-safety/cyberbullying-and-cybercrime/')
        


    st.header('Indicações de Leitura')
    with st.expander('Indicações de Leitura'):
        st.write('https://www.perallis.com/news (Empresa especializada em cibersegurança)')
        st.write('https://www.olharldigital.com/ (Empresa especializada em cibersegurança)')
        st.write('https://www.tecmundo.com.br/seguranca (Empresa especializada em tecnologia, com notícias de cibersegurança)')
        st.write('https://lupa.uol.com.br/ (Agência de notícias com foco em desinformação)')
        st.write('https://www.unicef.org/brazil/cyberbullying-o-que-eh-e-como-para-lo (Como parar com o Bullying)')
        st.write('https://help.twitter.com/pt/safety-and-security/report-abusive-behavior#:~:text=Pressione%20e%20mantenha%20pressionada%20a,e%20selecione%20Denunciar%20%40username).&text=Caso%20voc%C3%AA%20selecione%20%C3%89%20abusivo,o%20problema%20que%20est%C3%A1%20denunciando (Como denunciar abuso no Twitter)')

    with st.expander('Notícias Importantes'):
        st.write('https://canaltech.com.br/hacker/hackers-chineses-invadem-entidades-governamentais-pelo-mundo-brasil-na-lista-158443/')
        st.write('https://vejario.abril.com.br/coluna/fabio-barbirato/como-evitar-que-seu-filho-seja-vitima-de-crimes-na-internet/')
        st.write('https://www.adrenaline.com.br/seguranca/windows-11-coleta-e-envia-dados-de-usuarios-para-varias-empresas-denuncia-youtuber/')
        st.write('https://olhardigital.com.br/2019/08/09/dicas-e-tutoriais/como-dificultar-a-coleta-de-dados-no-computador-e-no-celular/')
        st.write('https://www.techtudo.com.br/noticias/2022/03/golpe-do-perfil-fake-em-relacoes-virtuais-atinge-1-a-cada-4-brasileiros.ghtml')
        st.write('https://www.bbc.com/portuguese/brasil-42172146')
        st.write('https://arquivo.canaltech.com.br/comportamento/pesquisa-da-intel-revela-dados-sobre-cyberbullying-no-brasil-46105/')
        st.write('https://www.uol.com.br/splash/noticias/2022/10/11/o-caso-real-de-linchamento-que-inspirou-gloria-perez-em-travessia.html')
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
        
    st.header('Lista de Delegacias de cibercrimes')
    with st.expander('Delegacias do Brasil'):
        st.write('https://new.safernet.org.br/content/delegacias-cibercrimes (Lista de todas as delegacias do Brasil)') 