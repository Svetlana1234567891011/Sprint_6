from pages.base_page import BasePage
from utils.locators import MainPageLocators
from utils.path import PATH
import allure


class MainPageService(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.open_page(PATH.MAIN_PAGE_URL)

    @allure.step('Загружаем')
    def wait_for_main_page(self):
        self.wait_for_top_load(MainPageLocators.MAIN_PAGE_TOP)

    @allure.step('Скролл до секции вопросов')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.SUBSECTION_TOP)

    @allure.step('Локатор для кнопки "Заказать" зависит от расположения: {position}')
    def click_order_button(self, position):
        if position == 'top':
            return self.click_element(MainPageLocators.TOP_ORDER_BUTTON)
        elif position == 'bottom':
            return self.scroll_to_element_and_click(MainPageLocators.BOTTOM_ORDER_BUTTON)
        else:
            return f'Button position {position} is not allowed'

