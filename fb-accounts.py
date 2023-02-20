# from webdriver_manager.chrome import ChromeDriverManager # this
from selenium.webdriver.chrome.service import Service # this
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

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
    driver.get("https://www.facebook.com/")

    time.sleep(4)

    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a').click()

    time.sleep(6)

    # driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input').send_keys(random.choice(firstname))
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input').send_keys("Catalina")

    time.sleep(1)

    # driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input').send_keys(random.choice(lastname))
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input').send_keys("Pérez")

    time.sleep(1)


    # Email
    email = "cabrerafernandad94fd4c77cb9a6a@outlook.es"
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input').send_keys(email) #replace with your mail/phone no

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[3]/div/div/div[1]/input').send_keys(email)#again paste the used mail/phone no

    time.sleep(1)

    # driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input').send_keys(random.choice(password))
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input').send_keys("thisismypass")

    time.sleep(2)

    dropdown = Select(driver.find_element_by_id("day"))
    dropdown.select_by_value("8")

    time.sleep(1)

    dropdown = Select(driver.find_element_by_id("month"))
    dropdown.select_by_value("5")

    time.sleep(1)

    dropdown = Select(driver.find_element_by_id("year"))
    dropdown.select_by_value("1999")

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[2]/input').click()

    time.sleep(2)

    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]').click()

    time.sleep(300)

    driver.close()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)




