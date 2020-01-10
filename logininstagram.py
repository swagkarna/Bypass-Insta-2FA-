import time, os
from selenium import webdriver
usernamePath = "/var/www/html/instagram/username.txt"
passwordPath = "/var/www/html/instagram/password.txt"
codePath = "/var/www/html/instagram/code.txt"
fusername = open(usernamePath, "r")
username = fusername.readline()
fpass = open(passwordPath, "r")
password = fpass.readline()
profile = webdriver.FirefoxProfile()
driver = webdriver.Firefox(executable_path='/root/2FAInstagram/geckodriver', firefox_profile=profile)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(1);
driver.find_element_by_name("username").send_keys(username.split("\n")[0])
driver.find_element_by_name("password").send_keys(password.split("\n")[0])
time.sleep(1);
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
while not os.path.exists(codePath):
    time.sleep(1)
fcode = open(codePath, "r")
code = fcode.readline()
driver.find_element_by_name("verificationCode").send_keys(code.split("\n")[0])
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/button").click()




