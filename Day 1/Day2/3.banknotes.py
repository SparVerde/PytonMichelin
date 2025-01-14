enter = True
#print(enter)
while enter:
    amount = input("Enter the amont\n")
    amount = int(amount)
    #print(amount, type(amount))
    Tens = amount//10
    Remains = amount%10
    print(Tens, Remains)
    Fives = Remains//5
    Remains = amount%5
    Twos = Remains//2
    Remains = Remains%2
    Ones = Remains//1
    Remains = Remains%1
    print("Enter Amount ", amount, "\nTens : ",Tens, "\nFives : ",Fives, "\nTwo\'s : ",Twos, "\nOnes : ",Ones)
    
    #print("Do you want a new calculation? yes or no\n")
   
    response = input("Do you want a new calculation? yes/no\n") 
    enter = response =='yes'
    #print(enter)
        











