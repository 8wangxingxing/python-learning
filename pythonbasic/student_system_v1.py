import json
# 数据文件路径
STUDENT_FILE = 'student.json'
def load_student():
    try:
        with open(STUDENT_FILE,'r',encoding='utf-8') as f:
            data = json.load(f)
        # json读取字典列表 → 转为Student对象列表
        student_obj_list = []
        for d in data:
            s = Student(d["id"], d["name"], d["age"])
            student_obj_list.append(s)
        return student_obj_list
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_student(students):
    # Student对象列表 → 字典列表，才能存入json
    dict_list = []
    for stu in students:
        temp = {
            "id": stu.id,
            "name": stu.name,
            "age": stu.age
        }
        dict_list.append(temp)
    with open(STUDENT_FILE,'w',encoding='utf-8') as f:
        json.dump(dict_list, f, ensure_ascii=False, indent=4)


# student_list=[{'id':"1",'name':'小明','age':'22'},{'id':"2",'name':'小红','age':'22'},{'id':"3",'name':'张明','age':'22'}]

class Student():
    def __init__(self,id,name,age):
        self.id =id
        self.name = name
        self.age = age

s1=Student('1','小明','12')
s2=Student('2','小刚','13')
s3=Student('3','小冰','23')
student_list=load_student()


def add():
    print("添加学生信息")
    print("学号","姓名","年龄",sep="  "  )#怎么插入空格
    stu: Student = Student("", "", "")
    stu.id=input("输入学生的学号：").strip()
    for i in student_list:
        if stu.id==i.id:
            print("已有学号存在，无法添加")
            return []
    stu.name=input("输入学生的姓名：").strip()
    stu.age=input("输入学生的年龄：").strip()
    student_list.append(stu)
    save_student(student_list)
    for stu in student_list:
        print(f"学号:{stu.id} 姓名 {stu.name} 年龄：{stu.age}")
def substract():
    print("删除学生信息")
    id=input("请输入要删除的学生的学号；").strip()
    stu: Student
    for stu in student_list:
        if stu.id == id:
            print(f"已删除：{stu.name}的相关信息")
            student_list.remove(stu)
            save_student(student_list)
            for stu in student_list:
                print(f"学号:{stu.id} 姓名 {stu.name} 年龄：{stu.age}")
def modify():
    print("修改学生信息")
    id=input("输入修改的学生的学号:")
    for stu in student_list:
        if stu.id == id:
            stu.id = input("输入新的id：")
            stu.name = input("输入新的名字：")
            stu.age = input("输入新的年龄：")
            save_student(student_list)

def show():
    print("显示所有学生")
    for stu in student_list:
        print(f"学号:{stu.id} 姓名 {stu.name} 年龄：{stu.age}")


def exit():
    print("退出操作系统")
def select():
    print("查询学生信息")
    id=input("请输入要查询的学号：").strip()
    for stu in student_list:
        if stu.id == id:
            print(f"学号:{stu.id} 姓名 {stu.name} 年龄：{stu.age}")

    else:
        print("输入无效")


def main():
    while  True:
        print('''
    ===学生管理系统===
    1、添加学生信息
    2、删除学生信息
    3、修改学生信息
    4、查询学生信息
    5、显示所有学生
    0、退出操作系统
    ''')
        student_list = load_student()
        choice = input("输入你要操作的选项：")
        if choice == "1":
            add()
        elif choice == "2":
            substract()
        elif choice =="3":
            modify()
        elif choice == "4":
            select()
        elif choice == "5":
            show()
        elif choice == "0":
            exit()
            break
        else :
            print("输入错误，请重新输入")
if __name__ == '__main__':
    main()