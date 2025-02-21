# utils/get_data_loader.py
import pandas as pd

def get_dados(arquivo):
    try:
        df = pd.read_excel(arquivo, engine="odf", dtype={
            'ano_sem_ingresso_regular': str,
            'ano_sem_ingresso_especial': str
        })
        return df
    except FileNotFoundError:
        return None

def get_info_aluno(df_filtrado):
    info = {}
    campos = [
        'nome',  # Adicionando o campo nome
        'ano_sem_ingresso_regular', 'ano_sem_ingresso_especial', 'modalidade', 'tipo', 'orientador', 'coorientador',
        'trancamento', 'bolsa_fomento', 'projetos_ext', 'inglês', 'qualificacao',
        'num_creditos_cursados', 'titulo'
    ]
    
    for campo in campos:
        if campo in df_filtrado.columns and not df_filtrado.empty:
            valor = df_filtrado[campo].iloc[0]
            if campo in ['ano_sem_ingresso_regular', 'ano_sem_ingresso_especial'] and isinstance(valor, pd.Timestamp):
                valor = valor.strftime('%Y-%m')  # Converter data para string no formato desejado
            elif campo == 'inglês' and isinstance(valor, pd.Timestamp):
                valor = valor.strftime('%Y-%m-%d')  # Remover timezone e mostrar só a data
            info[campo] = str(valor) if pd.notna(valor) else 'NA'
        else:
            info[campo] = 'NA'
    
    # Tratamento especial para coorientador
    if info.get('coorientador') == 'NA':
        info['coorientador'] = 'Sem coorientação'
        
    return info

