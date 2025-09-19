# Imports de libs
import pyautogui
import time
import pandas


time_inicio = time.time()
pyautogui.PAUSE = 1 # Define uma pausa de 5 segundos para cada ação

# Acessa o site
pyautogui.press('win') # Abre o menu do windows
pyautogui.write('comet') # Digita comet no menu de pesquisa de programas.
pyautogui.press('enter') # Pressiona o enter
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') # Escreve a url na barra de pesquisa
pyautogui.press('enter') # Pressiona enter para entrar no site
time.sleep(5) # Espera 5 segundos

# Faz login
pyautogui.click(868,398)
pyautogui.write('matheus.rj25@hotmail.com')
pyautogui.press('tab')
pyautogui.write('123')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

# Importar a base de dados
tabela = pandas.read_csv('./data/produtos.csv')

for linha in tabela.index:

    pyautogui.click(929,280)
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')
    marca = tabela.loc[linha,"marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    preco_unitario = tabela.loc[linha,"preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    custo = tabela.loc[linha,"custo"]
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    obs = str(tabela.loc[linha,"obs"])
    print(obs)
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.scroll(10000)

pyautogui.hotkey('win','d')
time_fim = time.time()
tempo_execucao = time_fim - time_inicio
print("Tempo de execução:", tempo_execucao, " segundos")
# 88 minutos