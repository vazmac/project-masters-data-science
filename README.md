# Previsão de Preços de Imóveis em Lisboa

## Introdução

Este projeto marca um ponto de viragem na minha carreira profissional: a transição de Engenheiro Industrial para Engenheiro de Dados. Foi o meu primeiro projeto no domínio da ciência de dados, representando o início de uma jornada no universo da análise e processamento de dados em larga escala.

Embora o projeto esteja fundamentalmente focado em *data science* e não siga as melhores práticas modernas de engenharia de dados (como containerização e arquitetura distribuída), foram os temas relacionados com **arquitetura de dados** e **desenvolvimento de pipelines** que capturaram verdadeiramente o meu interesse. O trabalho exploratório, embora necessário, foi apenas um meio para chegar a estes fins. Este projeto evidencia a minha paixão por estruturar fluxos de dados eficientes e escaláveis, sendo uma das razões que me levou a abraçar completamente a carreira em engenharia de dados.

## Descrição do Projeto

Este projeto implementa um sistema de análise de preços para imóveis em Lisboa, utilizando técnicas de *machine learning*. O sistema permite ao utilizador avaliar se o preço de uma propriedade está ajustado ao mercado ou se está inflacionado/subvalorizado. Para isso, o utilizador insere as características do imóvel **e o preço de listagem**, e o modelo compara com a previsão para gerar uma análise de mercado.

### Componentes Principais

#### 1. **Extração de Dados**
- Integração com a **API do Idealista** para coleta de dados de imóveis
- Armazenamento dos dados em ficheiros CSV para processamento posterior
- Documentação técnica da API incluída na pasta `documentation/`

#### 2. **Análise e Pré-processamento**
- Exploração dos dados através de notebooks Jupyter
- Transformação e limpeza dos dados brutos
- Engenharia de características (*feature engineering*)
- Criação de variáveis derivadas (ex: `size_per_room`, `isCityCenter`, etc.)
- Normalização e codificação de variáveis categóricas

#### 3. **Modelagem de Machine Learning**
- Desenvolvimento e treino de um modelo preditivo
- Avaliação de desempenho do modelo
- Serialização do modelo treinado para reutilização

#### 4. **Interface Web**
- Aplicação **Flask** como *backend*
- Interface HTML responsiva como *frontend*
- Formulário interativo para inserção de características do imóvel e preço de listagem
- Análise comparativa entre preço inserido e previsão do modelo
- Classificação de ajuste de preço (ajustado, inflacionado, subvalorizado) em tempo real

## Estrutura do Projeto

```
Project/
├── app.py                          # Aplicação Flask
├── preprocessing.py                # Funções de pré-processamento de dados
├── final_model.pkl                 # Modelo ML treinado (serializado)
├── estacoes_metro_lisboa.csv       # Dados de estações de metro
├── idealista.csv                   # Dados extraídos da API do Idealista
├── app.ipynb                       # Notebook da aplicação Flask
├── preprocessing.ipynb             # Notebook de pré-processamento
├── data_extraction_api.ipynb       # Notebook de extração de dados da API
├── notebook_final_version.ipynb    # Análise e modelagem completa
├── documentation/                  # Documentação técnica
│   ├── oauth2-documentation.pdf
│   └── property-search-api-v3_5.pdf
├── templates/
│   └── home.html                   # Interface web
└── README.md                       # Este ficheiro
```

## Funcionalidades

- **Análise Exploratória de Dados (EDA)**: Análise detalhada das características dos imóveis e distribuição de preços
- **Extração de Dados em Tempo Real**: Integração com API do Idealista para obtenção de dados atualizados
- **Modelo Preditivo**: Modelo treinado capaz de estimar preços baseado em características do imóvel
- **Análise Comparativa de Preços**: Comparação entre o preço de listagem inserido pelo utilizador e a previsão do modelo
- **Classificação de Ajuste de Mercado**: Determina se o preço está ajustado, inflacionado ou subvalorizado
- **Interface Interativa**: Aplicação web intuitiva que permite aos utilizadores avaliar a competitividade de um imóvel no mercado
- **Pré-processamento Automatizado**: Pipeline de transformação de dados para preparação de inputs

## Características Consideradas

O modelo utiliza as seguintes características para fazer previsões:

**Entradas do Utilizador:**
- **Preço de Listagem** (€): O preço que o proprietário está a pedir pelo imóvel
- **Tamanho** do imóvel (m²)
- **Número de Quartos** e **Casas de Banho**
- **Localização** (Município/Freguesias de Lisboa)
- **Comodidades**:
  - Mobiliário
  - Varanda
  - Estação de Metro próxima
  - Elevador
  - Garagem
- **Luxo**: Classificação de imóvel de luxo
- **Tipo de Propriedade**: Categorias de imóvel (T0, T1, Duplex, etc.)

**Saída do Sistema:**
- Preço previsto pelo modelo (€)
- Diferença entre preço de listagem e previsão
- Classificação: "Ajustado", "Inflacionado" ou "Subvalorizado"

## Variáveis Derivadas

Durante o pré-processamento, o modelo cria as seguintes variáveis:

- `size_per_room`: Relação entre tamanho total e número de compartimentos
- `total_rooms`: Soma de quartos e casas de banho
- `isCityCenter`: Indica se o imóvel localiza-se nas freguesias centrais de Lisboa
- `propertyType_duplex`: Codificação binária para imóveis do tipo duplex

## Requisitos de Execução

- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Pickle (para serialização do modelo)

## Como Utilizar

### 1. Preparação dos Dados
Execute o notebook `data_extraction_api.ipynb` para extrair dados da API do Idealista (requer credenciais OAuth2).

### 2. Pré-processamento e Modelagem
Execute o notebook `notebook_final_version.ipynb` para processar e treinar o modelo.

### 3. Execução da Aplicação Web
```bash
python app.py
```
A aplicação estará disponível em `http://localhost:5000`

### 4. Avaliar Preços
Aceda à interface web e:
1. Preencha as características do imóvel
2. Insira o preço de listagem (€)
3. Clique em "Analisar"
4. Receba uma análise comparativa indicando se o preço está ajustado, inflacionado ou subvalorizado

## Notas Técnicas

Este projeto, apesar de estar centrado em data science, reflete uma abordagem orientada para a **engenharia de dados**:
- Os dados são extraídos de uma fonte externa (API) e armazenados de forma estruturada
- Um pipeline de pré-processamento limpo e reutilizável é implementado
- O modelo treinado é serializado para reutilização em produção
- A arquitetura separa claramente as fases de extração, transformação e aplicação

Futuras melhorias poderiam incluir containerização (Docker), orquestração de workflows (Airflow), e deployment em plataformas cloud.

## Autor

Projeto desenvolvido como Trabalho de Fim de Mestrado (TFM) - Mestrado em Engenharia Industrial com Especialização em Engenharia de Dados.

---

**Última atualização**: Maio 2024
