from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from citilink_tests.Base.base import Base


class main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.citilink.ru/"  # URL тестируемого сайта

    # Locators
    Popular_category3 = '//*[@class="app-catalog-0 e456v710"]/div[1]/a[3]'

    # Getters
    def get_Popular_category3(self):
        """ Третий вариант из товаров популярных категорий"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.Popular_category3)))


    # Actions
    def click_on_Popular_category3(self):
        """ Переходим на страницу третьего по популярности товара """
        self.get_Popular_category3().click()


    # Methods
    def open_Popular_category3_page(self):
        """ Процесс покупки товара """
        self.driver.get(self.url)  # Открытие страницы Citilink
        self.driver.maximize_window()  # Разворачиваем окно браузера
        self.click_on_Popular_category3()

