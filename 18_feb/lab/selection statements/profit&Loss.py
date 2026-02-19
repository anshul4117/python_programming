# Wap to calculate profit and loss

cost_price = float(input("Enter cost price (in RS) : "))

if(cost_price <= 0):
    print("cost Price should be positive")
    exit()
else:
    sell_price = float(input("Enter sell price : (in RS) "))
    if(sell_price <= 0):
        print("sell Price should be positive")
        exit()
    else:
        if(cost_price > sell_price):
            print("loss", cost_price - sell_price)
            exit()
        elif(cost_price < sell_price):
            print("profit", sell_price - cost_price)
            exit()
        else:
            print("No profit No loss")