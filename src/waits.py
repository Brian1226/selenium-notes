from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/radio-button')

        # implicit wait
        # driver.implicitly_wait(5)

        # explicit wait
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Yes']"))).click()

        # fluent wait
        # wait = WebDriverWait(driver, 5, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException])
        # wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Yes']"))).click()

        driver.quit()

demo = WaitsTest()
demo.test()
