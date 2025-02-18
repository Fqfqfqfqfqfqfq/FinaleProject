import datetime
import os

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        """Открытие страницы"""
        self.driver.get(url)

    def get_screenshot(self):
        """For screenshots"""
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d_%H.%M.%S")  # Исправлено
        name_screenshot = f"scr_{now_date}.png"
        # Получаем путь к папке проекта
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screenshot_path = os.path.join(base_dir, "Screen", name_screenshot)  # Корректный путь
        # Делаем скриншот
        self.driver.save_screenshot(screenshot_path)
        print("сделан скрин")
        print(f"Путь сохранения скриншота: {screenshot_path}")

