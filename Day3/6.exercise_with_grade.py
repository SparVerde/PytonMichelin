Grade={
'1':'Insuffisent', '2':'Suffisent', '3':'Average grade', '4':'Good', '5':'Excellent'
}
#Version 1

i= input("Grade? ")
#verify is key exist
print("Version 1")
is_key_found = False
for k in Grade:
    if k == i:
        print(Grade[i] )
        is_key_found = True
if not is_key_found:
    print("The grade doesn't exist")

#Version 2
print("Version 2")
for k in Grade:
    if k == i:
        print(Grade[i])
        break
    else: 
        print("key not foud")

#Version 3
print("Version 3")
if i in Grade:
    print(Grade[i])
    
else: 
    print("key is not foud")


#Version 4
print("Version 4")
print(Grade.get
      (i,"Key not foud"))