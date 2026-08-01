"""
该文件用于记录学生类，学生的属性包括：姓名、性别、年龄、手机号、描述信息、
"""
#定义学生类
class Student:
    #定义魔法方法，初始化属性信息
    def __init__(self, name, gender, age, phone, description):
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.description = description

    #定义魔法方法，返回学生的姓名和年龄
    def __str__(self):
        return f"姓名: {self.name}, 性别: {self.gender}, 年龄: {self.age}, 手机号: {self.phone}, 描述信息: {self.description}"



#测试
if __name__ == "__main__":
    student1 = Student("张三", "男", 20, "13812345678", "是个富家公子")
    print(student1)