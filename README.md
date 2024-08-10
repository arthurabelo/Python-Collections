# Relatório Técnico: Análise de Estruturas de Dados

Este projeto é uma atividade de Estrutura de Dados realizada na Universidade Federal do Piauí (UFPI) por Arthur Rabelo de Carvalho. O objetivo é analisar o tempo de inserção, consulta e deleção de palavras nas classes do módulo `collections` do Python.

## 📋 Sumário

- [Introdução](#introdução)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Resultados](#resultados)
- [Licença](#licença)

## Introdução

Este projeto visa medir o desempenho de diferentes estruturas de dados fornecidas pelo módulo `collections` do Python. As estruturas analisadas incluem `dict`, `list`, `set`, `tuple`, `namedtuple`, `defaultdict`, `Counter`, `OrderedDict`, `deque`, `ChainMap`, `UserDict`, `UserList` e `UserString`.

## Instalação

Para executar este projeto, siga os passos abaixo:

- Clone o repositório:
    ```sh
    git clone https://github.com/arthurabelo/Python-Collections.git
    ```

## Uso

### Tratamento do Arquivo

1. Clique em `Tratar arquivo` para tratar o arquivo `leipzig100k.txt`

Esta ação irá gerar um arquivo [`leipzig100k_tratado.txt`] com as palavras tratadas.

### Seleção da questão

2. Clique nos menus disponíveis para escolher a questão que será gerado o gráfico correspondente. A descrição das questões está disponível no arquivo `Trabalho FInal - Python Collections.pdf`

### Construção do Gráfico

3. Clique em `Mostrar Resultado` para construir o gráfico de análise de tempo:
    Esta ação irá medir o tempo de inserção para cada estrutura de dados e retornar os resultados em um gráfico.

## Estrutura do Projeto

```plaintext
App.py
Containers.py
Grafico.py
```

App.py: Script para tratar o arquivo de entrada e implementar interface gráfica
Containers.py: Implementação das funções de inserção para diferentes estruturas de dados.
Grafico.py: Script para medir o tempo de inserção e construir o gráfico.
leipzig100k.txt: Arquivo de entrada com as palavras a serem analisadas.
leipzig100k_tratado.txt: Arquivo de saída com as palavras tratadas. Foi criado esse método para facilitar a execução em menos tempo e evitar sobrecarga desnecessária.
## Resultados
Os resultados da análise de tempo serão exibidos no console após a execução do script Grafico.py. Eles incluem o tempo de inserção para cada estrutura de dados.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

- Arthur Rabelo de Carvalho - Universidade Federal do Piauí (UFPI) 📚