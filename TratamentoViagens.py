import pandas as pd
import re

class DataCleaner:
    @staticmethod
    def comeca_com_numero(s):
        return str(s)[0].isdigit() if pd.notnull(s) else False

    @staticmethod
    def extrair_primeiros_numeros(s):
        if "Depois das" in s:
            return s
        match = re.findall(r'\d+', str(s))
        return match[0] if match else s

    def __init__(self, csvOrigem):
        self.csvOrigem = csvOrigem
        self.df = pd.read_csv(csvOrigem)

    def selecionar_colunas_validas(self):
        colunas_validas = [col for col in self.df.columns if DataCleaner.comeca_com_numero(col)]
        self.df = self.df[colunas_validas]

    def salvar_csv_tratado(self, output_path='outputs\Mobilidade_Elétrica_Niterói_Filtrado_Viagens.csv'):
        self.df.to_csv(output_path, index=False)

class DataFormatter:
    def __init__(self, csvOrigem):
        self.csvOrigem = csvOrigem
        self.df = pd.read_csv(csvOrigem)
        self.dados_formatados = []

    def formatar_dados(self):
        for index, row in self.df.iterrows():
            for i in range(0, len(row), 3):
                if i + 2 < len(row) and pd.notnull(row[i]) and pd.notnull(row[i + 1]) and pd.notnull(row[i + 2]):
                    hora = DataCleaner.extrair_primeiros_numeros(row[i])
                    origem = row[i + 1]
                    destino = row[i + 2]
                    self.dados_formatados.append([hora, origem, destino])

    def criar_novo_dataframe(self):
        novo_df = pd.DataFrame(self.dados_formatados, columns=['SAÍDA', 'ORIGEM', 'DESTINO'])
        novo_df.dropna(inplace=True)
        novo_df.insert(0, 'VIAGEM', range(1, len(novo_df) + 1))
        return novo_df

    def salvar_csv_formatado(self, output_path='outputs\Relação_de_Viagens.csv'):
        novo_df = self.criar_novo_dataframe()
        novo_df.to_csv(output_path, index=False)

class DataProcessor:
    @staticmethod
    def processar_dados():
        cleaner = DataCleaner("inputs\Mobilidade Elétrica Niterói.csv")
        cleaner.selecionar_colunas_validas()
        cleaner.salvar_csv_tratado()

        formatter = DataFormatter('outputs\Mobilidade_Elétrica_Niterói_Filtrado_Viagens.csv')
        formatter.formatar_dados()
        formatter.salvar_csv_formatado()

# Executa o processamento dos dados e criação do CSV novo
DataProcessor.processar_dados()
