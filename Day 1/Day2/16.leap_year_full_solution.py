start_date= 2001
end_date=2025
##Version 1
print('*'*5+"Allowed year"+"*"*5)
for  year in range(start_date, end_date+1):
    if year % 400 ==0 or (year % 4 ==0 and year % 100 !=0):
        print(year)

print('*'*5+len("Allowed year")*"*"+"*"*5)