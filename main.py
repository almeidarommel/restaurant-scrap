import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# rom selenium.webdriver.support import expected_conditions as EC
import pandas as pd

city = str(input('type the destination city: '))
pagg = int(input('how many page do you scrap: '))

s = Service(r'D:\download\chromedriver')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get(f'https://www.google.com/search?q=restaurant+in+{city}')
time.sleep(7)
driver.find_element(by=By.XPATH, value='//*[@id="Odp5De"]/div/div/div[2]/div[1]/div[4]/g-more-link/a/div/span[1]').click()

data = []
# scraping time!!
for a in range(0, pagg):
    time.sleep(7)
    mainpage = driver.find_elements(by=By.XPATH, value='//div[@jsname="GZq3Ke"]')

    for start in mainpage:
        start.find_element(by=By.CLASS_NAME, value='rllt__details').click()

        # waiting for opened js
        time.sleep(7)

        # start scrap
        title = driver.find_element(by=By.CLASS_NAME, value='SPZz6b').find_element(by=By.TAG_NAME, value='h2').find_element(by=By.TAG_NAME, value='span').text
        rating = driver.find_element(by=By.CLASS_NAME, value='Aq14fc').text
        review = driver.find_element(by=By.CLASS_NAME, value='hqzQac').find_element(by=By.XPATH, value='//*[@id="akp_tsuid_9"]/div/div[1]/div/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/span[3]/span/a/span').text
        location = driver.find_element(by=By.CLASS_NAME, value='LrzXr').text

        # scrap phone number
        try:
            numm = driver.find_element(by=By.XPATH, value='//span[(@class="LrzXr zdqRlf kno-fv")]').text
        except Exception:
            numm = 'no phone number'

        # scrap for opening hours
        try:
            driver.find_element(by=By.CLASS_NAME, value='IDu36').click()
            opening = driver.find_element(by=By.CLASS_NAME, value='WgFkxc').text
            if opening == '':
                time.sleep(3)
                opening = driver.find_element(by=By.XPATH, value='//table[(@class="WgFkxc CLtZU")]').text
                driver.find_element(by=By.XPATH, value='//*[@id="gsr"]/div[12]/g-lightbox/div/div[2]/div[2]').click()
        except Exception:
            opening = 'no opening hours'
        # storage
        dat = {
            'Name Location': title,
            'Rating': rating,
            'Review': review,
            'location': location,
            'Phone Number': numm,
            'Opening Hours': opening
        }
        data.append(dat)

        # test result
        print(f'{title}, rating = {rating}, {review}, location: {location}, phone: {numm}, operational hours: {opening}')

    # click next page
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="pnnext"]/span[2]').click()
    except Exception:
        break

# create data excle
df = pd.DataFrame(data)
df.to_excel(f'result from {pagg} page.xlsx', index=False)

driver.close()

