import pandas as pd

# Ler o arquivo com ajuste de linhas ignoradas (se necessário)
emissoes_gases = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name = 'GEE Estados')


emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']
emissoes_gases = emissoes_gases.drop(columns = 'Emissão / Remoção / Bunker')

#Chegou o momento de praticar! Vamos aplicar os conceitos aprendidos durante a aula a partir de
#algumas atividades. Solucione os problemas propostos através de códigos utilizando a base de dados
#disponibilizada no curso.

#Encontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar as atividades
#econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.

emissoes_gases["Estado"].unique(),emissoes_gases['Nível 1 - Setor'].unique()

#Filtre o DataFrame somente com os dados dos Estados da região Sul do Brasil.

emissoes_gases.loc[emissoes_gases['Estado'].isin(['PR', 'SC', 'RS'])]

#Filtre o DataFrame para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a
#"Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).

emissoes_gases_AM = emissoes_gases.query('Estado == "AM"')
emissoes_gases_AM = emissoes_gases_AM.query('`Nível 1 - Setor` == "Mudança de Uso da Terra e Floresta"')

#Encontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.

emissoes_gases_PA = emissoes_gases.query('Estado == "PA"')
emissoes_gases_PA = emissoes_gases_PA.query('`Nível 1 - Setor` == "Agropecuária"')
emissoes_gases_PA[2021].max()

#Mesma resposta com loc

emissoes_gases.loc[(emissoes_gases['Nível 1 - Setor'] == 'Agropecuária') & (emissoes_gases['Estado'] == 'PA'), 2021].max()