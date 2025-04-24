num = int(input("enter a number: "))
temp = num
result = 1
while temp > 0:
    result *= temp
    temp-=1
print(result)