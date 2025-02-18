import time
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from citilink_tests.Base.base import Base


class checkout_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://www.citilink.ru/"  # URL тестируемого сайта

    # Locators
    Firstname = '//input[@placeholder="Введите ваше имя"]'
    Secondname = '//input[@placeholder="Введите вашу фамилию"]'
    tel_number = '//input[@placeholder="+7"]'
    choosepvz_button = '//button[@class="e4uhfkv0 css-1w7mt1x e4mggex0"]'
    choose_store_string = '//input[@placeholder="Поиск по магазинам"]'
    choose_store_button = '//button[@data-meta-name="SelfDeliveryStoresList__select-button"]'
    email = '//input[@placeholder="Введите ваш e-mail"]'
    confirm_checkbox = '//label[@class="e1tts2c20 css-j0vyvu e1cseun00"]'
    submit_button = '//button[@data-meta-name="SubmitButton"]'

    # Getters
    def get_Firstname(self):
        """ Строка для ввода имени"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.Firstname)))

    def get_Secondname(self):
        """ Строка для ввода Secondname"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.Secondname)))

    def get_tel_number(self):
        """ Строка для ввода tel_number"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.tel_number)))

    def get_choosepvz_button(self):
        """ выбор пвз"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.choosepvz_button)))

    def get_choose_store_string(self):
        """ Строка для выбора магазина"""
        time.sleep(3)
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.choose_store_string)))

    def get_choose_store_button(self):
        """ кнопка выбора пвз"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.choose_store_button)))

    def get_confirm_checkbox(self):
        """подтверждение данных"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_checkbox)))

    def get_submit_button(self):
        """оформление покупки"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    def get_email(self):
        """ Строка для ввода email"""
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.email)))



    # Actions
    def add_firstname(self, fname):
        """ ввести имя """
        self.get_Firstname().send_keys(fname)

    def add_secondname(self, sname):
        """ ввести secondname """
        self.get_Secondname().send_keys(sname)

    def add_telephone(self, number):
        """ввести телефон"""
        self.get_tel_number().send_keys(number)

    def click_on_pvz_button(self):
        """перейти к выбору пвз"""
        self.get_choosepvz_button().click()

    def choose_store(self, storename):
        """выбрать магазин"""
        self.get_choose_store_string().send_keys(storename)

    def confirm_store(self):
        """подтвердить выбор магазина"""
        time.sleep(2)
        self.get_choose_store_button().click()

    def add_email(self, mailstring):
        """написать имейл"""
        self.get_email().send_keys(mailstring)

    def confirm_id(self):
        """подтвердить данные"""
        self.get_confirm_checkbox().click()

    def confirm_buy(self):
        """Подтвердить покупку"""
        time.sleep(3)
        self.get_submit_button().click()


    # Methods
    def write_customer_id_and_finalize_buying(self, fname, sname, tnumbe, store, email):
        """ заполняем данные покупателя и оформляем покупку"""
        self.add_firstname(fname)
        self.add_secondname(sname)
        self.add_telephone(tnumbe)
        self.click_on_pvz_button()
        self.choose_store(store)
        self.confirm_store()
        self.add_email(email)
        self.confirm_id()
        self.confirm_buy()





