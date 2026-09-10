"""
该文件用于 完成学生管理系统的 具体业务的操作，即：增删改查，保存学生信息等...
"""
#导包
import json
from student import Student

class StudentCMS(object):
    #类属性，保存数据的文件名（保存和加载都要用，定义在这里避免写两遍）
    filename = "students.json"

    #定义魔法方法，初始化属性信息
    def __init__(self):
        #启动时自动从文件加载，没有文件就是空列表
        self.students = self.load_students()

    #定义函数，根据姓名查找学生，找到返回学生对象，找不到返回 None
    #（删除、修改、查询单个都要用，抽出来避免重复写三遍）
    def find_student(self, name):
        for stu in self.students:
            if stu.name == name:
                return stu      # 找到就立刻返回，只返回第一个同名的
        return None             # 循环走完都没找到

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
        print('-' * 23)
        print("【添加学生】")

        #1.接收姓名，姓名是学生的标识，不能为空
        name = input("请输入姓名：").strip()
        if name == "":
            print("姓名不能为空，添加失败！")
            print('-' * 23)
            return

        #2.接收性别
        gender = input("请输入性别：").strip()

        #3.接收年龄，input 拿到的是字符串，需要转成数字
        #  用 try-except 兜底，防止用户输入非数字导致程序直接崩溃
        try:
            age = int(input("请输入年龄：").strip())
        except ValueError:
            print("年龄必须是数字，添加失败！")
            print('-' * 23)
            return

        #4.接收手机号和描述信息
        phone = input("请输入手机号：").strip()
        description = input("请输入描述信息：").strip()

        #5.用收集到的信息创建一个学生对象
        stu = Student(name, gender, age, phone, description)

        #6.把对象追加到列表中，完成保存
        self.students.append(stu)

        print(f"学生 {name} 添加成功！当前共有 {len(self.students)} 名学生")
        print('-' * 23)

    #定义函数，删除学生信息
    def delete_student(self):
        print('-' * 23)
        print("【删除学生】")

        #1.没有数据就没得删
        if len(self.students) == 0:
            print("当前系统中还没有学生信息！")
            print('-' * 23)
            return

        #2.按姓名找到要删的那个学生对象
        name = input("请输入要删除的学生姓名：").strip()
        stu = self.find_student(name)
        if stu is None:
            print(f"没有找到姓名为 {name} 的学生，删除失败！")
            print('-' * 23)
            return

        #3.删除是不可逆的，先二次确认
        print(f"待删除：{stu}")
        answer = input(f"确认删除 {name} 吗？(y/n)：").strip().lower()
        if answer != "y":
            print("已取消删除")
            print('-' * 23)
            return

        #4.remove 是按“值”删除，直接把对象传进去即可
        self.students.remove(stu)
        print(f"学生 {name} 删除成功！当前共有 {len(self.students)} 名学生")
        print('-' * 23)

    #定义函数，修改学生信息
    def update_student(self):
        print('-' * 23)
        print("【修改学生信息】")

        #1.没有数据就没得改
        if len(self.students) == 0:
            print("当前系统中还没有学生信息！")
            print('-' * 23)
            return

        #2.按姓名找到要改的那个学生对象
        name = input("请输入要修改的学生姓名：").strip()
        stu = self.find_student(name)
        if stu is None:
            print(f"没有找到姓名为 {name} 的学生，修改失败！")
            print('-' * 23)
            return

        #3.逐项修改，括号里是当前值，直接回车表示这一项不改
        print(f"当前信息：{stu}")
        print("提示：不想修改的项目，直接按回车跳过")

        new_name = input(f"姓名（{stu.name}）：").strip()
        if new_name != "":
            stu.name = new_name

        new_gender = input(f"性别（{stu.gender}）：").strip()
        if new_gender != "":
            stu.gender = new_gender

        #年龄要转数字，转失败就只跳过这一项，不影响其他已改的内容
        new_age = input(f"年龄（{stu.age}）：").strip()
        if new_age != "":
            try:
                stu.age = int(new_age)
            except ValueError:
                print("年龄必须是数字，本项未修改")

        new_phone = input(f"手机号（{stu.phone}）：").strip()
        if new_phone != "":
            stu.phone = new_phone

        new_description = input(f"描述信息（{stu.description}）：").strip()
        if new_description != "":
            stu.description = new_description

        print(f"修改成功！{stu}")
        print('-' * 23)

    #定义函数，查询单个学生信息
    def query_one_student(self):
        print('-' * 23)
        print("【查询单个学生】")

        if len(self.students) == 0:
            print("当前系统中还没有学生信息！")
            print('-' * 23)
            return

        name = input("请输入要查询的学生姓名：").strip()
        stu = self.find_student(name)
        if stu is None:
            print(f"没有找到姓名为 {name} 的学生！")
        else:
            print(stu)      # 自动调用 Student 的 __str__

        print('-' * 23)

    #定义函数，查询所有学生信息
    def query_all_students(self):
        print('-' * 23)

        #1.先判断有没有数据，列表为空时直接提示，不往下走
        if len(self.students) == 0:
            print("当前系统中还没有学生信息，请先添加！")
            print('-' * 23)
            return

        #2.遍历列表，逐个打印学生对象
        #  注意：print(学生对象) 会自动调用 Student 的 __str__ 方法
        print(f"共有 {len(self.students)} 名学生：")
        num = 1
        for stu in self.students:
            print(f"{num}. {stu}")
            num += 1

        print('-' * 23)

    #定义函数，保存学生信息
    def save_students(self):
        #1.对象没法直接写进文件，先把每个学生对象转成字典
        #  __dict__ 能直接拿到一个对象的所有属性，返回的就是字典
        stu_list = []
        for stu in self.students:
            stu_list.append(stu.__dict__)

        #2.用 json 把“字典列表”写成文本存进文件
        #  with 会在写完后自动关闭文件，不用手动 close
        #  ensure_ascii=False 保证中文正常显示，不然会存成 \uXXXX
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(stu_list, f, ensure_ascii=False)

        print(f"保存成功！{len(self.students)} 名学生已写入 {self.filename}")

    #定义函数，实现加载学生信息
    def load_students(self):
        #1.读文件，读出来是“字典组成的列表”
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                stu_list = json.load(f)
        except FileNotFoundError:
            #第一次运行时文件还不存在，属于正常情况，返回空列表即可
            return []
        except json.JSONDecodeError:
            #文件是空的或内容被改坏了
            print("数据文件内容有误，已按空数据启动")
            return []

        #2.把每个字典还原成 Student 对象，系统里始终操作对象而不是字典
        students = []
        for d in stu_list:
            students.append(
                Student(d["name"], d["gender"], d["age"], d["phone"], d["description"])
            )
        return students

    #定义函数，把上述所有业务逻辑跑通
    def start(self):
        #无限循环，让用户可以重复操作，直到确认退出
        while True:
            #1.显示系统菜单
            self.show_menu()

            #2.接收用户输入的功能序号（strip 去掉两端多余的空格）
            menu_num = input("请输入功能序号：").strip()

            #3.根据序号，调用对应的功能
            if menu_num == "1":
                self.add_student()
            elif menu_num == "2":
                self.delete_student()
            elif menu_num == "3":
                self.update_student()
            elif menu_num == "4":
                self.query_one_student()
            elif menu_num == "5":
                self.query_all_students()
            elif menu_num == "6":
                self.save_students()
            elif menu_num == "7":
                #二次确认，防止误操作退出
                answer = input("确认退出系统吗？(y/n)：").strip().lower()
                if answer == "y":
                    #退出前自动保存一次，防止用户忘了选 6 导致本次操作全丢
                    self.save_students()
                    print("感谢使用学生管理系统，再见！")
                    break
            else:
                print("输入有误，请输入 1-7 之间的序号！")


#测试
if __name__ == "__main__":
    cms = StudentCMS()
    cms.start()