import time
from selenium import webdriver
from citilink_tests.Pages.cart_page import cart_page
from citilink_tests.Pages.item_list_page import item_list_page
from citilink_tests.Pages.main_page import main_page
from citilink_tests.Pages.checkout_page import checkout_page


def buy_tv():
    driver = webdriver.Chrome()
    main = main_page(driver)
    main.open_Popular_category3_page()
    item = item_list_page(driver)
    item.add_item_to_cart(10000, 30000)
    cart = cart_page(driver)
    cart.add_1plus_and_go_to_checkout("2 товара")
    checkout = checkout_page(driver)
    checkout.write_customer_id_and_finalize_buying("Вася","Васильев","9992223344","Тимирязевский", "123pass@inpass.com")
    time.sleep(3)
    checkout.get_screenshot()
buy_tv()

