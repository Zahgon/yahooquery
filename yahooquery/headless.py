# stdlib
from typing import Dict, List

# third party
from requests.cookies import RequestsCookieJar

try:
    # third party
    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
except ImportError:
    # Selenium was not installed
    has_selenium = False
else:
    has_selenium = True


class YahooFinanceHeadless:
    LOGIN_URL = "https://login.yahoo.com"

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.cookies = RequestsCookieJar()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--ignore-ssl-errors")
        chrome_options.set_capability("pageLoadStrategy", "eager")
        service = Service()
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def login(self):
        pass

    def _add_cookies_to_jar(self, cookies: List[Dict]):
        pass
