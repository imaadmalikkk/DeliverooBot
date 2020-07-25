from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret import pwd
from secret import CN
from secret import Expiry
from secret import CVV
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


PATH = "/Users/imaadmalik/Desktop/Development/DeliverooBot/chromedriver"
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
time.sleep(2)
Order = driver.find_element_by_xpath("//li[13]")
Order.click()
time.sleep(2)
Flavour = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/span/button/label/div/div/div/span")
Flavour.click()
time.sleep(2)
Meal = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[2]/div/div[3]/div/div/div/div[4]/span/button/label/div/div/div/span")
Meal.click()
time.sleep(2)
Buy = driver.find_element_by_xpath("/html/body/div[15]/div/div/div/div[3]/div/div/span[1]/span/button/span")
Buy.click()
time.sleep(2)
Checkout = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/div/div/div/div/div[2]/div/div[1]/span/a/span/div/span[2]")
Checkout.click()
time.sleep(2)
Street = driver.find_element_by_id("address1")
Street.send_keys("58 Eastbury Road")
Note = driver.find_element_by_id("delivery_note")
Note.send_keys("Message when you are here and I will come down and collect")
#Submit = driver.find_element_by_xpath("//*[@id='payment-app-container']/div[2]/div/div/div[1]/form/div[6]/div/span/button/span")
#Submit.click()
time.sleep(3600)

