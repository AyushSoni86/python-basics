pet_species = input("Enter your pet species:\n").lower()
pet_age = int(input("Enter your pet's age:\n"))

if pet_species == 'cat':
    if pet_age > 5:
        print("Senior Cat food")
    else:
        print("Junior Cat food")
        
elif pet_species == 'dog':
    if pet_age < 2:
        print("Puppy food")
    else:
        print("Dogs food")