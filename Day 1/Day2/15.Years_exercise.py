#start_date= int(input("Please give the start date in YYYY:\n"))
#end_date=int(input("Please give the end date in YYYY:\n"))
start_date= 2000
end_date=2025
if end_date< start_date:
    end_date=int(input("Please give the end date in which is bigger tan start date YYYY:\n"))
l=[]
lenght = end_date-start_date
#print(lenght)
for i in range((lenght)+1): #for i in range(start_date, end_date+1)
     l.append(start_date+ i)
print("*"*5,"Allowed years","*"*5)
#print(len(l))
for i in range(len(l)):
    print(l[i])

print('*'*5+len("Allowed year")*"*"+"*"*5)

#Leap Years V1 - every 4 years: even = [i for i in l if i % 2 == 0]
Leap_year=[]
Leap_year = [l[i] for i in range(len(l)) if l[i] % 4 == 0]
print('*'*5+"Leap year"+"*"*5)
for i in range(len(Leap_year)):
    print(Leap_year[i])
print('*'*5+len("Leap year")*"*"+"*"*5)
#other solution:
#if start_date%4 ++0:
    #first_leap_year = start_date //4*4+4
#else:
    #first_lleap_year = start_date

#Leap Years V2 - a. if divisible by 400, b. is not divisible by 100 and not by 400, c. is divisiblw by 4 but not by 100
#a
Leap_year_400=[]
Leap_year_400 = [l[i] for i in range(len(l)) if l[i] % 400 == 0]
print('*'*5+"Leap year"+"*"*5)
for i in range(len(Leap_year_400)):
    print(Leap_year_400[i])
print('*'*5+len("Leap year")*"*"+"*"*5)
#b

