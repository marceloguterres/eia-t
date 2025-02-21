# utils/get_filtros.py

def get_orientadores(df):
    return sorted(df['orientador'].dropna().unique())

def get_alunos(df):
    return sorted(df['nome'].dropna().unique())

