from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src import config

def get_browser():
    browser = None
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    if config.ENV == 'DEV':
        s = Service(config.DRIVER_DIR)
        browser = webdriver.Chrome(service=s, options=option)
    else:
        browser = webdriver.Remote(config.REMOTE_BROWSER_URL, options=option)
        if not browser:
            raise Exception(f"Browser não encontrado para URL Remtota={config.REMOTE_BROWSER_URL}")
    return browser