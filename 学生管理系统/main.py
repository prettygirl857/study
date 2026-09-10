"""
该文件是 学生管理系统的 主程序入口，负责启动整个系统
运行方式：直接运行本文件即可
"""
#导包
from studentcms import StudentCMS


#程序入口：只有直接运行 main.py 时才执行，被别的文件 import 时不会启动系统
if __name__ == "__main__":
    #1.创建学生管理系统对象（创建时会自动从文件加载已有的学生信息）
    cms = StudentCMS()

    #2.启动系统，进入菜单循环
    cms.start()
