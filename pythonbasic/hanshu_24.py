def number_total(numbers):
    total=0;
    for i in numbers:
        if i%2==0:
            total=total+i
    return total
numbers=[1,2,3,4,5,6,7,8,9]
print(number_total(numbers))