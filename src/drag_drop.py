from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DragDropTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/droppable')

        actions = ActionChains(driver)
        
        # drag one element and drop on another
        draggable = driver.find_element(By.ID, 'draggable')
        droppable = driver.find_element(By.ID, 'droppable')
        actions.drag_and_drop(draggable, droppable).perform()

        # move element based on offset
        draggable = driver.find_element(By.ID, 'draggable')
        actions.drag_and_drop_by_offset(draggable, 100, 100).perform()

        driver.quit()

demo = DragDropTest()
demo.test()
