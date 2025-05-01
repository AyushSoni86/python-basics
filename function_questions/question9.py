def even_generator(limit):
    for i in range(1, limit, 2):
        yield i
        
        
for i in even_generator(10):
    print(i)