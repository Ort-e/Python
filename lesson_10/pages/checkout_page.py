from selenium.webdriver.common.by import By


class CheckoutPage:
    """
    Page Object страницы оформления заказа.
    """

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver — экземпляр браузера Selenium
        """
        self.driver = driver

    def fill_personal_info(
         self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Заполняет персональные данные покупателя.

        :param first_name: str — имя
        :param last_name: str — фамилия
        :param postal_code: str — почтовый индекс
        :return: None
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_amount(self) -> str:
        """
        Получает итоговую сумму заказа.

        :return: str — итоговая сумма заказа
        """
        return self.driver.find_element(*self.TOTAL).text
