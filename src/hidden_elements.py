from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HiddenElementsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://www.yatra.com/hotels')
        
        # click dropdown
        driver.find_element(By.XPATH, "//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        
        # click plus button for child
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        
        # check if age select button is displayed
        try:
            age_select = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
            print(age_select)
        except NoSuchElementException:
            print("Element not found in DOM")
        
        # click minus button for child
        driver.find_element(By.XPATH, "//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()

        # check if age select button is displayed
        try:
            age_select = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
            print(age_select)
        except NoSuchElementException:
            print("Element not found in DOM")

        driver.quit()

demo = HiddenElementsTest()
demo.test()
