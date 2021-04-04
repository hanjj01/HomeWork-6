# Author:Han
# python:3.9
import requests

from SetpTest_10.HomeWork_10.test_wework.wework_page.basepage import BasePage


class Address(BasePage):
    #新增成员
    def add_member(self, userid, name, department, mobile):
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        crart_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = self.send("POST", url=crart_member_url, json=data)

    #删除成员
    def delete_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        parmes={
            'userid':userid
        }
        r = self.send("GET",url,params=parmes)

    #修改成员
    def update_member(self,userid,name,mobile):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid":userid,
            "name": name,
            "mobile": mobile
        }
        r = self.send("POST",url,json=data)

    #获取成员信息
    def get_membner_infomation(self,userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "userid" : userid
        }
        r = self.send("GET",url,params = params)

