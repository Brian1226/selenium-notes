from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class AlertsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/alerts')

        # send keys and accept
        driver.find_element(By.ID, 'promtButton').click()
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys('Brian')
        driver.switch_to.alert.accept()

        #send keys and dismiss
        driver.find_element(By.ID, 'promtButton').click()
        driver.switch_to.alert.send_keys('Nguyen')
        driver.switch_to.alert.dismiss()
        
        driver.quit()

demo = AlertsTest()
demo.test()
