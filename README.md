# GEERS AI - Introducción a la Inteligencia Artificial

En este repositorio van a encontrar los diferentes pasos que vamos a seguir en 
este primer encuentro sobre Inteligencia Artificial. El objetivo es comenzar a 
familiarizarnos con algunas de las herramientas que hoy se utilizan en el 
desarrollo de aplicaciones, de una forma amigable, ya que hay mucho para 
aprender y no siempre es fácil encontrar un punto de partida.

## Pre-requisitos - Tiempo estimado: TBD

Debemos tener pre-instaladas las siguientes herramientas:

0. git
1. python@3.10
2. pip@22.3.1
3. Visual Studio Code (VSCode) con las siguientes extensiones:
    1. autopep8 para formatear el codigo
    2. Github Copilot para sugerencias de codigo
    3. Python para la sintaxis de python
    4. Pylance para el linter de python
    5. Jupyter para experimentar con notebooks (opcional)

Setup del entorno:

```bash
git clone ${url_del_repositorio}
pip install -r requirements.txt
code .
```

Definición de la API Key de OpenAI:

```bash
echo "OPENAI_API_KEY=<your-key>" > .env
```

## Data preparation

En esta primera etapa, vamos a utilizar un dataset de Kaggle, que contiene 
información de peliculas. 

El dataset original se encuentra en este enlace:
https://www.kaggle.com/datasets/joebeachcapital/top-10000-most-popular-movies-from-imdb

Pueden encontrar mas información acerca de esta fase en el siguiente enlace:
https://www.techtarget.com/searchbusinessanalytics/definition/data-preparation

### CSV and Pandas - Tiempo estimado: TBD

Comenzamos por familiarizarnos con el dataset y como manipularlo utilizando 
pandas: 

1. https://pandas.pydata.org/docs/user_guide/10min.html
2. https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

En este archivo encontraras un ejemplo basico para comenzar:

```bash
python steps/data-preparation/combine_columns.py
```

### Tiktoken - Tiempo estimado: TBD

Experimentamos con la libreria Tiktok, como para comenzar a familiarizarnos con
la traducción texto => tokens.

1. [Byte pair encoding (BPE)](https://github.com/openai/tiktoken#what-is-bpe-anyway)

Jugamos en la consola para ver que nos devuelve:

```bash
python steps/tokenizers/use_tiktoken.py
```

Ahora pre-procesamos el dataset para obtener los tokens:

```bash
python steps/data-preparation/compute_tokens.py
```

### Embedding - Tiempo estimado: TBD

Comenzamos a procesar los embeddings (vectores de 1516 dimensiones) utilizando 
el modelo de openai `text-embedding-ada-002`:

1. https://platform.openai.com/docs/guides/embeddings/what-are-embeddings

```bash
python steps/data-preparation/compute_embedding.py
```

## Base de datos vectoriales - Tiempo estimado: TBD

Ahora vamos a adentrarnos en la ultilización de bases de datos vectoriales, en
particular para este ejemplo, vamos a utilizar ChromaDB que es un wrapper sobre
SQLite:

1. https://www.trychroma.com/

```bash
python steps/vector-db/load-database.py
```

## LangChain

Nos metemos de lleno ahora en el uso de LangChain, que es una libreria que
permite integrar LLMs (Language Models) de forma sencilla en nuestras 
aplicaciones, pero al mismo tiempo intenta crear un ecosistema de herramientas
que nos permitan experimentar con diferentes aspectos de la Inteligencia
Artificial.

1. https://python.langchain.com/docs/get_started/introduction.html


### Prompts - Tiempo estimado: TBD

Como representamos los prompts en LangChain?

1. https://www.promptingguide.ai

```bash
python steps/langchain/prompts/prompt-templates.py
```

```bash
python steps/langchain/prompts/prompt-fstring.py
```

```bash
python steps/langchain/prompts/prompt-yaml.py
```

```bash
python steps/langchain/prompts/prompt-composition.py
```

### Memory - Tiempo estimado: TBD

Como le damos memoria?

```bash
python steps/langchain/memory/conversarion-buffer.py
```

### Retrieval - Tiempo estimado: TBD

Como obtenemos información adicional a la utilizada en el entrenamiento de los 
modelos third-party?

```bash
python steps/langchain/retrieval/web-retrieval.py
```

```bash
python steps/langchain/retrieval/vector-retrieval.py
```

### Agents - Tiempo estimado: TBD

Como utilizamos LangChain para crear agentes conversacionales? 

Esta ultima etapa se focaliza en la integración de todo lo que hemos visto hasta
ahora para crear un bot que pueda realizar tareas especificas.

```bash
python steps/langchain/agent/hugo-v0.py
```

```bash
python steps/langchain/agent/hugo-v1.py
```
