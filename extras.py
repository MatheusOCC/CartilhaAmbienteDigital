
import streamlit as st


def carrega_extras():
        
    st.divider()

    st.title('Materiais Recomendados')

    st.header('Indicações de Leitura')
    with st.expander('Indicações de Leitura'):
        st.write('Empresa especializada em cibersegurança - https://www.perallis.com/news')
        st.write('Empresa especializada em cibersegurança - https://www.olharldigital.com/')
        st.write('Empresa especializada em tecnologia, com notícias de cibersegurança - https://www.tecmundo.com.br/seguranca')
        st.write('Agência de notícias com foco em desinformação - https://lupa.uol.com.br/')
        st.write('Como parar com o Bullying - https://www.unicef.org/brazil/cyberbullying-o-que-eh-e-como-para-lo')
        st.write('Como denunciar abuso no Twitter- https://help.twitter.com/pt/safety-and-security/report-abusive-behavior#:~:text=Pressione%20e%20mantenha%20pressionada%20a,e%20selecione%20Denunciar%20%40username).&text=Caso%20voc%C3%AA%20selecione%20%C3%89%20abusivo,o%20problema%20que%20est%C3%A1%20denunciando')

    with st.expander('Notícias Importantes'):
        st.write('Hackers Chineses Invadem Entidades Governamentais pelo Mundo : Brasil na Lista - https://canaltech.com.br/hacker/hackers-chineses-invadem-entidades-governamentais-pelo-mundo-brasil-na-lista-158443/')
        st.write('Como Evitar que seu Filho seja Vítima de Crimes na Internet - https://vejario.abril.com.br/coluna/fabio-barbirato/como-evitar-que-seu-filho-seja-vitima-de-crimes-na-internet/')
        st.write('Windows 11 coleta e envia dados de usuários para várias Empresas, Denuncia youtuber - https://www.adrenaline.com.br/seguranca/windows-11-coleta-e-envia-dados-de-usuarios-para-varias-empresas-denuncia-youtuber/')
        st.write('Como dificultar a coleta de dados no computador e no celular - https://olhardigital.com.br/2019/08/09/dicas-e-tutoriais/como-dificultar-a-coleta-de-dados-no-computador-e-no-celular/')
        st.write('Golpe de Perfil Fake em relações virtuais atinge 1 a cada 4 brasileiros - https://www.techtudo.com.br/noticias/2022/03/golpe-do-perfil-fake-em-relacoes-virtuais-atinge-1-a-cada-4-brasileiros.ghtml')
        st.write('Exclusivo: investigação revela exército de perfis falsos usados para influenciar eleições no Brasil - https://www.bbc.com/portuguese/brasil-42172146')
        st.write('Pesquisa da Intel revela dados sobre Cyberbullying no brasil - https://arquivo.canaltech.com.br/comportamento/pesquisa-da-intel-revela-dados-sobre-cyberbullying-no-brasil-46105/')
        st.write(' Caso real de linchamento que inspirou Glória Perez em Travessia - https://www.uol.com.br/splash/noticias/2022/10/11/o-caso-real-de-linchamento-que-inspirou-gloria-perez-em-travessia.html')
    with st.expander('Explicando conceitos'):
        st.subheader('Software Livre vs proprietário')
        st.write('Comparação Software Livre e Programas Pagos - https://g1.globo.com/tecnologia/blog/tira-duvidas-de-tecnologia/post/software-livre-vale-pena-ser-substituido-por-programas-pagos.html')
        st.write('Definição original de Software livre - https://www.gnu.org/philosophy/free-sw.pt-br.html')


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
        st.write('Site que verifica se algum endereço de e-mail ou senha seus já foi vazado - https://www.haveibeenpwned.com/')
        st.write('Site comunitário que analisa os termos de serviços de sites e aplicativos no mundo - https://tosdr.org/pt_BR/frontpage/')
        st.write('Sites que checam a veracidade de boatos viralizados recentemente - https://www.boatos.org/ e https://www.e-farsas.com/')
        st.write('Site ensinando como ativar o monitoramento parental - https://www.techtudo.com.br/dicas-e-tutoriais/2023/03/como-ativar-monitoramento-parental-nas-redes-sociais-e-proteger-seu-filho-edapps.ghtml')
        
    st.header('Ajuda / Denúncia')
    with st.expander('Ajuda / Denúncia'):
        st.write('Linha de Ajuda (helpline) - https://new.safernet.org.br/helpline?gclid=Cj0KCQjwnf-kBhCnARIsAFlg491cAxCfJSYZiW4XY0cQvhDGyaohOFFyzz_hHFndxNKSWez4knI0mhQaAq5BEALw_wcB#') 
        st.write('Lista de todas as delegacias do Brasil - https://new.safernet.org.br/content/delegacias-cibercrimes') 