from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoCompleteTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/auto-complete')

        # send keys to input field
        driver.find_element(By.XPATH, "//input[@id='autoCompleteSingleInput']").send_keys("a")
        
        # wait for auto complete results to be visible, then get list of results
        search_results = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".auto-complete__option")))
        
        # print number of results
        print(len(search_results))
        
        # iterate through loop and click correct result
        for result in search_results:
            if result.text == 'Aqua':
                result.click()
                break

        driver.quit()

demo = AutoCompleteTest()
demo.test()
