age = int(input("Please enter your age: "))

if age < 13:
    print("Child")
elif age > 12 and age <= 19:
    print("Teenager")
elif age > 19 and age < 59:
    print("Adult")
else:
    print("Senior")