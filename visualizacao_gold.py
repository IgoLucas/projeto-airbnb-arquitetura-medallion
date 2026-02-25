import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Conectando na nossa camada final (GOLD)
engine = create_engine('postgresql://postgres:1234@localhost:5432/postgres')

# 1. Buscando os dados que eu processei e salvei na Gold
print("📊 Carregando dados da camada Gold para o gráfico...")
df_gold = pd.read_sql("SELECT * FROM gold_media_bairros LIMIT 10", engine)

# 2. Configurando o visual do gráfico
plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Criando o gráfico de barras
grafico = sns.barplot(
    x='preco_medio', 
    y='neighbourhood_cleansed', 
    data=df_gold, 
    palette='viridis'
)

# Colocando títulos que explicam o que eu fiz
plt.title('Top 10 Bairros Mais Caros do Rio (Dados Tratados e Validados)', fontsize=15)
plt.xlabel('Preço Médio por Noite (R$)', fontsize=12)
plt.ylabel('Bairro Oficial', fontsize=12)

# 3. Exibir o resultado
print("🎨 Gerando gráfico... feche a janela do gráfico para encerrar.")
plt.show()