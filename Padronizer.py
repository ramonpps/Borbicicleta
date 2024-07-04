import pandas as pd

# Carregar o arquivo CSV
file_path = 'inputs\Mobilidade Elétrica Niterói.csv'
df = pd.read_csv(file_path)

# Listar as colunas de interesse
columns_to_standardize = [
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por tempo. (Unidade: R$ por 15 minutos)',
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por distância.\n(Unidade: R$ por um km) ',
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por consumo de energia.\n(Unidade: R$ por um kWh) ',
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por plano diário.',
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por plano mensal. ',
    'Quanto você estaria disposto a pagar por esse serviço? \n\nConsiderando aluguel por plano anual. '
]

# Função para padronizar as colunas
def standardize_to_float(column):
    return pd.to_numeric(column.astype(str).str.replace(',', '.').str.replace('R$', '').str.strip(), errors='coerce').round(2)

# Aplicar a função a cada coluna e calcular a média
for column in columns_to_standardize:
    if column in df.columns:
        df[column] = standardize_to_float(df[column])
        mean_value = df[column].mean()
        print(f'Média da coluna "{column}": {mean_value:.2f}\n')

# Salvar o DataFrame modificado em um novo arquivo CSV
output_file_path = 'outputs\Mobilidade_Elétrica_Niterói_Padronizado.csv'
df.to_csv(output_file_path, index=False)
