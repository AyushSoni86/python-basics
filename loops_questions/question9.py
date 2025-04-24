items = ["apple", "banana", "orange", "apple", "mango"]
unique_set = set()
for item in items:
    if item in unique_set:
        print(item)
        break
    unique_set.add(item)
