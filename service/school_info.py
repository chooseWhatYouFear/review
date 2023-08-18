import random

from utilities.sql_util import SqlUtil
from utilities.tools_util import ToolsUtil
from db_tables.db.db_school import DbSchool
from db_tables.file.file_school import FileSchool


class SchoolInfo:
    def __init__(self):
        self._sql_util = SqlUtil()
        self.keys = [v for k, v in DbSchool.__dict__.items() if not k.startswith('__') and k not in ('table', 'id')]
        self.vals = []

    def insert_data(self):
        t_name = DbSchool.table
        self._sql_util.insert(
            t_name=t_name,
            keys=self.keys,
            values=self.vals
        )

    def gen_data(self):
        for i in range(100):
            tmp = [
                f'{i:0>8}',
                ToolsUtil.rand_zh(3),
                random.sample(('男', '女'), 1),
                random.sample(('1', '2', '3', '4'), 1),
                random.sample(('赵云', '姜子牙', '狂铁', '吕布'), 1)
            ]
            self.vals.append(tmp)

    def run(self):
        self._sql_util.create_table(FileSchool, DbSchool)
        self.gen_data()
        self.insert_data()


if __name__ == '__main__':
    SchoolInfo().run()