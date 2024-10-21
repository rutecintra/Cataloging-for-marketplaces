# Cataloging-for-marketplaces

Neste projeto trago algumas funcionalidades importantes para a catalogação de produtos para marketplaces.

# Product Weight Estimator

Este projeto é uma aplicação web que processa informações de produtos, incluindo imagens, e utiliza APIs externas (BestBuy, OpenAI GPT e Google Cloud Vision) para estimar o peso de cada produto. Ele calcula o peso com base em dados disponíveis nas APIs, processa informações em massa e fornece uma média de peso entre diferentes fontes.

## Funcionalidades

- Processamento de produtos em massa via API.
- Integração com **BestBuy API** para obtenção de peso de produtos.
- Integração com **OpenAI GPT** para estimar o peso com base na descrição de imagens.
- Integração com **Google Cloud Vision** para obter informações de descrição de imagens.
- Cálculo de peso médio a partir de múltiplas fontes.
- Retorno dos dados em formato JSON, preservando a ordem dos campos.

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Framework**: Flask
- **APIs**: OpenAI GPT, BestBuy, Google Cloud Vision
- **Bibliotecas**:
  - `requests`: Para fazer requisições HTTP.
  - `openai`: Para integração com a API GPT.
  - `google-cloud-vision`: Para integração com a API Google Vision.
  - `pandas`: Para manipulação de dados (opcional, se houver).
  - `python-dotenv`: Para carregar variáveis de ambiente.
  - `pytest`: Para testes unitários.

## Instalação

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/product-weight-estimator.git
cd product-weight-estimator
```

### 2. Criar e Ativar um Ambiente Virtual

Para Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Para Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

Instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

### 4. Definir Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto e adicione suas chaves de API, conforme necessário:

```bash
OPENAI_API_KEY=your_openai_key
BESTBUY_API_KEY=your_bestbuy_key
GOOGLE_APPLICATION_CREDENTIALS=path_to_google_credentials.json
```

### 5. Executar o Servidor

Após configurar as variáveis de ambiente, execute o servidor Flask:

```bash
python run.py
```

O servidor rodará por padrão em http://localhost:5000.