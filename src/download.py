from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

class DownloadTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        options = Options()
        
        # get absolute path of my_downloads directory
        my_downloads = os.path.abspath('my_downloads')

        # set preferences to change default download directory
        prefs = {'download.default_directory': my_downloads}
        options.add_experimental_option('prefs', prefs)

        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://demoqa.com/upload-download')

        download_button = driver.find_element(By.ID, 'downloadButton')
        download_button.click()

        driver.quit()

demo = DownloadTest()
demo.test()

