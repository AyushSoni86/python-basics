color = input("Enter the color: ")
banana_color = color.lower()

if banana_color == 'green':
    print("Unripe")
elif banana_color == 'yellow':
    print("Ripe")
elif banana_color == 'brown':
    print("Overripe")
else:
    print("Enter a valid color")
        