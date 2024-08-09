import pyautogui
import pyperclip
import webbrowser
import time
import yfinance
from time import sleep


ticker =  input("Digite o código da ação desejada: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd):")
dt_final = input("Digite a data final(aaaa-mm-dd):")

dados = yfinance.Ticker(ticker)
tabela = dados.history(start=dt_inicial, end=dt_final)
print(tabela)

fechamento = tabela['Close']
print(fechamento)
fechamento.plot()

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio= round(fechamento.mean(), 2)

print(maxima)
print(minima)
print(valor_medio)

destinatario = "atenasestudo@gmail.com"
assunto = "Análises das ações"

mensagem = f"""
Prezado gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!
Atte.
"""

webbrowser.open("www.gmail.com")
time.sleep(10)

pyautogui.PAUSE = 3

pyautogui.click(x=38, y=166)

pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyautogui.click(x=778, y=689)

pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso!")