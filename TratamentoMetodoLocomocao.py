import pandas as pd

df = pd.read_csv('inputs/Mobilidade Elétrica Niterói.csv')
colunas_interessantes = [
    col for col in df.columns 
    if 'Como você se locomove entre os campi?' in col
]
df_filtrado = df[colunas_interessantes]
df_filtrado.to_csv("outputs/Mobilidade_Eletrica_Niterói_Filtrado_Metodos.csv", index=False)


import pandas as pd

class CSVProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def transform_data(self):
        """Lê o arquivo CSV e transforma os dados conforme necessário."""
        data = pd.read_csv(self.input_file)
        
        # Renomear a coluna para simplificação
        data.columns = ['metodos']

        # Separar os métodos em colunas individuais
        methods_split = data['metodos'].str.split(';', expand=True)

        # Criar nomes dinâmicos para as colunas de métodos
        method_columns = [f'METODO {i+1}' for i in range(methods_split.shape[1])]
        methods_split.columns = method_columns

        # Adicionar a coluna "VIAGEM" com valores autoincrementados
        methods_split.insert(0, 'VIAGEM', range(1, len(methods_split) + 1))

        # Salvar o novo dataframe em um arquivo CSV
        methods_split.to_csv(self.output_file, index=False)
        print(f"Novo arquivo CSV salvo em: {self.output_file}")

    def process(self):
        """Executa todas as etapas de processamento."""
        self.transform_data()

if __name__ == "__main__":
    input_file = 'outputs/Mobilidade_Eletrica_Niterói_Filtrado_Metodos.csv'
    output_file = 'outputs/Relação_de_Metodos.csv'
    
    processor = CSVProcessor(input_file, output_file)
    processor.process()
