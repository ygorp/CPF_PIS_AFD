import pandas as pd

# Lê o arquivo Excel
arquivo_excel = 'dados.xlsx'
df = pd.read_excel(arquivo_excel, sheet_name='Planilha1')

# Localiza as colunas CPF e PIS
coluna_cpf = 'CPF'.strip()
coluna_pis = 'PIS'.strip()

# Itera pelas linhas do DataFrame
for index, row in df.iterrows():
    cpf = row[coluna_cpf]
    pis = row[coluna_pis]

    # Abre o arquivo txt para substituição
    arquivo_txt = 'AFD0001400375022157604567650000840REP_C.txt'
    with open(arquivo_txt, 'r') as arquivo:
        conteudo = arquivo.read()
        conteudo = conteudo.replace(str(cpf), str(pis))

    # Escreve o conteúdo de volta no arquivo txt
    with open(arquivo_txt, 'w') as arquivo:
        arquivo.write(conteudo)

print("Substituição concluída com sucesso!")
