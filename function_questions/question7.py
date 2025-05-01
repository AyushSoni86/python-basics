def sum_all(*args):
    print("Arguments with asterik: ", *args)
    print("Argusments without asterik: ", args)
    for i in args:
        print(i * 23, end=" ")
    return sum(args)
    
    
print(sum_all(1, 2, 3, 4, 5, 6))