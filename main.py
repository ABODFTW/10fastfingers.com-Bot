from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://10fastfingers.com/typing-test/english")

elem = driver.find_element_by_css_selector("#inputfield")

for i in range(1000):
    word = driver.find_element_by_css_selector("#row1 > span.highlight")
    for i in word.text:
        elem.send_keys(i)
        time.sleep(.009)
    elem.send_keys(Keys.SPACE)