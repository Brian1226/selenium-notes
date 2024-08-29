from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class ScreenshotsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/text-box')

        # screenshot before filling out form
        driver.save_screenshot('screenshots/before.png')

        driver.find_element(By.ID, 'userName').send_keys('Brian')
        driver.find_element(By.ID, 'userEmail').send_keys('test_email89@gmail.com')
        driver.find_element(By.ID, 'submit').click()

        # screenshot after filling out form
        driver.save_screenshot('screenshots/after.png')

        driver.quit()

demo = ScreenshotsTest()
demo.test()
