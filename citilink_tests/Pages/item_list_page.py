import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from citilink_tests.Base.base import Base


class item_list_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.citilink.ru/"  # URL тестируемого сайта

    # Locators
    Price_input_min = '//div[@data-meta-value="Цена"]/div[2]/div[1]/div[1]/input[1]'
    Price_input_max = '//div[@data-meta-value="Цена"]/div[2]/div[1]/div[1]/input[2]'
    cart_button_1 = '//div[@data-meta-name="ProductHorizontalSnippet"][1]/div[1]/div[2]/div[7]/div[3]'
    go_to_cart = '//div[@class="app-catalog-pf49b8 e1jliu4a0"]/a[1]'


    # Getters
    def get_Price_input_min(self):
        """ минимальная цена"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.Price_input_min)))
    def get_Price_input_max(self):
        """ максимальная цена"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.Price_input_max)))
    def get_cart_button_1(self):
        """ в корзину для 1го товара"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button_1)))
    def get_go_to_cart(self):
        """ Переходим в корзину"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))


    # Actions
    def chose_min_price(self, price):
        """ выбираем минимальную цену """
        self.get_Price_input_min().clear()
        self.get_Price_input_min().send_keys(price)
        self.get_Price_input_min().send_keys(Keys.ENTER)

    def chose_max_price(self, price):
        """ выбираем максимальную цену """
        self.get_Price_input_max().clear()
        self.get_Price_input_max().send_keys(price)
        self.get_Price_input_max().send_keys(Keys.ENTER)

    def item_to_cart(self):
        self.get_cart_button_1().click()

    def user_go_to_cart(self):
        self.get_go_to_cart().click()



    # Methods
    def add_item_to_cart(self,minprice,maxprice):
        """ добавить товар в определеном диапазоне цены в корзину и перейти в корзину"""
        self.chose_min_price(minprice)
        self.chose_max_price(maxprice)
        time.sleep(3)
        self.item_to_cart()
        self.user_go_to_cart()