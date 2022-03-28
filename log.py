import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.get('https://tienichmmo.net/tfa/')
# driver.find_element_by_xpath('/html/body/form/textarea').send_keys('MIRTMSE55JEW2MP3AANWUHZONS3OZZ5H')
# driver.find_element_by_xpath('/html/body/form/div[1]/button').click()
# driver.switch_to.frame(frame_reference=driver.find_element_by_xpath(xpath="//iframe[@id='iFrameResizer0']"))
# twofa  = driver.find_element_by_xpath('/html/body/span/span').get_attribute('innerHTML').splitlines()[0]
# print(twofa)

# driver.get('https://www.facebook.com/')
# time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input').send_keys('100074595218511')
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input').send_keys('ShopSun@#8006')
# driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()

driver.get('https://mail.tm/en/')
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div/button/img').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[4]/a').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/span/form/div[1]/span/div/input').send_keys('tunghovan11044615@metalunits.com')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/span/form/div[2]/span/div/input').send_keys('TieL#16920')
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/span[1]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div[2]/ul/li[1]/a/div/div[1]/div[2]/div[1]/div[1]').click()
time.sleep(1)
driver.switch_to.frame(frame_reference=driver.find_element_by_xpath(xpath="//iframe[@id='iFrameResizer0']"))
otpmail  = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td/span/div/table/tbody/tr/td/span').get_attribute('innerHTML').splitlines()[0]
print(otpmail)
# driver.get('https://www.facebook.com/')
time.sleep(1)