import os
import toml
import pymysql
from config.path import Path
from pymysql.constants import CLIENT
from dbutils.pooled_db import PooledDB


class SqlUtil:
    def __init__(self):
        env_path = os.path.join(Path.env_path)
        env_toml = toml.load(env_path)
        self.db_pool = PooledDB(
            creator=pymysql,
            host=env_toml["Mysql"]["ip"],
            port=3306,
            user=env_toml["Mysql"]["usr"],
            password=env_toml["Mysql"]["pwd"],
            database=env_toml["Mysql"]["db"],
            charset="utf8mb4",
            client_flag=CLIENT.MULTI_STATEMENTS,
        )
        self._conn = None
        self._cur = None

    def conn_sql(self):
        self._conn = self.db_pool.connection()
        self._cur = self._conn.cursor()

    def select(self, sql):
        if self._conn is None or self._cur is None:
            self.conn_sql()
        try:
            self._cur = self._conn.cursor(cursor=pymysql.cursors.DictCursor)
            self._cur.execute(sql)
            res = self._cur.fetchall()
            self._conn.commit()
            return res
        except Exception as e:
            self._conn.rollback()
            raise Exception("执行SQL出错："+str(e))

    def insert(self, t_name, keys, values):
        if self._conn is None or self._cur is None:
            self.conn_sql()
        try:
            sql = f"insert into {t_name} ({', '.join(keys)}) values ({', '.join(['%s']*len(keys))})"
            self._cur.executemany(sql, values)
            self._conn.commit()
        except Exception as e:
            self._conn.rollback()
            raise Exception("插入出现错误："+str(e))

    def create_table(self, file_obj, db_obj):
        column_lst = []
        for k, v in file_obj.__members__.items():
            tmp = v.value
            column_lst.append(
                f"`{k}` {tmp.get('type')}({tmp.get('byte')}) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL  DEFAULT NULL COMMENT '{tmp.get('comment')}'"
            )
        column_info = ",\n".join(column_lst)
        t_name = db_obj.__dict__.get('table')
        sql = """
        DROP TABLE IF EXISTS `{drop_table_name}`;
        CREATE TABLE `{table_name}` (
        `id` int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        {column_info} 
        ) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET =utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;
        """.format(
            drop_table_name=t_name,
            table_name=t_name,
            column_info=column_info,
        )
        self.select(sql)


if __name__ == '__main__':
    SqlUtil().conn_sql()