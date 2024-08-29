from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class JScriptTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # open window
        driver.execute_script("window.open('https://demoqa.com/links' , '_self')")

        # return second link
        home_link = driver.execute_script("return document.getElementsByTagName('a')[1];")

        # click second link
        driver.execute_script("arguments[0].click();", home_link)
        driver.quit()

demo = JScriptTest()
demo.test()
