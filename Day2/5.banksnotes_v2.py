enter = True
#print(enter)
while enter:
    initial_amount = input("Enter the amont\n")
    amount = int(initial_amount)
    banknotes = [100,50,20,10,5,1]
    #print(amount, type(amount))
    #i=0
    for note in banknotes:
        value = amount//note
        
        #print("Banknotes of ",note, ":", value)
        print(f"Banknotes of {note} :{value}")
        amount = amount%note
        
    #print("Do you want a new calculation? yes or no\n")
   
    response = input("Do you want a new calculation? yes/no\n") 
    enter = response =='yes'
    #print(enter)
        