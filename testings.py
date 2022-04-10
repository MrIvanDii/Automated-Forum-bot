from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random_account
import random_URL
import time
import ran_comm

up_acc_stat = random_account.upgrade_status()
up_url_stat = random_URL.upgrade_url_status()
up_comm_stat = ran_comm.upgrade_commetns_status()

web_url = "https://www.quora.com/"
list_of_url = random_URL.get_list_of_url()

list_of_acc = random_account.get_list_of_acc()

for url in list_of_url:
    #print(random_URL.upgrade_url_status())
    print(ran_comm.upgrade_commetns_status())

    for i in range(list_of_acc):

        url_for_use = url

        username, password = random_account.random_pass_acc()


        driver = webdriver.Chrome()
        driver.get(web_url)

        time.sleep(2)
        driver.find_element(By.NAME, "email").send_keys(username)

        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys(password)

        time.sleep(2)


#------------------------------ТУТ НАДО РЕШИТЬ КАПТЧУ------------------------------------------


        #if not driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border"):
            #continue
        #else:
            #driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()


#-----------------------------------------------------------------------------------------------


        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)

        time.sleep(2)

        driver.get(url_for_use)

        time.sleep(5)

        try:
            coment_box = driver.find_element(By.CLASS_NAME, "section")

        except NoSuchElementException:
            pass

        driver.find_element(By.NAME, "Comment").click()
        time.sleep(2)

        coment_box = driver.find_element(By.CLASS_NAME, "section")
        time.sleep(2)

        coment_box.send_keys(ran_comm.random_comment())
        time.sleep(2)

        driver.quit()


    print(random_account.upgrade_status())
    #print(random_URL.upgrade_url_status())
    print(ran_comm.upgrade_commetns_status())


print('DONE')