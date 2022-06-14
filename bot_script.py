from selenium import webdriver
from pyautogui import press

navegador = webdriver.Chrome()

navegador.get(input("Digite o site desejado "))

numero_de_recargas = int(input("Digite o número de vezes que você quer recarregar: "))

for _ in range():
    press('F5')