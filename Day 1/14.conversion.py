EUR = 4.97
USD = 4.87
HUF = 0.012
PLN = 1.16

amount = int(input("Please insert yot=r amount in RON\n"))
currency = input("Please insert the currency you want to convert to (EUR, USD, HUF, PLN)\n")
currency = currency.upper() #cover case when EUR is not well written

while currency != "EUR" and currency != "USD" and currency != "HUF" and currency != "PLN":
    currency = input("Please insert the currency you want to convert to (EUR, USD, HUF, PLN)\n")
    currency = currency.upper() #cover case when EUR is not well written

#print(currency)
if currency =="EUR": #or currency =="eur":
    print("Sum in EUR = ", amount / EUR)
elif currency =="USD":
    print("Sum in USD = ", amount / USD)
elif currency =="HUF":
    print("Sum in HUF = ", amount / HUF)
elif currency =="PLN":
    print("Sum in PLN = ", amount / PLN)

   