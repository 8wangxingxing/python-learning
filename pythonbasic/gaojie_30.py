import functools
price=[1,2,3,4,5,6,7]
price1=list(map(lambda x:x+10,price))
print(price1)
sum_price=sum(price1)

print(sum_price)
sum_price1=functools.reduce(lambda x,y:x+y,price1,0)
print(sum_price1)

price_15=filter(lambda x:x>15,price1)
print(list(price_15))
