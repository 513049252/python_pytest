from api.api import Api
import pytest
# 实例化对象
api = Api()
class TestLogin():
    def test_correct_login(self):
        username = "admir";password="1234"
        res = api.login(username,password)
        assert len(res)==0,"登录失败"
    def test_error_login(self):
        username = "admir";
        password = "12349"
        res = api.login(username, password)
        assert res == "密码错误", "返回不是密码错误"
    def test_get_longininfo(self):
        res = api.get_login_name()
        assert res["uUsername"]=="admir","登录用户不是admir"
        assert res["uPassword"]=="1234","登录密码不是1234"

if __name__ == '__main__':
    pytest.main()