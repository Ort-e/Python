import allure
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@allure.title("Проверка работы медленного калькулятора")
@allure.description("Тест проверяет корректность вычисления 7 + 8")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Ввести выражение 7 + 8"):
            page.press("7")
            page.press("+")
            page.press("8")

        with allure.step("Нажать кнопку вычисления"):
            page.calculate()

        with allure.step("Получить результат"):
            result = page.get_result()

        with allure.step("Проверить результат"):
            assert result == "15", f"Ожидали 15, но получили {result}"

    finally:
        driver.quit()
