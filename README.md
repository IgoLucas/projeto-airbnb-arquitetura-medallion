🏠 Projeto Airbnb Rio de Janeiro - Arquitetura Medallion

Este projeto foi desenvolvido para aplicar conceitos de Engenharia de Dados em um cenário real. Utilizei dados públicos do Airbnb para construir um pipeline completo, focando em organização, limpeza e transformação de dados utilizando a Arquitetura Medallion.

O objetivo principal foi transformar um dataset bruto (.csv) em tabelas estruturadas no PostgreSQL, prontas para análise.

 Estrutura do Banco de Dados

Como o GitHub não armazena o banco de dados em si, abaixo demonstro como os dados foram organizados dentro do PostgreSQL seguindo as camadas de qualidade:

Camada Bronze (Dados Brutos): Nesta etapa, o dado é ingerido exatamente como vem do CSV. Note que os tipos de dados ainda são genéricos (strings).

Camada Silver (Dados Limpos): Aqui os dados já passaram pelo tratamento em Python. Preços foram convertidos para numérico e colunas desnecessárias foram removidas.

Camada Gold (Visão de Negócio): Tabelas agregadas prontas para o time de análise, como a média de preços por bairro.

Evidências e Resultados

Estrutura da Camada Gold (Visualização no DBeaver)
Insight: Top 10 Bairros Mais Caros do Rio

Tratamento do Dataset (Big Data)

O arquivo original listings.csv possui aproximadamente 82MB, o que excede as recomendações de versionamento do GitHub. Por boas práticas de Engenharia de Dados, o dataset não foi incluído neste repositório para manter o projeto leve e focado no código.

Como obter os dados:

Acesse o site Inside Airbnb.

Procure pela seção do Rio de Janeiro.

Baixe o arquivo listings.csv.gz, descompacte e coloque na pasta raiz do projeto.

Nota Técnica: No desenvolvimento, utilizei o arquivo .csv localmente, garantindo que o script bronze_ingestion.py fizesse a leitura e o carregamento para o PostgreSQL de forma otimizada, sem comprometer a performance do Git.

Ferramentas Utilizadas

Linguagem: Python (Pandas para manipulação).

Banco de Dados: PostgreSQL (armazenamento das camadas).

Conexão: SQLAlchemy e Psycopg2.

Desafios e Aprendizados

Tratamento de Dados: Limpeza de caracteres especiais e conversão de tipos de dados.

Organização: Implementação da arquitetura Medallion para garantir a linhagem dos dados.

<img width="1366" height="768" alt="00eddc89-c0bc-41c5-9865-39e2589bf193" src="https://github.com/user-attachments/assets/087ed142-9859-43a3-9993-a2af9175fd75" />

![Design sem nome (2)](https://github.com/user-attachments/assets/44798c56-2ddc-4f50-bf6c-2b79a647a80f)
