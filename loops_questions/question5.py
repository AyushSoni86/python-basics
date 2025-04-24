str = input("Enter your string:\n")

for char in str:
    if str.count(char) == 1:
        print(char)
        break
    

