from selenium import webdriver
from pyautogui import press

navegador = webdriver.Chrome()

site = input("Digite o site desejado ")

navegador.get(site)

numero_de_recargas = int(input("Digite o número de vezes que você quer recarregar: "))

for _ in range(numero_de_recargas):
    press('F5')