# 演示对象属性和类属性
# 定义一个student类，每个学生有自己的姓名，年龄
class Student:
    # 定义类属性
    school = "武汉大学"


    # 定义对象属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 定义str方法，返回学生的姓名和年龄
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}"  
    
# 测试
if __name__ == "__main__":
    # 创建两个学生对象
    s1 = Student("张三", 20)
    s2 = Student("李四", 22)

    # 修改s1属性值
    s1.name = "王五"
    s1.age = 21

    print(s1) 
    print(s2)  
   
    s2.school = "清华大学"  # ❌ 这样改不了类属性！只是在 s2 身上新建了同名实例属性
    print(f"学校: {s1.school}")  # 武汉大学（类属性没被动过）
    print(f"学校: {s2.school}")  # 清华大学（s2 自己的实例属性，挡住了类属性）

    # ✅ 正确修改类属性
    Student.school = "清华大学"
    print(f"学校: {s1.school}")  # 清华大学（类属性真的被改了，s1 跟着变）。只能通过类名. 来修改