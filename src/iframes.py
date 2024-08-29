from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class IFramesTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/nestedframes')
        
        # switch to parent iframe using locator
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame1']"))

        # switch to its child iframe using locator
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']"))

        # print text from child iframe
        child_text = driver.find_element(By.XPATH, "//p[normalize-space()='Child Iframe']").text
        print(child_text)

        # can switch iframes using 'name' attribute, parent, or index too
        # when in parent, can access children. But if in child and want to switch to siblings, need to switch back to parent first
        driver.switch_to.parent_frame()
        driver.switch_to.frame(0)
        child_text = driver.find_element(By.XPATH, "//p[normalize-space()='Child Iframe']").text
        print(child_text)

        driver.quit()

demo = IFramesTest()
demo.test()
