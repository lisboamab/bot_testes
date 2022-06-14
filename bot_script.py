from selenium import webdriver
from pyautogui import press

numero_de_recargas = int(input("Digite o número de vezes que você quer recarregar: "))

site = input("Digite o site desejado ")

navegador = webdriver.Chrome()

navegador.get(site)

for _ in range(numero_de_recargas):
    press('F5')