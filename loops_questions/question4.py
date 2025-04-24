str = input("Enter your string:\n")
reversed_str = ""
for ch in str:
    reversed_str = ch + reversed_str
    
print(reversed_str)