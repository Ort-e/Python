import allure
from selenium import webdriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Проверка итоговой стоимости заказа")
@allure.description(
    "Тест проверяет корректность подсчета общей стоимости товаров")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_total_price_saucedemo():

    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть сайт"):
            login_page.open()

        with allure.step("Авторизоваться"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить товары в корзину"):
            inventory_page.add_product_to_cart("Sauce Labs Backpack")
            inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
            inventory_page.add_product_to_cart("Sauce Labs Onesie")

        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()

        with allure.step("Перейти к оформлению"):
            cart_page.click_checkout()

        with allure.step("Заполнить данные покупателя"):
            checkout_page.fill_personal_info(
                "Ivan",
                "Ivanov",
                "12345"
            )

        with allure.step("Получить итоговую стоимость"):
            total = checkout_page.get_total_amount()

        with allure.step("Проверить итоговую стоимость"):
            assert total == "Total: $58.29", (
                f"Ожидали $58.29, но получили {total}")

    finally:
        driver.quit()
