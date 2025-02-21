# utils/get_orientados_tab.py
import streamlit as st
from utils.get_exibicao import get_dados_exibicao_aluno
from utils.get_data_loader import get_info_aluno

def get_orientados_tab(df, orientador_selecionado):
    st.markdown(f"### Orientados do Professor(a) {orientador_selecionado}")
    df_orientados = df[df['orientador'] == orientador_selecionado]
    if not df_orientados.empty:
        for idx, row in df_orientados.iterrows():
            with st.expander(f"🎓 {row['nome']} - {row['modalidade']}"):
                get_dados_exibicao_aluno(get_info_aluno(df_orientados[df_orientados['nome'] == row['nome']]))
    else:
        st.warning("Nenhum orientado encontrado para este professor.")
