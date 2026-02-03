from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    DELAY_INPUT = (By.ID, "delay")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def button(self, text):
        return (By.XPATH, f"//span[text()='{text}']")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value: int):
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(value))

    def press(self, value: str):
        self.driver.find_element(*self.button(value)).click()

    def calculate(self):
        self.press("=")

    def get_result(self) -> str:
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT, "15")
        )
        return self.driver.find_element(*self.RESULT).text
