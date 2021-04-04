# Author:Han
# python:3.9
import pytest

from SetpTest_10.HomeWork_10.test_wework.wework_page.address import Address


class TestAddress:

    def setup(self):
        self.address = Address()
        self.userid = "zhangsan90aa"
        self.name = "helelelea"
        self.department = [1]
        self.mobile = "+86 13300000092"

    @pytest.mark.parametrize("userid,mobile", [("zhangsan009", "13200000009"),
                                               ("zhangsan002", "13200000002")
                                        ])
    # 新增成员（先删除清洗数据，再新增）
    def test_add_member(self, userid, mobile):
        self.address.delete_member(userid)
        r = self.address.add_member(userid, self.name, self.department, mobile)

    #删除成员，先新增，再删除，避免删除报错
    def test_delete_member(self):
        self.address.add_member(self.userid, self.name, self.department, self.mobile)
        self.address.delete_member(self.userid)

    #修改成员，先删除成员，再新增，在修改成员成员
    def test_update_member(self):
        self.address.delete_member(self.userid)
        self.address.add_member(self.userid, self.name, self.department, self.mobile)
        new_name = self.name + "hjjkk"
        self.address.update_member(self.userid, new_name, self.mobile)

    #获取成员，现在删除，再新增，然后再去获取信息
    def test_get_membner_infomation(self):
        self.address.delete_member(self.userid)
        self.address.add_member(self.userid, self.name, self.department, self.mobile)
        r = self.address.get_membner_infomation(self.userid)
        print(r)
