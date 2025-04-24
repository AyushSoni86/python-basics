num = int(input("Enter a number: "))
even_sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        even_sum+=i
print(even_sum)