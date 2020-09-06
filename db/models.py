from db import db_handler

class Admin:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    @classmethod
    def select(cls,username):
        obj = db_handler.select_data(cls,username)
        return obj


    def save(self):
        db_handler.save_data(self)


class School:
    pass

class Student:
    pass

class Course:
    pass

class Teacher:
    pass

