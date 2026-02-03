from selenium.webdriver.common.by import By


class InventoryPage:
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_name: str):
        xpath = (
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()
