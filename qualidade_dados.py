import pandas as pd
from sqlalchemy import create_engine

# 1. CONEXÃO
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

# 2. LEITURA DA CAMADA 'BRONZE' (O que você já tem no banco)
df = pd.read_sql("SELECT * FROM tabela_airbnb_rio", engine)

print(f"📊 Total de registros iniciais: {len(df)}")

# --- PILAR 1: GARANTIA DE QUALIDADE (DATA QUALITY) ---

# A. Removendo Preços Nulos ou Zerados
# Um anúncio com preço 0 é um erro de dado.
df = df[df['price'] > 0]

# B. Tratando Outliers (O segredo do Estácio)
# Vamos definir que qualquer preço acima de 10 mil reais por noite é um erro (outlier)
# Isso vai limpar a média dos bairros.
limite_superior = 10000
df = df[df['price'] <= limite_superior]

# C. Corrigindo o Texto (Encoding)
# Isso resolve o problema do "EstÃ¡cio" -> "Estácio"
df['neighbourhood_cleansed'] = df['neighbourhood_cleansed'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

# --- PILAR 2: MODELAGEM (CAMADA SILVER) ---

print(f"✅ Total de registros após limpeza de qualidade: {len(df)}")

# Enviando para uma NOVA tabela chamada 'silver_airbnb_rio'
# Na engenharia, mantemos a original (bronze) e a limpa (silver)
df.to_sql('silver_airbnb_rio', engine, if_exists='replace', index=False)

print("🚀 Dados de alta qualidade salvos na tabela 'silver_airbnb_rio'!")