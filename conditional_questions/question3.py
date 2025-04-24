score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
    print('Grade is A')
elif score >= 80 and score <= 89:
    print('Grade is B')
elif score >= 70 and score <= 79:
    print('Grade is C')
elif score >= 60 and score <= 69:
    print('Grade is D')
else:
    print('Grade is F')

