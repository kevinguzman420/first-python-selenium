# from webdriver_manager.chrome import ChromeDriverManager # this
from selenium.webdriver.chrome.service import Service # this
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time, uuid

password = ["pass123$%","elen23$51","word324%","length12#$%","face23$%&1","hru231%$#"] #replace with your required password here...

service = Service(executable_path="C:\\bin\\chromedriver.exe") # this

driver = webdriver.Chrome(service=service)



import ctypes, sys

def is_admin(): # this
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    driver.get("https://www.google.com/intl/es/gmail/about/")

    time.sleep(1)

    driver.find_element_by_xpath('/html/body/main/div/div/div/div/div/div/div[3]/div/a').click()

    time.sleep(1)

    # Name
    name = "Fernanda"
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/div/div/div/div/div/input').send_keys(name)

    time.sleep(1)

    # Lastname
    lastname = "Cabrera"
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div/div/div[2]/div/div/div/div/input').send_keys(lastname)

    time.sleep(1)

    # To add an uuid part to fullname to generate a valid email
    code = uuid.uuid1()
    email_code = str(code).replace("-", "")
    fullname_length = len(name + lastname)
    email_format = lastname.lower() + name.lower()

    for char in range(fullname_length, 30):
        email_format += email_code[char]

    print()
    print()
    print(email_format)
    print()
    print()

    # Email
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div[2]/div/div/div/div/div/input').send_keys(email_format)

    time.sleep(2)

    # Password
    password = "fernandacabrera"
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div[3]/div/div/div/div/div/div/div/div/input').send_keys(password)

    time.sleep(2)

    # Confirm Password
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/div/form/span/section/div/div/div[3]/div/div/div/div[2]/div/div/div/div/input').send_keys(password)

    time.sleep(6)

    # Click button ("prefiero iniciar sesión")
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/button').click()

    time.sleep(6)

    driver.close()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)




