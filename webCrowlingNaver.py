# 크롤링 1 ) BeautifulSoup 방식

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import time


# 크롤링 로그인( 세션 )
LOGIN_NAVER = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
NAVER = "https://www.naver.com/"

id = '네이버 계정'
pw = '네이버 계정 암호'


session = requests.Session()

login_info = {
    "id":id,
    "pw":pw
}



with session as s:

    firstPage = s.get(LOGIN_NAVER)
    html = firstPage.text
    soup = BeautifulSoup(html, "html.parser")
    locale = soup.find('input',{'name':'locale'})
    timezone = soup.find('input',{'name':'timezone'})
    sysId = soup.find('input',{'name':'sysId'})
    csrf = soup.find('input',{'name':'_csrf'})

    print('locale :: '+str(locale['value']))
    print('timezone :: '+str(timezone['value']))
    print('sysId :: '+str(sysId['value']))
    print('csrf :: '+str(csrf['value']))

    headers = {  # 참조 및 유저정보 입력
        'Referer': LOGIN_NAVER,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    # 크롬 개발자도구 > 네트워크 > LOGIN_NAVER URL > 페이로드 양식 데이터 
    LOGIN_INFO = { **{'locale': locale['value']}, **{'timezone': timezone['value']}, **{'sysId': sysId['value']},**{'_csrf': csrf['value']}, **login_info}

    print('LOGIN_INFO :: '+str(LOGIN_INFO))

    response = session.post(LOGIN_NAVER,data=LOGIN_INFO, headers=headers)

    # APROS 로그인 처리
    if response.status_code == 200:
        print('로그인 성공')
        time.sleep(2)

        #print(response.text)
        
        request = s.get(NAVER,headers=headers)

        print(request.text)

    else:
        print('로그인 실패')



# 크롤링


# html = urlopen(APROS)


#print(bsObject)
#print(bsObject.title)
#print(bsObject.head.find("meta",{"name":"description"}))
# print(bsObject.body.find("div",{"class":"login_area"}))
# time.sleep(1)



# print(response.text)
