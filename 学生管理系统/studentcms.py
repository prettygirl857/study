"""
该文件用于 完成学生管理系统的 具体业务的操作，即：增删改查，保存学生信息等...
"""
#导包
from student import Student

class StudentCMS(object):
    #定义魔法方法，初始化属性信息
    def __init__(self):
        self.students = []    # 用于存储学生对象的列表

    #定义函数，实现打印 管理系统的界面
    def show_menu(self):
        print('*' * 23)
        print("欢迎使用学生管理系统")
        print("\t1. 添加学生")
        print("\t2. 删除学生")
        print("\t3. 修改学生信息")
        print("\t4. 查询单个学生信息")
        print("\t5. 查询所有学生信息")
        print("\t6. 保存学生信息")
        print("\t7. 退出系统")
        print('*' * 23)


    #定义函数，添加学生信息
    def add_student(self):
        pass

    #定义函数，删除学生信息
    def delete_student(self):
        pass    

    #定义函数，修改学生信息
    def update_student(self):  
        pass

    #定义函数，查询单个学生信息
    def query_one_student(self):
        pass    

    #定义函数，查询所有学生信息
    def query_all_students(self):
        pass

    #定义函数，保存学生信息
    def save_students(self):
        pass    

    #定义函数，实现加载学生信息
    def load_students(self):
        pass

    #定义函数，把上述所有业务逻辑跑通
    def start(self):


#测试
if __name__ == "__main__":
    cms = StudentCMS()
    cms.start()