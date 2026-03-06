from selenium.webdriver.common.by import By


class CartPage:
    """
    Page Object страницы корзины.
    Позволяет просматривать товары и переходить к оформлению заказа.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver — экземпляр браузера Selenium
        """
        self.driver = driver

    def get_cart_items(self) -> list[str]:
        """
        Получает список товаров в корзине.

        :return: list[str] — список названий товаров
        """
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.

        :return: None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
