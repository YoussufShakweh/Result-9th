from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException


def main() -> None:
    # Enter The Student Number
    std_num = input("Enter Your Number: ")

    url = "http://moed.gov.sy/9th/index.php"
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
    driver.find_element(By.ID, "submit").click()

    input("Press to close ...")

    driver.quit()


if __name__ == '__main__':
    main()
