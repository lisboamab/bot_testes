from selenium import webdriver
from pyautogui import press

navegador = webdriver.Chrome()

navegador.get("https://dc-full-stack.github.io/Site-da-Turma/pages/modulo01.html")

for _ in range(1000):
    press('F5')