from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class DropdownsTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/select-menu')

        # dropdown (select tag)
        # dropdown = driver.find_element(By.ID, 'oldSelectMenu')
        # dropdown.click()
        # select = Select(dropdown)
        # select.select_by_index(0)
        # select.select_by_visible_text('Blue')
        # select.select_by_value('2')
        # dropdown.click()

        # multi-select dropdown (div tag)
        multi_dropdown = driver.find_element(By.XPATH, "(//div[contains(@class,'css-1hwfws3')])[3]")
        multi_dropdown.click()
        # select an option by clicking on it
        driver.find_element(By.ID, 'react-select-4-option-2').click()
        # select an option by typing and pressing enter
        multi_input = driver.find_element(By.ID, 'react-select-4-input')
        multi_input.send_keys('red')
        multi_input.send_keys(Keys.ENTER)

        # .deselect_all(), .deselect_by_index(), .deselect_by_visible_text(), .deselect_by_value() only works for Select class

        driver.quit()

demo = DropdownsTest()
demo.test()
