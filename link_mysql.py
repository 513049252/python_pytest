#!/usr/bin/python3
#coding=utf-8

import pymysql
class LinkMysql():
    def __init__(self):
        self.db = pymysql.connect(host="120.79.242.145", database="mms", user="root", password="523147689")
        self.cursor = self.db.cursor()
    # 查询数据库
    def select_table(self,select_sql):
        try:
            self.cursor.execute(select_sql)
        except Exception as e:
            print(e)
        else:
            data = self.cursor.fetchall()
            print(data)
        finally:
            # self.db.close()
            # self.connect.close()
            return data
    # 更新数据库表
    def uptade_table(self,update_sql):
        try:
            self.cursor.execute(self.cursor.execute(update_sql))
            self.cursor.close()  # 先关游标
        except Exception as e:
            self.cursor.close()  # 先关游标
            self.connect.rollback()
            print(e)
        finally:
            self.cursor.close()
            self.connect.commit()
            self.connect.close()
    # 删除数据库数据
    def drop_table(self,drop_sql):
        self.cursor.execute(drop_sql)
# if __name__ == '__main__':
#     t = LinkMysql().select_table("select cno from client;")
#     assert ('4396',) in t,"asdf"


