person={
'张三':{"年龄":'10','职业':'学生','居住城市':'北京'},
'王兴':{'年龄':'10','职业':'学生','居住城市':'北京'},
'小明':{'年龄':'10','职业':'学生','居住城市':'北京'}
        }
print(person)
print(person['王兴'])
del person['张三']
print(person)
person['ji']={'年龄':'11','职业':'学生','居住城市':'北京'}
print(person)
if input('删除信息输入y，否则是n')=='y':
    del person['ji']
print(person)