# -*- coding:utf-8 -*-
# _author_ = 'zdq'


import sys
import pymysql
import psycopg2
from Utility.logger import Logger


log = Logger(logger="db_helper").get_log()


class Database:
    # 配置host，端口等信息
    def __init__(self, host, port, user, passwd, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cursor = None

    def get_mysql_con_cursor(self):
        try:
            self.conn = pymysql.Connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd,
                                        db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
        except Exception as e:
            # self.conn.close()
            log.error("MySQL数据库连接错误：%S" % e)

    def get_postgresql_conn(self, host, port, user, passwd, db):
        try:
            self.conn = psycopg2.connect(host=host, port=port, user=user, password=passwd,
                                         database=db)
            self.cursor = self.conn.cursor()
        except Exception as e:
            self.conn.close()
            log.error("postgresql数据库连接错误：%s" % e)

    def db_rw(self, sql):
        try:
            self.cursor.execute(sql)
            if 'insert' in sql.lower() or 'update' in sql.lower():
                result = True
            else:
                result = self.cursor.fetchall()
            self.conn.commit()
            return result
        except Exception as e:
            self.conn.commit()
            log.error("SQL语句执行错误：%s；当前SQL：%s" % (e, sql))
            return False

    def close(self):
        self.conn.close()
