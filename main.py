from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox() # Create the browser
driver.get("https://10fastfingers.com/typing-test/english") # Go to this link

elem = driver.find_element_by_css_selector("#inputfield") # find the text field 

for i in range(1000):
    word = driver.find_element_by_css_selector("#row1 > span.highlight") # find the word you are going to write
    # loop through the word
    for i in word.text:
        elem.send_keys(i) # send a letter of the world every 0.009 seconds
        time.sleep(.009)
    elem.send_keys(Keys.SPACE) # then send space