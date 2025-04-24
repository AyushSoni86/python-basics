num = int(input("Enter a number: "))
isPrime = True
for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break

print("Number is prime" if isPrime else "Not a prime number")