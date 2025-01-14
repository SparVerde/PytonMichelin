 # how to end with cycle with break or with True/False variabels

EUR = 4.97
USD = 4.87
HUF = 0.012
PLN = 1.16

amount = int(input("Please insert yot=r amount in RON\n"))
currency = input("Please insert the currency you want to convert to (EUR, USD, HUF, PLN)\n")
currency = currency.upper() #cover case when EUR is not well written

while True:

#print(currency)
#or while should continue = True
#and put should continue = False after else should continue = True
    if currency =="EUR": #or currency =="eur":
        print("Sum in EUR = ", amount / EUR)
        break #put break
    elif currency =="USD":
        print("Sum in USD = ", amount / USD)
        break
    elif currency =="HUF":
        print("Sum in HUF = ", amount / HUF)
        break
    elif currency =="PLN":
        print("Sum in PLN = ", amount / PLN)
    else:
        currency = input("Please insert the currency you want to convert to (EUR, USD, HUF, PLN)\n")
        currency = currency.upper() #cover case when EUR is not well written
        

