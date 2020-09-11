import os
import sys
from conf import settings


def get_all_school_interface():
    school_dir  = os.path.join(settings.DB_PATH,'School')

    if not os.path.exists(school_dir):
        return False,'学校不存在,请先联系管理员'

    school_list = os.listdir(school_dir)
    return True,school_list

