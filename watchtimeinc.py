
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
hour = int(input('enter hour:'))

links = [
            'https://www.youtube.com/watch?v=MhSBeVsL1bw',
            'https://www.youtube.com/watch?v=r_4uz9YIX9o',
            'https://www.youtube.com/watch?v=FAkGlmwfLa0',
            'https://www.youtube.com/watch?v=MF0npoiQfFU',
            'https://www.youtube.com/watch?v=2CpuznudFlk',
            'https://www.youtube.com/watch?v=kuKEvrJFM6o',
            'https://www.youtube.com/watch?v=qU7y7YdYV-g',
            'https://www.youtube.com/watch?v=T3ObvO6oAAY',
            'https://www.youtube.com/watch?v=wf5z_FPdRb8',
            'https://www.youtube.com/watch?v=uFZtVer4Uiw',
            'https://www.youtube.com/watch?v=FHS8d7d7pSw',
            'https://www.youtube.com/watch?v=gGmER2HTBP8',
            'https://www.youtube.com/watch?v=9EZQJURUp2k',
            'https://www.youtube.com/watch?v=1M1IeA7277c',
            'https://www.youtube.com/watch?v=kuKEvrJFM6o',
            'https://www.youtube.com/watch?v=MhSBeVsL1bw',
            'https://www.youtube.com/watch?v=r_4uz9YIX9o',
            'https://www.youtube.com/watch?v=FAkGlmwfLa0',
            'https://www.youtube.com/watch?v=MF0npoiQfFU',
            'https://www.youtube.com/watch?v=2CpuznudFlk',
            'https://www.youtube.com/watch?v=kuKEvrJFM6o',
            'https://www.youtube.com/watch?v=qU7y7YdYV-g',
            'https://www.youtube.com/watch?v=Fi405o8kCH0'
            
            ]
print(len(links))


for times in range(hour*6):    
    

    driver = webdriver.Chrome('F://chromedriver.exe')
    driver.get("https://www.youtube.com/watch?v=Zutpvox5ygI")

    for link in links:
        driver.execute_script("window.open('{}');".format(link))

    
    time.sleep(10)    
    for i in range(10):
        for j in range(len(driver.window_handles)):
            if(i==0):
                driver.switch_to_window(driver.window_handles[j])
                try :
                    element2 = driver.find_element_by_link_text( "No thanks").click()    
                    print('No thanks is clicked')
                except Exception as e:
                    print(e)
                        
                try:
                    element2 = driver.find_element_by_link_text( "I agree").click()
                    print('I agree is clicked')
                except Exception as e:
                    print(e)
                    
                try:
                    driver.find_element_by_xpath("//button[@aria-label='Settings'").click()

                    element = driver.find_element_by_xpath("//button[@aria-label='Play']")
                    element.click()
                except Exception as e:
                    print(e)
                #body = driver.find_element_by_tag_name("body")
                #body.send_keys(Keys.SPACE)
                print('Tab switched:',j)
                #time.sleep(5)
        #time.sleep(60)
        print(i+1,' minute over')
    print('Refreshing Tabs')
    driver.quit()
        
    print(times,'/',hour*6,' remaining')
