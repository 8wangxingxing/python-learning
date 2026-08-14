import json
# 数据文件路径
STUDENT_FILE = 'student.json'
def load_student():
    try:
        with open(STUDENT_FILE,'r',encoding='utf-8' ) as f:
            return json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
student_list=load_student()
def save_student(students):
    with open(STUDENT_FILE,'w',encoding='utf') as f:
        json.dump(students,f,ensure_ascii=False,indent=4)


# student_list=[{'id':"1",'name':'小明','age':'22'},{'id':"2",'name':'小红','age':'22'},{'id':"3",'name':'张明','age':'22'}]


def add():
    print("添加学生信息")
    print("学号","姓名","年龄")#怎么插入空格
    stu = {}
    stu['id']=input("输入学生的学号：").strip()
    stu['name']=input("输入学生的姓名：").strip()
    stu['age']=input("输入学生的年龄：").strip()
    student_list.append(stu)
    save_student(student_list)
    for stu in student_list:
        print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")
def substract():
    print("删除学生信息")
    id=input("请输入要删除的学生的学号；").strip()
    for stu in student_list:
        if stu['id'] == id:
            print(f"已删除：{stu['name']}的相关信息")
            student_list.remove(stu)
            save_student(student_list)
            for stu in student_list:
                print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")
def modify():
    print("修改学生信息")
    id=input("输入修改的学生的学号:")
    for stu in student_list:
        if stu['id'] == id:
            stu['id'] = input("输入新的id：")
            stu['name'] = input("输入新的名字：")
            stu['age'] = input("输入新的年龄：")
            save_student(student_list)

def show():
    print("显示所有学生")
    for stu in student_list:
        print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")


def exit():
    print("退出操作系统")
def select():
    print("查询学生信息")
    print('''
    ===查询学生信息===
    1、通过学号查询
    2、通过姓名查询
    3、通过年龄查询
    ''')

    choice=input('输出要选择的选项：')
    if choice=='1':
        id=input("请输入要查询的学号：").strip()
        for stu in student_list:
            if stu['id'] == id:
                print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")
    elif choice=='2':
        name=input("输入要查询的姓名：").strip()
        for stu in student_list:
            if stu['name'] == name:
                print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")
    elif choice=='3':
        age=input("请输入要查询的年龄：").strip()
        for stu in student_list:
            if stu['age'] == age:
                print(f"学号:{stu['id']} 姓名 {stu['name']} 年龄：{stu['age']}")
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