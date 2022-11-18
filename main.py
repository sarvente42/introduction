try:
    PriceOfOne = int(input('Price->>'))
    Amount = int(input('The amount of consoles->>'))
    DiscountInPercentage = float(input('The percentage of discount->>'))
    action = input('action->>')
    Discount = float(DiscountInPercentage / 100)
    PriceOfFew = (PriceOfOne * Amount)

    if action == 'sum of the order without discount':
        print(PriceOfFew)
    elif action == 'sum of the order with discount':
        Discount1 = (PriceOfFew * Discount)
        print(PriceOfFew - Discount1)
    elif action == 'price of one console with discount':
        Discount2 = (PriceOfOne * Discount)
        print(PriceOfOne - Discount2)
except ValueError as vl_er:
    print('Error! Wrong type of function,', vl_er)
