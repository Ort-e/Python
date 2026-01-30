from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_total_price():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 4)

    driver.get("https://www.saucedemo.com")

    wait.until(
        EC.visibility_of_element_located((
            By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie",
    ]

    for products_id in products:
        wait.until(
            EC.visibility_of_element_located((By.ID, products_id))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_container").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(
        EC.visibility_of_element_located((
            By.ID, "first-name"))).send_keys("Ilya")
    driver.find_element(By.ID, "last-name").send_keys("Frolov")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(
        EC.visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label"))
    ).text

    total_price = total_text.replace("Total: ", "")

    assert total_price == "$58.29"

    driver.quit()
