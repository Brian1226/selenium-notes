from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MiscTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://the-internet.herokuapp.com/login')  
        
        driver.maximize_window() 

        print(driver.find_element(By.XPATH, "//h2[normalize-space()='Login Page']").text)

        attr_value = driver.find_element(By.CLASS_NAME, 'radius').get_attribute('type')
        print(attr_value)

        button_enabled = driver.find_element(By.CLASS_NAME, 'radius').is_enabled()
        print(button_enabled)

        button_displayed = driver.find_element(By.CLASS_NAME, 'radius').is_displayed()
        print(button_displayed)

        print(driver.current_url)
        print(driver.title)
        driver.back()
        driver.forward()
        driver.refresh()

        driver.quit()

demo = MiscTest()
demo.test()
