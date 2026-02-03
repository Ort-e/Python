from selenium import webdriver
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = CalculatorPage(driver)

        page.open()
        page.set_delay(45)

        page.press("7")
        page.press("+")
        page.press("8")
        page.calculate()

        result = page.get_result()

        assert result == "15", f"Ожидали 15, но получили {result}"

    finally:
        driver.quit()
