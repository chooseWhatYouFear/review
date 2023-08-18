from enum import Enum


class FileSchool(Enum):
    number = dict(byte=8, type='char', encoding='utf-8', comment='学号')
    name = dict(byte=3, type='char', encoding='utf-8', comment='姓名')
    sex = dict(byte=1, type='char', encoding='utf-8', comment='性别')
    class_num = dict(byte=2, type='char', encoding='utf-8', comment='班级名')
    main_teacher = dict(byte=3, type='char', encoding='utf-8', comment='班主任')