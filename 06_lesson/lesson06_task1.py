from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")


driver.find_element(By.ID, "ajaxButton").click()


green_label = WebDriverWait(driver, 16).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

txt = green_label.text

print(txt)


driver.quit()
