from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MouseHoverTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/menu')
        driver.maximize_window()

        actions = ActionChains(driver)
        main_item = driver.find_element(By.XPATH, "//a[normalize-space()='Main Item 2']")
        sub_item = driver.find_element(By.XPATH, "//a[normalize-space()='SUB SUB LIST »']")
        # hover mouse to main item and then sub item on menu
        actions.move_to_element(main_item).move_to_element(sub_item).perform()
        
        driver.quit()

demo = MouseHoverTest()
demo.test()
