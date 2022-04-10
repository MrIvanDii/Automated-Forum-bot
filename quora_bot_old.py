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
    print(random_URL.upgrade_url_status())
    print(ran_comm.upgrade_commetns_status())
    print(random_account.random_pass_acc())

    for i in range(list_of_acc):

        url_for_use = url

        username, password = random_account.random_pass_acc()

        driver = webdriver.Chrome()
        driver.get(web_url)

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

        time.sleep(2)

        # ------------------------------ТУТ НАДО РЕШИТЬ КАПТЧУ------------------------------------------

        # if not driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border"):
        # continue
        # else:
        # driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-border").click()

        # -----------------------------------------------------------------------------------------------

        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div[2]/div[2]/div[4]/button').click()

        time.sleep(2)

        driver.get(url_for_use)

        time.sleep(5)

        try:
            # ищу строку для комментариев, если ее нет - ищу кнопку "комментарий" и нажимаю,
            # чтоб потом зайти в строку для комментариев
            comment_section = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[9]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div')
            # нашел строку для комментариев
            time.sleep(2)

            comment_section.send_keys(ran_comm.random_comment())
            # вставил в строку рандомный коммент
            time.sleep(2)

            add_comment_button = driver.find_element(By.XPATH,
                                                     '//*[@id="mainContent"]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/button')
            # нашел кнопку "отправить комментарий"
            time.sleep(2)

            add_comment_button.click()
            # кликнул по кнопке "отправить комментарий"

            time.sleep(5)

        except NoSuchElementException:

            driver.find_element(By.XPATH,
                                '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[7]/div/div/div[1]/span[3]/div/div/button').click()
            # нашел кнопку "комментарии" и кликнул по ней, чтоб перейти в строку для комментариев
            time.sleep(2)

            comment_section = driver.find_element(By.XPATH,
                                                  '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[9]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div')
            # нашел строку для комментариев
            time.sleep(2)

            comment_section.send_keys(ran_comm.random_comment())
            # вставил в строку рандомный коммент
            time.sleep(2)

            add_comment_button = driver.find_element(By.XPATH,
                                                     '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[9]/div/div/div/div/div[1]/div[2]/div/button')
            # нашел кнопку "отправить комментарий"
            time.sleep(2)

            add_comment_button.click()
            # кликнул по кнопке "отправить комментарий"

            pass


        #coment_box = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[9]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div')
        #time.sleep(2)

        #coment_box.send_keys(ran_comm.random_comment())
        #time.sleep(2)

        #add_comment_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div/div[1]/div[2]/div/div/div[1]/div[2]/div/button')
        #print('Кнопка найдена')
        #time.sleep(5)

        #add_comment_button.click()
        #time.sleep(10)

        upvote_button = driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div/div/div/div/div/div[7]/div/div/div[1]/span[1]/div/div/div[1]/div/button')
        upvote_button.click()
        time.sleep(10)


        driver.quit()

    print(random_account.random_pass_acc())
    # print(random_URL.upgrade_url_status())
    print(ran_comm.upgrade_commetns_status())

print('DONE')