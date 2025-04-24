coffee_size = input("Provide the coffee size you want\n")
is_extra_shot = int(input("Do you want Extra shot of Espresso\n"))

if is_extra_shot:
    print(coffee_size, 'coffee with extra espresso shot')
else:
    print(coffee_size)