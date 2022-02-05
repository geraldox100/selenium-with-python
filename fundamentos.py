from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv


def main():
    option = webdriver.ChromeOptions()
    # s = Service('/Users/geraldoferraz/Downloads/chromedriver')    
    # navegador = webdriver.Chrome(service=s, options=option)

    option.add_argument('headless')
    navegador = webdriver.Remote('http://selenium-chrome:4444/wd/hub', options=option)
    

    acoes = ['MGLU3', 'LREN3', 'BBAS3', 'ITSA4']

    try:
        with open('/tmp/acoes.csv', 'w', newline='') as csvfile:
            cabecalho = ['valor_atual', 'min', 'max', 'yield', 'valorizacao']
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=cabecalho)
            writer.writeheader()

            for acao in acoes:
                navegador.get(f"https://fundamentus.com.br/detalhes.php?papel={acao}")
                xpath_valor_atual = '/html/body/div[1]/div[2]/table[1]/tbody/tr[1]/td[4]/span'
                xpath_min = '/html/body/div[1]/div[2]/table[1]/tbody/tr[3]/td[4]/span'
                xpath_max = '/html/body/div[1]/div[2]/table[1]/tbody/tr[4]/td[4]/span'
                xpath_yield = '/html/body/div[1]/div[2]/table[3]/tbody/tr[9]/td[4]/span'
                xpath_valorizacao = '/html/body/div[1]/div[2]/table[3]/tbody/tr[2]/td[2]/span/font'

                valor_atual = navegador.find_element(By.XPATH, xpath_valor_atual).text
                min = navegador.find_element(By.XPATH, xpath_min).text
                max = navegador.find_element(By.XPATH, xpath_max).text
                _yield = navegador.find_element(By.XPATH, xpath_yield).text
                valorizacao = navegador.find_element(By.XPATH, xpath_valorizacao).text

                writer.writerow({'valor_atual': valor_atual, 'min': min, 'max': max, 'yield': _yield, 'valorizacao': valorizacao})
    finally:
        navegador.close()


if __name__ == '__main__':
    main()
