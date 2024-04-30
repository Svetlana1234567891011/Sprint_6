from pages.order_page import OrderPage
from utils.path import PATH
from time import sleep
import allure


class TestOrdersRedirect:
    @allure.description('Клик по лого Яндекса')
    def test_check_orders_page_to_yandex_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_yandex_logo()
        page.wait_for_new_tab_opened()
        page.switch_to_new_tab(driver.window_handles[1])
        sleep(3)
        assert 'dzen' in driver.current_url

    @allure.description('Клик по лого Самоката')
    def test_check_orders_page_to_scooter_redirect(self, driver):
        page = OrderPage(driver)
        page.open_order_page()
        page.click_scooter_logo()
        assert driver.current_url == PATH.MAIN_PAGE_URL
