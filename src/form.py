from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class FormTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/automation-practice-form')

        # textbox
        driver.find_element(By.ID, 'firstName').send_keys('Brian')
        driver.find_element(By.ID, 'lastName').send_keys('Nguyen')
        driver.find_element(By.ID, 'userEmail').send_keys('test_email89@gmail.com')
        driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__value-container.subjects-auto-complete__value-container--is-multi.css-1hwfws3').send_keys('Math') 
        driver.find_element(By.ID, 'currentAddress').send_keys('123 Fake Street')
        
        # checkbox
        driver.find_element(By.XPATH, "//label[normalize-space()='Music']").click()
        checkbox = driver.find_element(By.ID, "//label[normalize-space()='Music']").is_selected()
        print(checkbox)

        # radio button
        driver.find_element(By.ID, "//label[normalize-space()='Male']").click()
        radio = driver.find_element(By.ID, "//label[normalize-space()='Male']").is_selected()
        print(radio)

        # button
        driver.find_element(By.ID, 'submit').click()

        driver.quit()

demo = FormTest()
demo.test()
