from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Page Object страницы медленного калькулятора.
    Позволяет выполнять операции и получать результат вычисления.
    """

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: WebDriver — экземпляр браузера Selenium
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def button(self, text: str) -> tuple:
        """
        Возвращает локатор кнопки калькулятора по тексту.

        :param text: str — текст кнопки
        :return: tuple — локатор Selenium (By, value)
        """
        return (By.XPATH, f"//span[text()='{text}']")

    def open(self) -> None:
        """
        Открывает страницу калькулятора.

        :return: None
        """
        self.driver.get(self.URL)

    def set_delay(self, value: int) -> None:
        """
        Устанавливает задержку вычисления.

        :param value: int — значение задержки в секундах
        :return: None
        """
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(value))

    def press(self, value: str) -> None:
        """
        Нажимает кнопку калькулятора.

        :param value: str — значение кнопки
        :return: None
        """
        self.driver.find_element(*self.button(value)).click()

    def calculate(self) -> None:
        """
        Нажимает кнопку "=" для вычисления.

        :return: None
        """
        self.press("=")

    def get_result(self) -> str:
        """
        Получает результат вычисления.

        :return: str — результат вычисления на экране калькулятора
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, "15")
        )
        return self.driver.find_element(*self.RESULT).text
