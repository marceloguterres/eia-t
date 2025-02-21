# utils/get_prazo_migracao.py

def get_prazo_migracao(ano_semestre_especial, modalidade):
    if ano_semestre_especial == 'NA':
        return 'Dados de ingresso especial não disponíveis'
    
    try:
        ano, semestre = map(int, ano_semestre_especial.split('-'))
        limite = 4 if modalidade.lower() == "mestrado" else 8
        semestre_total = semestre + limite
        ano_migracao = ano + (semestre_total - 1) // 2
        semestre_migracao = (semestre_total - 1) % 2 + 1
        return f"{ano_migracao}-{semestre_migracao}"
    except ValueError:
        return 'Erro ao calcular o prazo de migração'


