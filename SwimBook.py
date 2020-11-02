####Book Swims at Arlington aquatic centers
#Add logic to check if class is booked
from datetime import date, timedelta
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import helperFunctions

import helperFunctions

username = ""
password = ""
securityCode = ''

def lambda_handler(event, context):
    #uncomment below to run in headless mode
    #assert opts.headless  # Operating in headless mode
    opts = Options()
    opts.binary_location = './headless-chromium'
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--single-process')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument("--window-size=1920,1080")

    browser = Chrome(executable_path='./chromedriver', options=opts)
    browser.get('https://arlingtonaquatics.ezfacility.com/Sessions#')
    WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '/html/body/section[2]/section/div/div[3]/div/div[1]/div[1]/ul/li[2]/button'))).click()
#     browser.find_element_by_xpath('//*[@id="fc-actions"]/li[2]/button').click()

    #Get the form data
    today = date.today()
    tomorrow = date.today() + timedelta(days = 1)
    formData = helperFunctions.getReservationData(today,tomorrow)

    #Find the index for the 7am washlib reservation (We can put some logic in for a second choice if it's full)
    tableIndex =(helperFunctions.getResponseindex(formData))
    if (tableIndex >=0):
        dataEventID = formData[tableIndex]['id']
        # browser should wait up to 10 seconds for elements to appear
        browser.implicitly_wait(10)

        # click the element
        tablerow = browser.find_element_by_xpath("//*[@data-eventid=" + str(dataEventID) + "]")
        tablerow.click()

        # click buy
        # bottombar = browser.find_element_by_xpath('/html/body/section[2]/section/div/div[4]/div/div/div[1]')
        # clickbutton = bottombar.find_element_by_xpath('/html/body/section[2]/section/div/div[4]/div/div/div[1]/button[2]')
        # browser.find_element_by_xpath('//*[@id="btnBook"]').click()

        WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="btnBook"]'))).click()

        # login and buy package
        browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[3]/div/div/div/form/div[1]/div/div/div/input').send_keys(username)
        browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[3]/div/div/div/form/div[2]/div/div/div/input').send_keys(password)
        browser.find_element_by_xpath('//*[@id="btnLogin"]').click()

        # element = WebDriverWait(browser, 10).until(ec.element_to_be_clickable('/html/body/section[2]/section/div/div[4]/div/div/div[1]/button[3]'))
        browser.find_element_by_xpath('/html/body/section[2]/section/div/div[4]/div/div/div[1]/button[3]').click()

        # buy package for adult resident

        browser.find_element_by_xpath(
            '/html/body/section[2]/section/div/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[7]/div/button').click()
        WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="defaultCVN"]'))).click()
        WebDriverWait(browser, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="defaultCVN"]'))).send_keys(
            securityCode)

        body = f"Headless Chrome Initialized, Page title: {browser.title}"

        browser.close()
        browser.quit()

        return {
            "statusCode": 200,
            "body": body
        }

    return {
        "statusCode": 404,
        "body": formData
    }
