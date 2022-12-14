# coding: utf8
""" 
@File: exec_sql.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/10/27 19:21
"""

from public.init_mysqlserver import ConnectMySQL


class ExecuteSQL(ConnectMySQL):
    """sql执行"""

    def __init__(self):
        super(ExecuteSQL, self).__init__()
        self.connect = super(ExecuteSQL, self).mysql()
        self.cursor = self.connect.cursor()

        
    def exec_sql(self, sql_msg):
        """
        执行sql语句方法封装
        不含查询, 无数据返回
        :param sql_msg: sql语句 
        :return: 
        """
        try:
            self.cursor.execute(query=sql_msg)
            print('执行成功！')
        except Exception as error:
            self.cursor.close()
            self.connect.close()
            print(error)
        self.cursor.close()
        self.connect.commit()
        self.connect.close()
        





