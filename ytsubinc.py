from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


def Google(username, password,name_list):
    driver = webdriver.Chrome('F://chromedriver.exe')
    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
    driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    sleep(5)
    driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
    sleep(30)
    driver.get('https://www.youtube.com/create_channel?action_create_new_channel_redirect=true')

    for name in name_list:
        brand_name = driver.find_element_by_id("PlusPageName")
        brand_name.clear()
        brand_name.send_keys(name)
        brand_name.send_keys(Keys.RETURN)

   

fp = open('names.txt')
data = fp.read()
fp.close()
name_list = data.split('\n')

Google('jokrsingh@gmail.com','Joker@1998',name_list)

