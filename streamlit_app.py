# app_aeropos.py
import streamlit as st
import pandas as pd
from utils.get_data_loader import get_dados, get_info_aluno
from utils.get_timeline import get_linha_tempo_avancada
from utils.get_prazo_migracao import get_prazo_migracao
from utils.get_filtros import get_orientadores, get_alunos
from utils.get_exibicao import get_dados_exibicao_aluno
from utils.get_orientados_tab import get_orientados_tab

def main():
    st.set_page_config(page_title="AeroPos", layout="wide")

    st.title("AeroPos")
    st.markdown("### Análise e Registro de Operações da Pós-graduação em Infraestrutura Aeronáutica")

    df = get_dados("base_de_dados_eia_t.ods")
    if df is None:
        st.error("Arquivo 'base_de_dados_eia_t.ods' não encontrado. Verifique se o arquivo está na mesma pasta do script.")
        st.stop()

    # Criando abas
    tab1, tab2 = st.tabs(["👨‍🎓 Alunos", "👨‍🏫 Orientados por Professor"])

    # Sidebar - Filtros
    st.sidebar.markdown("## Filtros")

    # Filtro de Professores no Sidebar
    if 'orientador' in df.columns:
        orientadores = get_orientadores(df)
        orientador_selecionado = st.sidebar.selectbox("Selecione um Orientador", orientadores)

        # Na aba de Orientados, mostrar os alunos do orientador selecionado
        with tab2:
            get_orientados_tab(df, orientador_selecionado)

    # Aba de Alunos
    with tab1:
        if 'nome' in df.columns:
            nomes = get_alunos(df)
            nome_selecionado = st.sidebar.selectbox("Selecione um Nome", nomes)

            df_filtrado = df[df['nome'] == nome_selecionado]

            if not df_filtrado.empty:
                info_aluno = get_info_aluno(df_filtrado)
                get_dados_exibicao_aluno(info_aluno)
            else:
                st.warning("Nenhum dado encontrado para o aluno selecionado.")
        else:
            st.error("A coluna 'nome' não está presente no DataFrame. Verifique a base de dados.")

if __name__ == "__main__":
    main()

