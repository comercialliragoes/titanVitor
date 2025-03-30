import streamlit as st

pontos = 0
st.title('Game titanic')
with st.form('b'):
    pergunta1 = st.selectbox('que dia ano e mes o titanic afundou?',[' ','14 de abril de 1912','12 de maio de 2000','31 de março de 1899'])
    pergunta2 = st.selectbox('o titanic afundou porque?',[' ','mina aquatica','pedra subaquatica','bate no iceberg'])
    pergunta3 = st.selectbox('qual a classe de navios do titanic?',[' ','cunard line','whit star line','britannic'])
    pergunta4 = st.selectbox('que horas o titanic bateu no iceberg?',[' ','23:40','11:20','9:00'])
    pergunta5 = st.selectbox('o titanic quebrou no meio?',[' ','sim','não','não sei'])
    pergunta6 = st.selectbox('quantas pessoas sobreviveram au naufragio',[' ','1500','200','600'])
    pergunta7 = st.selectbox('quantos metros o titanic tinham?',[' ','333','243','269'])
    pergunta8 = st.selectbox('onde o titanic afundou?',[' ','atlantico sul','atlantico norte','pacifico sul'])
    pergunta9 = st.selectbox('qual a temperatura da água no momento do nalfragio?',[' ','-2','15','-15'])
    pergunta10 = st.selectbox('que horas o titanic quebrou no meio?',[' ','2:30','22:00','2:10'])

    botao = st.form_submit_button('Verificar as respostas:')
    if botao :
        if pergunta1 == '14 de abril de 1912':
            pontos+=1
        if pergunta2 == 'bate no iceberg':
            pontos+=1
        if pergunta3 == 'whit star line':
            pontos+=1
        if pergunta4 == '23:40':
            pontos+=1
        if pergunta5 == 'sim':
            pontos+=1
        if pergunta6 == '1500':
            pontos+=1
        if pergunta7 == '269':
            pontos+=1
        if pergunta8 == 'atlantico norte':
            pontos+=1
        if pergunta9 == '-2':
            pontos+=1
        if pergunta10 == '2:10':
            pontos+=1
        
        if pontos < 1:
            st.write(f'Voce precisa estudar mais sobre o Titanic')
        if pontos > 1 and pontos < 5:
            st.write(f'voce precisa estudar mais')
        if pontos > 5 and pontos <= 9:
            st.write(f'voce acertou {pontos} pontos')
        if pontos == 10:
            st.write('*****************************')
            st.write('*PARABENS voce acertou todas*')
            st.write('*****************************')
            audio_file =open('m.mp3','rb')
            audio_bytes =audio_file.read()
            st.audio(audio_bytes,format = 'audio/mp3')


























































































































































