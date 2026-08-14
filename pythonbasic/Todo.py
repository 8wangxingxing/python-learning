#个人记账本
import json
BILL_FILE="bill.json"
class Bill:
    def __init__(self, number, bill_type, amount, category, note):
        self.number = number
        self.bill_type = bill_type
        self.amount = amount
        self.category = category
        self.note = note
    def Record(self,):
        return {
            "number":self.number,
            "billtype":self.bill_type,
            "amount":self.amount,
            "note":self.note,
            "category":self.category
        }

# s=Todo(1,"支出",50,"日用","牙刷")
# print(s.Record())
class Bill_Manager():
    def __init__(self):
        self.bill_list= []
        self.number=0

    def save_bill(self):
        dict_list = []
        with open(BILL_FILE, "w",encoding='utf-8') as bill_file:
           for x in self.bill_list:
                temp_dict=x.Record()
                dict_list.append(temp_dict)
           json.dump(dict_list, bill_file, ensure_ascii=False,indent=4)
    def load_bill(self):
        temp_list = []
        try:
            with open(BILL_FILE, "r",encoding="utf-8") as bill_file:
                temp_list=json.load(bill_file)
                for i in temp_list:
                    x = Bill(1, 1, 1, 1, 1)
                    self.number = i['number']
                    x.number = i['number']
                    x.bill_type = i['billtype']
                    x.amount = i['amount']
                    x.category = i['category']
                    x.note = i['note']
                    self.bill_list.append(x)
        except FileNotFoundError:
            print("File Not Found")



    def addTodo(self,choice):
        self.number=self.number+1
        if choice == "1":
            billtype="收入"
        elif choice == "2":
            billtype="支出"
        amount=int(input("请输入金额："))
        while amount <0:
            print("金额出错，请重新输入")
            amount=int(input("请输入金额："))
        category=input("类别：").strip()
        note=input("备注：").strip()
        tempx=Bill(self.number, billtype, amount,category,note)
        self.bill_list.append(tempx)
        self.save_bill()
        print("添加成功")

    def show_bill(self):#查看所有记录
        print("编号","类型","金额","类别","备注",sep="  ")
        print("=======================================")
        for bill in self.bill_list:
            print(bill.number, bill.bill_type, bill.amount, bill.category, bill.note, sep="    ")
    def check_data(self):
        total_income=0
        income_items=0;
        total_expense=0
        expense_items=0;
        for bill in self.bill_list:
            if bill.bill_type=='收入':
                total_income=total_income+bill.amount
                income_items=income_items+1
            if bill.bill_type=='支出':
                total_expense=total_expense+bill.amount
                expense_items=expense_items+1
        print("总收入：",total_income)
        print(" ")
        print("总支出：",total_expense)
        print(" ")
        print("当前余额；",total_income-total_expense)
        print(" ")
        print(f"收入记录：{income_items} 条")
        print(" ")
        print(f"支出记录：{expense_items} 条")
    def del_record(self):
        number=int(input("请输入要删除的编号："))
        for bill in self.bill_list:
            if bill.number==number:
                self.bill_list.remove(bill)
                self.save_bill()
                print("删除成功")
                return
        print("没有这个编号")


    def fix_record(self):
        number=int(input("输入要修改的编号"))
        for bill in self.bill_list:
            if bill.number==number:
                bill.amount=int(input("请输入修改的金额："))
                bill.category=input("输入修改的类别：")
                bill.note=input("输入修改的备注：")
                self.save_bill()
                print("修改成功")










s1=Bill_Manager()
s1.load_bill()


def main():
    while True:
        print('''
        ===个人记账本===
        1、添加收入
        2、添加支出
        3、查看所有记录
        4、查询统计
        5、删除记录
        6、修改记录
        0、退出
        ==============
        ''')
        choice=input("请输入你的选者：").strip()
        if choice=='1':
            s1.addTodo('1')
        elif choice=='2':
            s1.addTodo('2')
        elif choice =='3':
            s1.show_bill()
        elif choice=='4':
            s1.check_data()
        elif choice=='5':
            s1.del_record()
        elif choice=='6':
            s1.fix_record()
        elif choice=='0':
            break





if __name__ =='__main__':
    main()


