from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MultipleWindowsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/links')

        # get first handle
        first_handle = driver.current_window_handle
        driver.find_element(By.ID, 'simpleLink').click()

        # switch to second handle using for loop
        handles = driver.window_handles
        for handle in handles:
            if handle != first_handle:
                driver.switch_to.window(handle)

        # switch to second handle using for loop
        # handles = driver.window_handles
        # for handle in handles:
        #     driver.switch_to.window(handle)
        #     if driver.title == 'DEMOQA':
        #         break

        # switch to third handle using index, then close tab
        driver.find_element(By.CLASS_NAME, 'banner-image').click()
        handles = driver.window_handles
        driver.switch_to.window(handles[2])
        driver.close()

        # switch to second handle using index, then close tab
        driver.switch_to.window(handles[1])
        driver.close()

        driver.quit()

demo = MultipleWindowsTest()
demo.test()
