from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_total_price_saucedemo():
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_product_to_cart("Sauce Labs Backpack")
        inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_product_to_cart("Sauce Labs Onesie")

        inventory_page.go_to_cart()
        cart_page.click_checkout()

        checkout_page.fill_personal_info(
            first_name="Ivan",
            last_name="Ivanov",
            postal_code="12345"
        )

        total = checkout_page.get_total_amount()

        assert total == "Total: $58.29", f"Ожидали $58.29, но получили {total}"

    finally:
        driver.quit()
