from re import A
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.taipower.com.tw/tc/page.aspx?mid=206&cid=406&cchk=b6134cc6-838c-4bb9-b77a-0b0094afd49d")
driver.find_element('xpath','/html/body/form/div[5]/div[3]/div[2]/div/div[3]/ul/li[1]/a').click()
time.sleep(2)
a = driver.find_element('xpath','/html/body/div[2]/div/table[1]/tbody/tr/td[1]/div[2]/h5/span').text
print(a)
# /html/body/div[2]/div[2]/div[2]/div/span[1]
time.sleep(5)
time.sleep(5)