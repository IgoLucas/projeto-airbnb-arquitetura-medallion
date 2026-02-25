import pandas as pd
from sqlalchemy import create_engine

# 1. CONEXÃO (Sem senha)
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

print("⏳ Lendo o arquivo CSV... isso pode levar uns segundos.")
# Lendo o arquivo que está na mesma pasta
df = pd.read_csv('listings.csv', low_memory=False, encoding='ISO-8859-1')
# 2. DATA CLEANING (O que seu tutor pediu)
print("🧼 Limpando os dados...")
# Selecionamos as colunas principais
colunas = ['id', 'name', 'host_id', 'neighbourhood_cleansed', 'price']
df_limpo = df[colunas].copy()

# Limpeza do Preço: remove o '$' e a vírgula para virar número
df_limpo['price'] = df_limpo['price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

# 3. ENVIAR PARA O POSTGRES
print("🚀 Enviando para o banco de dados...")
# Tenta enviar para o esquema 'bronze', se não existir, envia para o 'public'
# Enviando direto para o padrão 'public' que sempre funciona
df_limpo.to_sql('tabela_airbnb_rio', engine, if_exists='replace', index=False)
print("✅ Tabela criada com sucesso no esquema public!")

print("🏁 Tudo pronto! Pode conferir no DBeaver.")