a = 1500
print("Bill amount:",a)
Mo = input("Please specify the payment mode:")
Mo = Mo.upper()
if Mo == "CREDIT CARD":
             discount = 10
             print("Discount: 10% of the bill amount")
elif Mo == "DEBIT CARD":
             discount = 5
             print("Discount: 5% of the bill amount")
elif Mo == "NET BANKING":
             discount = 2
             print("Discount: 2% of the bill amount")
else:
             discount = 0
             print("Discount: 0")
b = a - discount*a/100
print("Net Amount",b)
