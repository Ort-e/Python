from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


def third_image_src_loaded(driver):
    images = driver.find_elements(By.TAG_NAME, "img")
    if len(images) >= 4:
        src = images[3].get_attribute("src")
        if src:
            return src
    return False


third_image_src = WebDriverWait(driver, 10).until(third_image_src_loaded)

print("Значение атрибута src у 3-й картинки:", third_image_src)


driver.quit()
