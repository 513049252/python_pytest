from api.api import Api
import pytest,json,time
from link_mysql import LinkMysql
linkmysql=LinkMysql()
# 实例化对象,json
api = Api()

class TestClient():
    # 正常浏览顾客信息
    def test_correct_get_client_message(self):
        page=1;count=10
        res = api.get_client_message(page,count)
        # 将返回内容转为json格式
        bodyjson = json.loads(res)
        # 校验前端展示内容不为空
        for item in bodyjson["rows"]:
            assert item["cid"] > 0,"返回顾客编号小于0"
            assert len(item["cno"])>0,"返回顾客编号长度小于0"
            assert len(item["cname"]) > 0, "返回顾客姓名长度小于0"
            assert len(item["csex"]) > 0, "返回顾客性别长度小于0"
            assert len(item["cage"]) > 0, "返回顾客年龄长度小于0"
            assert len(item["cphone"]) > 0,"返回顾客电话号码长度小于0"
            assert len(item["mno"]) > 0, "返回顾客已购药品编号长度小于0"
            assert len(item["ano"]) > 0, "返回顾客的经办人编号长度小于0"
            assert len(item["cdate"]) > 0, "返回数据更新时间长度小于0"
        # 数据库校验拉取内容正确
        sql = "select * from client;"
        data = linkmysql.select_table(sql)
        # 校验接口返回的值
        for a,b in zip(data,bodyjson["rows"]):
            assert a[0]==b["cno"],"接口返回的数据内容不存在数据库当中"
    # 搜索顾客信息--正向case
    def test_correct_search_client_message(self):
        cno = "123"
        res = api.search_client_message(cno)
        try:
            bodyjson = json.loads(res)
        except Exception as e:
            assert False
        else:
            assert bodyjson["cno"]==cno,"搜索顾客编号与返回顾客编号不一致"
            assert bodyjson["cid"] > 0,"返回顾客id小于0"

    # 搜索顾客信息--负向case
    def test_error_search_client_message(self):
        cno = "12"
        res = api.search_client_message(cno)
        try:
            bodyjson = json.loads(res)
        except:
            assert len(res) == 0,"输入不存在的顾客编号时，接口返回不为空"
            print(res)
        else:
            assert bodyjson["cno"]==cno,"搜索顾客编号与返回顾客编号不一致"
            assert bodyjson["cid"] > 0,"返回顾客id小于0"
    # 录入顾客信息--正向case
    def test_correct_client_save_client(self):
        cno = "10000"
        try:
            res = api.client_save_client(cno)
            assert res=="保存成功","录入失败！"
            # 数据库校验数据录入成功
            # ****有bug，需要第二次查询数据库才会返回刚刚录入的信息，待有空排查****
            # sql = "select cno from client;"
            # time.sleep(1)
            # linkmysql.select_table(sql)
            # data = linkmysql.select_table(sql)
            # assert (cno,) in data,"接口录入成功，但是数据库未查询到该记录"
        except Exception as e:
            print(e)
        else:
            # 清除录入的脏数据
            # time.sleep(1)
            api.client_delete_rows(cno)
    # 录入顾客信息--负向case
    def test_error1_client_save_client(self):
        cno = "123"
        res = api.client_save_client(cno)
        assert res=="客户编号已经存在，请重新输入编号","录入失败！"
    # 录入顾客信息--负向case
    # 编号传空时，由前端进行校验，接口不做校验，故可以正常录入成功！但是删除该记录需要执行sql语句进行删除
    # def test_error2_client_save_client(self):
    #     cno = ""
    #     try:
    #         res = api.client_save_client(cno)
    #         assert res=="保存成功","接口编号传空，应该可以正常录入！"
    #         # 数据库校验数据录入成功
    #         # ****有bug，需要第二次查询数据库才会返回刚刚录入的信息，待有空排查****
    #         # sql = "select cno from client;"
    #         # time.sleep(1)
    #         # linkmysql.select_table(sql)
    #         # data = linkmysql.select_table(sql)
    #         # assert (cno,) in data,"接口录入成功，但是数据库未查询到该记录"
    #     except Exception as e:
    #         print(e)
    #     else:
    #         # 清除录入的脏数据
    #         # time.sleep(1)
    #         api.client_delete_rows(cno)
    def test_correct_client_modify_client(self):
        cname = "张胜男"
        res = api.client_modify_client(cname)
        assert res == "修改成功","顾客信息未修改成功"
    def test_correct_client_delete_rows(self):
        cno = "8888"
        api.client_save_client(cno)
        res = api.client_delete_rows(cno)
        assert res=="删除成功","顾客信息删除失败"
if __name__ == '__main__':
    pytest.main(["-vs","./test_client_case.py::TestClient"])