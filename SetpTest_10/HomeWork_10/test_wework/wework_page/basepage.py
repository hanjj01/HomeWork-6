# Author:Han
# python:3.9
import requests


class BasePage:
    def __init__(self):
        #获取session
        self.s = requests.session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)

    #获取token
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwe3899bf08bc008d9&corpsecret=osqf3fOwSOKWnX7d2f5VZQSCsF5KR7VOpYrunEcH9O8"
        r= requests.get(url)
        token = r.json()["access_token"]
        # print(r.json())
        # print(token)
        return  token










