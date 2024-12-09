amount=50

while amount>0:
    print(f"Amount Due: {amount}")
    val=input("Insert Coin: ")
    if val=="5" or val=="10" or val=="25":
        amount-=int(val)

print(f"Change Owed: {-amount}")
