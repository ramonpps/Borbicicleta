import pandas as pd

class CSVProcessor:
    def __init__(self, input_file, output_file_filtered, output_file_final):
        self.input_file = input_file
        self.output_file_filtered = output_file_filtered
        self.output_file_final = output_file_final

    def filter_columns(self):
        """Lê o arquivo CSV original e filtra as colunas de interesse."""
        df = pd.read_csv(self.input_file)
        colunas_interessantes = [
            col for col in df.columns 
            if 'Quais regiões lhe interessariam ter uma estação de compartilhamento de bicicletas elétricas?' in col
        ]
        df_filtrado = df[colunas_interessantes]
        df_filtrado.to_csv(self.output_file_filtered, index=False)
        print(f"Arquivo CSV filtrado salvo em: {self.output_file_filtered}")

    def transform_data(self):
        """Lê o arquivo CSV filtrado e transforma os dados conforme necessário."""
        data = pd.read_csv(self.output_file_filtered)
        
        # Renomear a coluna para simplificação
        data.columns = ['regioes']

        # Separar as regiões em colunas individuais
        regions_split = data['regioes'].str.split(';', expand=True)

        # Criar nomes dinâmicos para as colunas de regiões
        region_columns = [f'REGIAO {i+1}' for i in range(regions_split.shape[1])]
        regions_split.columns = region_columns

        # Adicionar a coluna "VIAGEM" com valores autoincrementados
        regions_split.insert(0, 'VIAGEM', range(1, len(regions_split) + 1))

        # Salvar o novo dataframe em um arquivo CSV
        regions_split.to_csv(self.output_file_final, index=False)
        print(f"Novo arquivo CSV salvo em: {self.output_file_final}")

    def process(self):
        """Executa todas as etapas de processamento."""
        self.filter_columns()
        self.transform_data()

if __name__ == "__main__":
    input_file = 'inputs/Mobilidade Elétrica Niterói.csv'
    output_file_filtered = 'outputs/Mobilidade_Elétrica_Niterói_Filtrado_Regioes.csv'
    output_file_final = 'outputs/Relação_de_Regiões.csv'
    
    processor = CSVProcessor(input_file, output_file_filtered, output_file_final)
    processor.process()
