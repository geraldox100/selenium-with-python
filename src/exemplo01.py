from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from src.util import get_browser
from selenium.webdriver.common.by import By
import time

def main():
    acao = 'MGLU3'
    url = f"https://statusinvest.com.br/acoes/{acao}"

    navegador = get_browser()
    navegador.get(url)

    try:
        xpath_valor_atual = '/html/body/main/div[2]/div/div[1]/div/div[1]/div/div[1]/strong'
        xpath_min = '/html/body/main/div[2]/div/div[1]/div/div[2]/div/div[1]/strong'
        xpath_max = '/html/body/main/div[2]/div/div[1]/div/div[3]/div/div[1]/strong'
        xpath_yield = '/html/body/main/div[2]/div/div[1]/div/div[4]/div/div[1]/strong'
        xpath_valorizacao = '/html/body/main/div[2]/div/div[1]/div/div[5]/div/div[1]/strong'

        valor_atual = navegador.find_element(By.XPATH, xpath_valor_atual).text
        min = navegador.find_element(By.XPATH, xpath_min).text
        max = navegador.find_element(By.XPATH, xpath_max).text
        _yield = navegador.find_element(By.XPATH, xpath_yield).text
        valorizacao = navegador.find_element(By.XPATH, xpath_valorizacao).text

        print(f'valor atual={valor_atual}, min={min}, max={max}, min={_yield}, min={valorizacao} ')
    finally:
        navegador.close()


if __name__ == '__main__':
    main()