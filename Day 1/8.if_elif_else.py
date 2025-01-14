age=50

#version 1
if age<18:
    print("minor")
else:
    #print("adult")
    if age < 30:
        print("young adult")
    else:
        if age < 50:
            print("mature")
        else:
            if age < 80:
                print("wise")
            else:
                print("legacy")

#version 2
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