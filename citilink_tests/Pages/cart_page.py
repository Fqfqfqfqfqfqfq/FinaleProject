import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from citilink_tests.Base.base import Base


class cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.citilink.ru/"  # URL тестируемого сайта

    # Locators
    item_plus_button = '//button[@class="css-1k94dyf e1x2u7fl1"][2]'
    customer_choice = '//div[@class="css-j7qwjs e63z2z20"]/div[2]/span'
    go_to_buy_button = '//button[@title="Перейти к оформлению"]'
    continue_as_guest_button = '//div[@class="css-xs89nv efjk8v20"]/button'



    # Getters
    def get_item_plus_button(self):
        """ добавить еще один товар"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.item_plus_button)))

    def get_customer_choice(self):
        """ текущий список включенного в корзину"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.customer_choice)))

    def get_go_to_buy_button(self):
        """ Перейти к оформлению"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_buy_button)))

    def get_continue_as_guest_button(self):
        """ Перейти к оформлению"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_as_guest_button)))



    # Actions
    def click_item_plus_button(self):
        """ нажать на + товар """
        self.get_item_plus_button().click()
        time.sleep(5)

    def check_cart_info(self, text):
        """сравниваем текстовые значения в корзине"""
        try:
            checking_text = self.get_customer_choice().text
            assert text == checking_text
            print("текст совпадает!")
        except Exception as e:
            print(f"⚠ Ошибка: Текст не совпадает")

    def click_on_go_to_buy_button(self):
        """ нажать на перейти к оформлению"""
        self.get_go_to_buy_button().click()

    def click_on_continue_as_guest_button(self):
        """ нажать на продолжить как гость"""
        self.get_continue_as_guest_button().click()

    # Methods
    def add_1plus_and_go_to_checkout(self,text_for_check):
        """ добавить настройку смарт тв и перейти к оформлению"""
        self.click_item_plus_button()
        self.check_cart_info(text_for_check)
        self.click_on_go_to_buy_button()
        self.click_on_continue_as_guest_button()

