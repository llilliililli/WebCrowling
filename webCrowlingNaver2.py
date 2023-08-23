# 크롤링 2 ) selenium 방식

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip


LOGIN_NAVER = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
NAVER = "https://www.naver.com/"

id = '네이버 계정'
pw = '네이버 계정 암호'


driver = webdriver.Chrome()
driver.get(LOGIN_NAVER)
# print(driver.body)
time.sleep(1)

tag_Id = driver.find_element(By.ID,'id')
tag_Pw = driver.find_element(By.ID,'pw')

tag_Id.clear()
tag_Pw.clear()
time.sleep(1)

# # id 입력
tag_Id.click()
pyperclip.copy(id)
tag_Id.send_keys(Keys.CONTROL,'v')
time.sleep(1)

# # pw 입력
tag_Pw.click()
pyperclip.copy(pw)
tag_Pw.send_keys(Keys.CONTROL,'v')
time.sleep(1)


# #login Btn
login_btn = driver.find_element(By.CLASS_NAME,'btn_login')
login_btn.click()
time.sleep(1)


# #new.dontsave
login_btn = driver.find_element(By.ID,'new.dontsave')
login_btn.click()
time.sleep(2)



# try:

#     # btns = driver.find_elements(By.TAG_NAME,'sc-button')
#     # for b in btns:
#     #     print(b.text)

#     # alert = driver.switch_to.alert
#     # print(alert.text)
#     # alert.accept

#     # driver.find_element(By.LINK_TEXT, "확인").click()
#     # text = alert.text
#     # alert.accept()

#     tap_btn = driver.find_element(By.TAG_NAME,'sc-toolbar')
#     print(tap_btn.text)
#     #tap_btn.click()


# except:
#     print('pass')
#     pass

# # popup_btn = driver.find_element(By.CLASS_NAME,'style-scope sc-messagebox')
# # popup_btn.click()
# time.sleep(5)