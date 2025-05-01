def print_key_values(**kwargs):
    print(kwargs.items())
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} = {value}")
    
    
print_key_values(name="Ayush", address="Pune", age="23")
