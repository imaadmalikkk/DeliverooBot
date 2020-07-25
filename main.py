from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret import pwd
from selenium.webdriver.common.action_chains import ActionChains


PATH = "/Users/imaadmalik/Desktop/Development/Python_Selenium/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://deliveroo.co.uk")
time.sleep(2) # time to allow the site to load to avoid an exception error
# Presses the log in button
LogIn = driver.find_element_by_link_text("Sign up or log in")
LogIn.click()
time.sleep(2)
# Presses continue with email button
ContinueByEmail = driver.find_element_by_class_name("ccl-cce251427bbe4ec4")
ContinueByEmail.click()
time.sleep(2)
# Enters my email
Email = driver.find_element_by_class_name("ccl-f67359d1c16a266a")
Email.send_keys("imaad@wearenwn.com")
time.sleep(2)
# Presses continue
Continue = driver.find_element_by_class_name("ccl-cce251427bbe4ec4")
Continue.click()
time.sleep(2)
# Puts my password in from another file 
Password = driver.find_element_by_id("login-password")
Password.send_keys(pwd)
time.sleep(2)
# Presses continue
Go = driver.find_element_by_class_name("ccl-cce251427bbe4ec4")
Go.click()
time.sleep(2)
# Searches for my postcode
searchLocation = driver.find_element_by_id("location-search")
searchLocation.send_keys("WD19 4JH")
searchLocation.send_keys(Keys.RETURN)
time.sleep(2)
Food = driver.find_element_by_class_name("HomeSearch-b8d615a5b6ee28c6")
Food.send_keys("Pepes")
Food.send_keys(Keys.RETURN)
time.sleep(2)
Location = driver.find_element_by_class_name("HomeSuggestionRow-9580956c8c36b7d6")
Location.click()
time.sleep(3)
Order = driver.find_element_by_xpath("//li[13]")
Order.click()
time.sleep(5)
Flavour = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/span/button/label/div/div/div/span")
Flavour.click()
Meal = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[2]/div/div[3]/div/div/div/div[4]/span/button/label/div/div/div/span")
Meal.click()
Buy = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[3]/div/div/span[1]/span/button/span")
Buy.click()
time.sleep(1000)
