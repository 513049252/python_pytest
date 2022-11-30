import requests,time
# 定义重试装饰器
def retry(times):
    def wrapper(func):
        def inner_wrapper(*args,**kwargs):
            for i in range(times):
                try:
                    return func(*args,**kwargs)
                except:
                    print("重试第{}次{}()".format(i,func.__name__))
                    time.sleep(1)
            assert False
        return inner_wrapper
    return wrapper
class ApiRequests(object):
    def __init__(self):
        pass
    # 定义post方法
    @retry(3)
    def post_method(self,url,headers,data=None):
        session = requests.session()
        response = session.post(url=url, data=data, headers=headers)
        if response.status_code==200:
            return response.text
        else:
            print("请求失败")
    #  定义get方法
    def get_method(self,url,headers,data=None):
        session = requests.session()
        response = session.post(url=url, params=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("请求失败")
