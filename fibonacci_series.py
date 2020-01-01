# this is the fibonacci series

num1 = 0
num2 = 1
print(num1)
for i in range(2,51):
    num3 = num1+num2
    num1 = num2
    num2 = num3
    print(num3)
