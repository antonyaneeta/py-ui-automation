from selenium import webdriver
from config import USERNAME,PASSWORD
import time

browser = webdriver.Chrome(r'C:\chromedriver\chromedriver')
browser.maximize_window()
browser.get('https://www.instagram.com/')

users= ['aliaabhatt','joebiden']

time.sleep(2)

user_name_box = browser.find_element_by_name('username')
user_name_box.send_keys(USERNAME)

password_box = browser.find_element_by_name('password')
password_box.send_keys(PASSWORD)

time.sleep(2)
login_btn = browser.find_element_by_css_selector('button[type="submit"]')
login_btn.click()

time.sleep(4)

for user in users:
    browser.get(f"https://www.instagram.com/{user}/")
    posts, followers, following = browser.find_elements_by_class_name('g47SY')
    print(posts.text,followers.text)

    time.sleep(2)


out = browser.find_element_by_css_selector('span[role="link"]')
out.click()

logout_button = browser.find_element_by_class_name()   
logout_button.click()