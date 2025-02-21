# utils/get_exibicao.py

import streamlit as st
from utils.get_timeline import get_linha_tempo_avancada
from utils.get_prazo_migracao import get_prazo_migracao

def get_dados_exibicao_aluno(info_aluno):

    st.markdown(f"##### 👨‍🎓 {info_aluno['nome']}")  # Nome do aluno em destaque

    st.markdown(f"""
    **📌 Dados do Aluno Selecionado**  
    - 🏫 **Ano de Ingresso e Semestre (Especial):** `{info_aluno['ano_sem_ingresso_especial']}`  
    - 🏫 **Ano de Ingresso e Semestre (Regular):** `{info_aluno['ano_sem_ingresso_regular']}`  
    - 🎓 **Modalidade:** `{info_aluno['modalidade']}`  
    - 📖 **Tipo:** `{info_aluno['tipo']}`  
    - 👨‍🏫 **Orientador:** `{info_aluno['orientador']}`  
    - 👩‍🏫 **Coorientador:** `{info_aluno['coorientador']}`  
    - 🔄 **Trancamento:** `{info_aluno['trancamento']}`  
    - 💰 **Bolsa de Fomento:** `{info_aluno['bolsa_fomento']}`  
    - 🔬 **Projetos Externos:** `{info_aluno['projetos_ext']}`  
    - 🇬🇧 **Inglês:** `{info_aluno['inglês']}`  
    - 🏅 **Qualificação:** `{info_aluno['qualificacao']}`  
    - 📚 **Número de Créditos:** `{info_aluno['num_creditos_cursados']}`  
    - 📜 **Título:** `{info_aluno['titulo']}`  
    """)

    if info_aluno['ano_sem_ingresso_regular'] == 'NA':
        prazo_migracao = get_prazo_migracao(
            info_aluno['ano_sem_ingresso_especial'], info_aluno['modalidade'])
        st.markdown(f"##### 📅 Prazo Limite para Migrar para Regular: `{prazo_migracao}`")
    else:
        st.markdown("##### 📅 Linha do Tempo Acadêmica")  # Fonte menor
        fig = get_linha_tempo_avancada(
            info_aluno['ano_sem_ingresso_regular'], info_aluno['modalidade'])
        st.pyplot(fig)

