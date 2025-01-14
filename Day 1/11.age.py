age = input("What is your age?")
print(age, type(age))

age = int(age) #type conversion
if age<18:
    print("minor")
elif age < 30:
        print("young adult")
elif age < 50:
        print("mature")
elif age < 80:
        print("wise")
else:
     print("legacy")