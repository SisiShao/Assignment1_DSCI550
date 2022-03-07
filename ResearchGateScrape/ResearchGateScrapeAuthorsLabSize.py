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
        writer.writerow(['article',
                         'author',
                         'lab_size'])

for article in articles:
    driver.get('https://www.researchgate.net/search')

    sleep(5)  # this sleep is essential

    # input the title of article in the search bar
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/form/div[2]/input').send_keys(
        article, Keys.ENTER)
    sleep(2)
    print('article:', article)

    for i in range(2, 5):
        try:
            ul = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[{i}]/ul')
            lis = ul.find_elements(By.XPATH, 'li')
            break
        except NoSuchElementException:
            pass

    for s in range(2, len(lis)+1):
        for i in range(2, 5):
            try:
                author = driver.find_element(By.XPATH,
                                             f'/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[{i}]/ul/li[{s}]/a/span[2]').text
                print('author:', author)
                break
            except NoSuchElementException:
                pass

        # get the contents and have to click to get the author's info
        for i in range(2, 5):
            try:
                driver.find_element(By.XPATH,
                                    f'/html/body/div[1]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div[1]/div/div/div/div/div/div[{i}]/ul/li[{s}]/a/span[2]').click()
                break
            except NoSuchElementException:
                pass

        try:
            lab_size = driver.find_element(By.XPATH,
                                             '/html/body/div[1]/main/aside/div[1]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/b').text[
                         -3:-1]
        except NoSuchElementException:
            lab_size = 'N/A'
        print('lab_size:', lab_size)

        s += 1
        driver.back()

        with open('2.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.writer(f)
            writer.writerow([article,
                             author,
                             lab_size
                             ])

    print('==========================================')
    sleep(2)