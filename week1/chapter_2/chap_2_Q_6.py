weight = float(input("Enter the package weight: "))
method = input("Enter the shipping method (ground/priority/express): ")
def calculate_shipping_cost(weight, method):
    if method == "ground":
        if weight <= 2:
            cost = 1.5
        elif weight <= 5:
            cost = 3.0
        elif weight <= 10:
            cost = 4.0
        else:
            cost = 4.75
    elif method == "priority":
        if weight <= 2:
            cost = 3.5
        elif weight <= 5:
            cost = 5.5
        elif weight <= 10:
            cost = 7.0
        else:
            cost = 8.5
    elif method == "express":
        if weight <= 2:
            cost = 4.5
        elif weight <= 5:
            cost = 7.5
        elif weight <= 10:
            cost = 9.5
        else:
            cost = 12.0
    else:
        raise ValueError("Invalid shipping method")
    
    return cost


cost = calculate_shipping_cost(weight, method)
print("Shipping cost: $", cost)