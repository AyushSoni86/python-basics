age = int(input('Enter your age: '))
isWednesday = int(input('Is is Wednesday?\n'))

price = 12 if age >= 18 else 8

if isWednesday:
    print('You get a 2$ discount: ', price - 2)
else:
    print(price)