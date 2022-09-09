import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

item = str(input('type what place do you want to find: '))
city = str(input('type the destination city: '))

s = Service(r'D:\download\chromedriver')
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.get(f'https://www.google.com/search?q={item}+in+{city}')
time.sleep(5)

driver.find_element(by=By.XPATH, value='//*[@id="Odp5De"]/div/div/div[2]/div[1]/div[4]/g-more-link/a/div/span[1]').click()

# scrap per item
mainpage = driver.find_elements(by=By.XPATH, value='//div[@jsname="GZq3Ke"]')
for i in mainpage:
    i.find_element(by=By.CLASS_NAME, value='rllt__details').find_element(by=By.TAG_NAME, value='span').click()

    # waiting for opened js
    time.sleep(10)

    # start scrap
    title = driver.find_element(by=By.CLASS_NAME, value='SPZz6b').find_element(by=By.TAG_NAME, value='h2').find_element(by=By.TAG_NAME, value='span').text
    rating = driver.find_element(by=By.CLASS_NAME, value='Aq14fc').text
    review = driver.find_element(by=By.CLASS_NAME, value='hqzQac').find_element(by=By.XPATH, value='//*[@id="akp_tsuid_9"]/div/div[1]/div/div/block-component/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div/span[3]/span/a/span').text
    location = driver.find_element(by=By.CLASS_NAME, value='LrzXr').text

    # scrap for opening hours
    opening = driver.find_element()


    # storage
    dat = {
        'Name Location': title,
        'Rating': rating,
        'Review': review,
        'location': location
    }

    # test result
    print(f'{title}, rating = {rating}, {review}, location: {location}')

time.sleep(20)
driver.close()


