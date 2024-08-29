from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MouseClicksTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/buttons')

        actions = ActionChains(driver)
        # right click
        right_click_btn = driver.find_element(By.ID, 'rightClickBtn')
        actions.context_click(right_click_btn).perform()

        # double click
        double_click_btn = driver.find_element(By.ID, 'doubleClickBtn')
        actions.double_click(double_click_btn).perform()

        driver.quit()

demo = MouseClicksTest()
demo.test()
