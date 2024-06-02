from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def fill_form(username, email, password):
    driver = webdriver.Chrome()
    driver.get("https://discord.com/register")
    time.sleep(2)
    
    username_field = driver.find_element_by_name("username")
    username_field.send_keys(username)
    
    email_field = driver.find_element_by_name("email")
    email_field.send_keys(email)
    
    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)
    
    password_field.send_keys(Keys.RETURN)
    
    time.sleep(5)
    
    driver.close()

# Test the form filling function
fill_form("test_user", "test_email@example.com", "test_password")