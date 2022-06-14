from selenium import webdriver
from pyautogui import press

numero_repeticoes = int(input("Quantas vezes você que recarregar a página? "))

site = input("Qual site você quer acessar? ")

navegador = webdriver.Chrome()

navegador.get(site)

for _ in range(numero_repeticoes):
    press("F5")