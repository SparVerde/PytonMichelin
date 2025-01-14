age =18
#mutual exclusive
#right:
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


#mutual exclusive
#not right:
if age<18:
    print("minor?")
if age < 30:
        print("young adult?")
if age < 50:
        print("mature?")
if age < 80:
        print("wise?")
else:
     print("legacy?")

#not right:
if age<18:
    print("minor??")
if age >=18 and age < 30:
        print("young adult??")
if age >30 and age < 50:
        print("mature??")
if age >50 and age < 80:
        print("wise??")
else:
     print("legacy??") #in this case put if for last in cases

#right:
if age<18:
    print("minor???")
if age >=18 and age < 30:
        print("young adult???")
if age >30 and age < 50:
        print("mature???")
if age >50 and age < 80:
        print("wise???")
if age >80:
     print("legacy??") #in this case put if for last in cases