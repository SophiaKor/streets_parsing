from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from typing import Optional

from config import STREETS, NUMBERS


class Parsing:
    """ Парсинг улиц городов с использованием драйвера селениум. """

    def __init__(self):
        self.driver: Optional[webdriver.Firefox] = None

    def setup_driver(self):
        """ Запуск драйвера. """
        if self.driver is None:
            options = Options()
            options.add_argument('--headless')
            # windows
            # self.driver = webdriver.Firefox(executable_path=r'*\geckodriver.exe', options=options)
            # linux
            # self.driver = webdriver.Firefox('*/geckodriver')

    def close_driver(self):
        """ Остановка драйвера. """
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    def get_urls_for_one_city(self, _url):
        """ Получение количества страниц и url страниц для одного города. """
        self.driver.get(_url)
        wait = WebDriverWait(self.driver, 10)
        urls = [_url]
        list_of_urls = []

        try:
            pages = wait.until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, NUMBERS)
                )
            )
            list_of_urls.extend(pages.text.split("\n"))
        except:
            pass

        if len(list_of_urls) > 1:
            for page in range(int(list_of_urls[- 1]) - 1):
                urls.append(f'{_url}stranica-{page + 2}/')

        return urls

    def handle_query(self, urls, file_name):
        """ Выполнение запросов на все страницы одного города и
        запись названий улиц в файл txt.
        """
        with open(f'{file_name}.txt', 'w') as file:
            for url in urls:
                self.driver.get(url)
                wait = WebDriverWait(self.driver, 10)
                web_element = wait.until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, STREETS)
                    )
                )
                file.writelines(web_element.text)
                file.writelines('\n')
