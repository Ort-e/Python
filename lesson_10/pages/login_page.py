from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object страницы авторизации сайта SauceDemo.
    Содержит методы для открытия страницы и выполнения входа в систему.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        :param driver: WebDriver — экземпляр браузера Selenium
        """
        self.driver = driver

    def open(self) -> None:
        """
        Открывает страницу авторизации.

        :return: None
        """
        self.driver.get(self.URL)

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию пользователя.

        :param username: str — имя пользователя
        :param password: str — пароль
        :return: None
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
