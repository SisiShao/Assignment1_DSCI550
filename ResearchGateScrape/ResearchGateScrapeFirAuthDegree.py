from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import csv

options = webdriver.ChromeOptions()

# unload any css or images
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
        'permissions.default.stylesheet': 2,
        'javascript': 1
    }
}
options.add_experimental_option('prefs', prefs)
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# read article list
with open('article.txt', 'r', encoding='utf8') as f:
    articles = f.readlines()
    articles = [article.replace('\n', '') for article in articles]

# prepare an empty csv file and write the title
try:
    with open('2.csv', 'r', encoding='utf8') as f:
        f.read()
except FileNotFoundError:
    with open('2.csv', 'w', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow(['author',
                         'degree'])

for article in articles:
    driver.get('https://www.researchgate.net/search')

    sleep(5)  # this sleep is essential

    # input the title of article in the search bar
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/form/div[2]/input').send_keys(
        article, Keys.ENTER)
    sleep(2)
    print('article:', article)

    # the xpath of the "author" is changing, so use 'for' to grab it
    for i in range(2, 5):
        try:
            author = driver.find_element(By.XPATH,
                                         f'/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[{i}]/ul/li[1]/a/span[2]').text
            print('author:', author)
            break
        except NoSuchElementException:
            pass

    # get the contents and have to click to get the author's info
    for i in range(2, 5):
        try:
            driver.find_element(By.XPATH,
                                f'/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[{i}]/ul/li[1]/a/span[2]').click()
            break
        except NoSuchElementException:
            pass

    sleep(2)

    # degree
    try:
        degree = driver.find_element(By.XPATH, '/html/body/div[1]/main/section[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div').text
    except NoSuchElementException:
        degree = 'N/A'
    print('degree:', degree)

    with open('2.csv', 'a', newline='', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow([author,
                         degree
                         ])
    print('==========================================')
    sleep(2)
