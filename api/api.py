# -*- coding: UTF-8 -*-
from common.request_util import ApiRequests
import configparser,logging,os,sys
# 添加文件日志
# sys.path(os.getcwd())
logging.basicConfig(level=logging.INFO,format="%(asctimes)s - %(nema)s - %(levelname)s - %(message)s")
config = configparser.RawConfigParser()
config.read(r"D:\test_soft\python_pytest\api\config.ini")
api = ApiRequests()
class Api(ApiRequests):
    def __init__(self):
        # super(Api,self.__init__())
        self.host = config.get("host","host")
        self.headers = dict(config.items("headers"))

    # 登录
    def login(self,username,password):
        url = self.host + "/mms/Login/loginUser"
        payload = "username={0}&password={1}".format(username,password)
        res = api.post_method(url=url,data=payload,headers=self.headers)
        return res

    # 获取顾客信息
    def get_client_message(self,page,count):
        url = self.host + "/mms/Client/GetMessage"
        data = {"page":page,"rows":count}
        res = api.post_method(url=url,data=data,headers=self.headers)
        return res

    # 查询顾客信息
    def search_client_message(self,cno):
        url = self.host + "/mms/Client/GetClient"
        data = {"cno":cno}
        res = api.post_method(url=url,data=data,headers=self.headers)
        # print(res)
        return res

    # 录入顾客信息
    def client_save_client(self,cno):
        url = self.host + "/mms/Client/SaveClient"
        data = {
            "cno":cno,
            "cname":"张三",
            "csex": "男",
            "cage": "23",
            "cphone":"123",
            "ano": "10342830",
            "cdate":"2022-11-15",
            "mno": "1000562256",
            "caddress":"撒的法国红酒看来",
            "csymptom":"的风格",
            "cremark":"微软体育"
        }
        res = api.post_method(url=url, data=data, headers=self.headers)
        print(res)
        return res

    # 修改顾客信息
    def client_modify_client(self,cname):
        url = self.host + "/mms/Client/ModifyClient"
        data = {
            "cid":6,
            "cno": "1237",
            "cname": cname,
            "csex": "男",
            "cage": "23",
            "cphone": "123",
            "ano": "10342830",
            "cdate": "2022-11-15",
            "mno": "1000562256",
            "caddress": "撒的法国红酒看来",
            "csymptom": "的风格",
            "cremark": "微软体育"
        }
        res = api.post_method(url=url, data=data, headers=self.headers)
        print(res)
        return res

    # 删除顾客信息
    def client_delete_rows(self,cno):
        url = self.host + "/mms/Client/DeleteRows"
        data = {"array[]": cno}
        res = api.post_method(url=url, data=data, headers=self.headers)
        print(res)
        return res

    # 获取经办人的信息
    def get_agency_message(self):
        url = self.host + "/mms/Agency/GetMessage"
        data = {"page": 1, "rows": 10}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    # 查询经办人的信息
    def search_agency_message(self):
        url = self.host + "/mms//Agency/GetAgency"
        data = {"ano": "1000055"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    # 增加经办人信息
    def agency_save_agency(self):
        url = self.host + "/mms/Agency/SaveAgency"
        data = {"ano": "69", "aname": "张三", "asex": "男", "aphone": "234567", "aremark": "自己肯定很厉害"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    # 修改经办人信息
    def agency_modify_rows(self):
        url = self.host + "/mms/Agency/ModifyAgency"
        data = {"aid": "9369", "ano": "1000055", "aname": "张三", "asex": "男", "aphone": "234567",
                "aremark": "自己肯定很厉害"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    # 删除经办人信息
    def agency_delete_rows(self):
        url = self.host + "/mms/Agency/DeleteRows"
        data = {"array[]": "10018252"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    # 获取药品信息
    def get_medicine_message(self):
        url = self.host + "/mms/Medicine/GetMessage"
        data = {"page": 1, "rows": 10}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res
    # 查询药品信息---bug
    def search_medicine_message(self):
        url = self.host + "/mms/Medicine/GetMedicine"
        data = {"mno": "1000007667"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res
    # 增加药品信息
    def medicine_save_message(self):
        url = self.host + "/mms/Medicine/SaveMedicine"
        data = {"mno": 100870, "mmode": "内服","mname":"测试","mefficacy":"的时刻v但是看了"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res
    # 修改药品信息
    def medicine_modify_message(self):
        url = self.host + "/mms/Medicine/ModifyMedicine"
        data = {"mno": 1008700, "mmode": "内服","mname":"测试12345","mefficacy":"的时刻v但是看了"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res
    # 删除药品信息
    def medicine_delete_message(self):
        url = self.host + "/mms/Medicine/DeleteRows"
        data = {"array[]": "1000664460"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res
    # 获取登录用户信息
    def get_login_name(self):
        url = self.host + "/mms/Login/GetLoginName"
        data = ""
        res = api.get_method(url=url, data=data, headers=self.headers)
        # data = json.loads(res.json)
        print(res["uUsername"])
        # return res

    # 查询管理员用户
    def get_user_queryalluser(self):
        url = self.host + "/mms/User/queryAllUser"
        data = {"page": 1, "rows": 10}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    #  添加管理员
    def user_add_user(self):
        url = self.host + "/mms/User/AddUser"
        data = {"uUsername": "test12", "uPassword": "123456","uAccess":"信息浏览功能"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    #  修改系统管理员
    def user_update_user(self):
        url = self.host + "/mms/User/UpdateUser"
        data = {"uUsername": "test1", "uPassword": "123456","uAccess":"信息浏览功能"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

    #  删除管理员
    def user_delete_user(self):
        url = self.host + "/mms/User/DeleteUser"
        data = {"uUsername": "test12"}
        res = api.post_method(url=url, data=data, headers=self.headers)
        return res

if __name__ == '__main__':
#     Api().login()
#     Api().get_login_name()
#     Api().get_client_message(1,10)
#     Api().client_save_client("")
#     Api().client_modify_client("789")
    Api().client_delete_rows("123")
    # Api().get_agency_message()
    # Api().get_medicine_message()
    # Api().medicine_save_message()
    # Api().search_medicine_message()
    # Api().medicine_modify_message()
    # Api().user_add_user()
    # Api().medicine_delete_message()
    # Api().user_delete_user()
    # Api().user_update_user()
    # Api().get_client_save_client()
    # Api().agency_save_agency()
    # Api().agency_delete_rows()
    # Api().agency_modify_rows()
    # Api().search_agency_message()
    # Api().search_client_message("12")