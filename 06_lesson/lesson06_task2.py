from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput?")
weit = WebDriverWait(driver, 4)


input_fiel = weit.until(
    EC.visibility_of_element_located((By.ID, "newButtonName"))
)
input_fiel.clear()
input_fiel.send_keys("SkyPro")

button = weit.until(
    EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
button.click()

button_text = button.text
print(button_text)

driver.quit
