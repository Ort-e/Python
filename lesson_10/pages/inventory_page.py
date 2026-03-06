from selenium.webdriver.common.by import By


class InventoryPage:
    """
    Page Object страницы каталога товаров.
    Позволяет добавлять товары в корзину и переходить в корзину.
    """

    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """
        Инициализация страницы каталога.

        :param driver: WebDriver — экземпляр браузера Selenium
        """
        self.driver = driver

    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по названию.

        :param product_name: str — название товара
        :return: None
        """
        xpath = (
            f"//div[text()='{product_name}']"
            f"/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        self.driver.find_element(*self.CART_BUTTON).click()
