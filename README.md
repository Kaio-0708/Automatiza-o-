# Análise de Ações com Python

Este projeto em Python permite a análise de ações de uma empresa utilizando a biblioteca `yfinance` para buscar dados históricos de preços. O programa calcula a cotação máxima, mínima e o valor médio das ações dentro de um período especificado e envia um e-mail com os resultados para um destinatário predefinido.

## Funcionalidades

- **Consulta de dados históricos**: Busca os dados de uma ação específica em um intervalo de datas definido pelo usuário.
- **Cálculo de indicadores**: Calcula a cotação máxima, mínima e o valor médio das ações no período consultado.
- **Geração de gráfico**: Exibe um gráfico da evolução da cotação de fechamento das ações no período.
- **Envio automático de e-mail**: Envia os resultados da análise por e-mail utilizando as bibliotecas `pyautogui`, `pyperclip`, e `webbrowser`.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `yfinance`
  - `pyautogui`
  - `pyperclip`
  - `matplotlib`
 
## Autor

Kaio Vitor - [GitHub](https://github.com/Kaio-0708)
