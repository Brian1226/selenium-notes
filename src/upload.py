from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

class UploadTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get('https://demoqa.com/upload-download')

        # inputting the absolute path of the file to upload
        file_to_upload = os.path.abspath('my_uploads/batman.jpeg')
        upload_file_btn = driver.find_element(By.ID, 'uploadFile')
        upload_file_btn.send_keys(file_to_upload)

        driver.quit()

demo = UploadTest()
demo.test()
