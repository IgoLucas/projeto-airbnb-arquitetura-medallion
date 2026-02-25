import pandas as pd
from sqlalchemy import create_engine

# 1. Configurando a conexão com o nosso banco local
# Aqui uso o engine que já validamos com a senha 1234
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

print("🏆 Iniciando a criação da Camada Gold (Dados Prontos para Uso)...")

# 2. Lendo os dados da camada Silver
# Eu busco da 'silver_airbnb_rio' porque ela já passou pelo filtro de qualidade
# e não tem mais aqueles preços absurdos (outliers) que vimos antes.
query_silver = "SELECT * FROM silver_airbnb_rio"
df_silver = pd.read_sql(query_silver, engine)

# 3. Gerando os insights (Agrupamento e Agregação)
# entendi que para o relatório ser útil, preciso de:
# - Média de preço por bairro (para saber o valor de mercado)
# - Contagem de imóveis (para saber se o bairro tem amostragem boa)
relatorio = df_silver.groupby('neighbourhood_cleansed').agg(
    preco_medio=('price', 'mean'),
    quantidade_anuncios=('id', 'count')
).sort_values(by='preco_medio', ascending=False)

# 4. Arredondando os valores para ficar mais apresentável
relatorio['preco_medio'] = relatorio['preco_medio'].round(2)

# 5. Salvando a Camada Gold no Banco de Dados
# Esta tabela 'gold_media_bairros' é a que será usada para gráficos e apresentações.
relatorio.reset_index().to_sql('gold_media_bairros', engine, if_exists='replace', index=False)

print("\n✨ VISÃO FINAL - TOP 10 BAIRROS (DADOS VALIDADOS):")
print(relatorio.head(10))

print("\n✅ Etapa concluída! A tabela Gold foi criada no PostgreSQL.")
print("🚀 O pipeline está completo: CSV -> Bronze -> Silver -> Gold.")