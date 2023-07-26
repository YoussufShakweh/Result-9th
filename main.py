from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException

# Enter The Student Number
std_num = input("Enter Your Number: ")

url = "https://www.bakaloriasyria.com/2023/07/asasy-result.html?fbclid=IwAR0IC55pDJ78C_T7qkK20kgcwtE0kAphxdxMSqML9nlUaJTpfMYq6f_t2t4"
driver = webdriver.Edge()

while True:
  try: 
    driver.get(url)
    break
  except WebDriverException:
    driver.refresh()

# Find Selection Webelement "Branch" and Select Basic Branch
Select(driver.find_element(By.ID, "branch")).select_by_value("1")

# Find Selection Webelement "City" and Select Hama
Select(driver.find_element(By.ID, "city")).select_by_value("7")

# Find Webelement "stdnum" and Fill It
driver.find_element(By.ID, "stdnum").send_keys(std_num)

# Find Webelement "Submit" and Click It
driver.find_element(By.LINK_TEXT, "ابدأ البحث").click()

input("Press to close ...")

driver.quit()
