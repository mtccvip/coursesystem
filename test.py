class Student:
    __school= 'Tinghua'

    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd

print(Student.__dict__)