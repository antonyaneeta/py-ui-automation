from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\chromedriver\chromedriver')

driver.get('https://www.google.com')

time.sleep(2)

google_search_box = driver.find_element_by_name('q')
google_search_box.send_keys('smile')

time.sleep(2)
google_search_button = driver.find_element_by_css_selector('input[type="submit"]')
google_search_button.click()

'''
//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input
<input class="gNO89b" value="Google Search" aria-label="Google Search" name="btnK" type="submit" data-ved="0ahUKEwjKwIv61pvtAhWx63MBHT8KCTwQ4dUDCAs">

'''