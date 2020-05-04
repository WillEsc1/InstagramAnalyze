from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class IGBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)

        loginButton = driver.find_element_by_xpath("//a[@href'accounts/login]")
        loginButton.click()
        time.sleep(2)

        user_name_element = driver.find_element_by_xpath("//input[@name='username']")
        user_name_element.clear()
        user_name_element.send_keys(self.username)
        time.sleep(2)

        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(2)

        password_element.send_keys(Keys.RETURN)


myBot = IGBot("thewillescobar", "PromiseE@12")
myBot.login()