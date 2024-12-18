cost_price=int(input("enter a cost price"))
selling_price=int(input("enter a selling price"))
amount=selling_price-cost_price
if amount<0:
    print("seller has loss{}".format abs(amount))
else:
    print("seller has profit{}".format(amount))