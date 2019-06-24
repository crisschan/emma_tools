# encoding=utf8
# !/usr/bin/env python
# __author_='crisschan'
# __from__='EmmaTools：https://github.com/crisschan/EMMATools'
# import MySQLdb
import pymysql

class MySQLHelper(object):
    def __init__(self, host, port,user, password,charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.charset = charset

        try:
            self.conn = pymysql.connect(host=self.host, port=self.port,user=self.user, passwd=self.password)
            self.conn.set_charset(self.charset)
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
    def __del__(self):
        self.close()
    def selectDb(self, db):
        try:
            self.conn.select_db(db)
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def query(self, sql):
        try:
            #---
            #print sql
            n = self.cur.execute(sql)
            return n
        except pymysql.Error as e:
            print("Mysql Error:%s\nSQL:%s" % (e, sql))

    def queryRow(self, sql):
        self.query(sql)
        result = self.cur.fetchone()
        return result

    def queryAll(self, sql):
        self.query(sql)
        result = self.cur.fetchall()
        desc = self.cur.description
        d = []
        for inv in result:
            _d = {}
            for i in range(0, len(inv)):
                _d[desc[i][0]] = str(inv[i])
            d.append(_d)
        return d

    def insert(self, p_table_name, p_data):
        for key in p_data:
            #try:
            p_data[key] = "'" + str(p_data[key]).replace('\'','"') + "'"
            #except:
            #p_data[key]="u'" + str(p_data[key].encode('utf8')).replace('\'','"') + "'"

        key = ','.join(p_data.keys())
        value = ','.join(p_data.values())

        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value+ ")"

        # self.query("set names 'utf8'")

        return self.query(real_sql)

    def moreinsert(self, p_table_name, p_data):
        for key in p_data:
            #try:
            p_data[key] = "'" + str(p_data[key]) + "'"
            #except:
            #p_data[key]="u'" + str(p_data[key].encode('utf8')).replace('\'','"') + "'"

        key = ','.join(p_data.keys())
        value = ','.join(p_data.values())

        real_sql = "INSERT INTO " + p_table_name + " (" + key + ") VALUES (" + value+ ")"

        # self.query("set names 'utf8'")

        return self.query(real_sql)
    def getLastInsertId(self):
        return self.cur.lastrowid

    def rowcount(self):
        return self.cur.rowcount

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()