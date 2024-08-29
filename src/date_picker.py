from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DatePickerTest():
    def test(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        
        driver.get('https://demoqa.com/date-picker')

        # click on input field
        driver.find_element(By.ID, 'datePickerMonthYearInput').click()

        # wait for date to be visible
        date = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='react-datepicker__current-month react-datepicker__current-month--hasYearDropdown react-datepicker__current-month--hasMonthDropdown']")))

        # dictonary for months
        months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

        # loop through months (default is August 2024, but looking for November 2024)
        while(date.text != 'November 2024'):
            print(date.text)
            month, year = date.text.split(' ')
            if months[month] < 11 and int(year) == 2024:
                driver.find_element(By.XPATH, "//button[normalize-space()='Next Month']").click()
            elif  months[month] > 11 and int(year) == 2024:
                driver.find_element(By.XPATH, "//button[normalize-space()='Previous Month']").click()
            elif year < '2024':
                driver.find_element(By.XPATH, "//button[normalize-space()='Next Month']").click()
            elif year > '2024':
                driver.find_element(By.XPATH, "//button[normalize-space()='Previous Month']").click()

        # click on specified date
        driver.find_element(By.XPATH, "//div[@aria-label='Choose Friday, November 1st, 2024']").click()
        
        driver.quit()

demo = DatePickerTest()
demo.test()
