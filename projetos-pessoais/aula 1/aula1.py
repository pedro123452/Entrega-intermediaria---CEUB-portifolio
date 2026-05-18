import pyautogui

import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.PAUSE = 0.7
# acessar o site
pyautogui.press('win')
pyautogui.write('google')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)  
#logar no site
pyautogui.click(x=989, y=496)  # clicar no campo de email
pyautogui.write("phciriacoo@gmail.com")
pyautogui.press('tab')
pyautogui.write("pedro2028")
pyautogui.press('tab')
pyautogui.press('enter')

pyautogui.sleep(4) 
#importar a biblioteca de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
pyautogui.sleep(0.6)
for linha in tabela.index:
    #cadastrar os produtos
    pyautogui.click(x=858, y=360)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')
    #preço unitário
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')
    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    #enviar
    pyautogui.press('enter')
    #voltar o inicio da página
    pyautogui.scroll(50000)