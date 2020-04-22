for n in range(int(input())):
    income=int(input())
    if (income >= 0) and (income <= 250000):
        tax = (0*income)
        print(int(income-tax))
    elif (income >250000) and (income <=500000):
        tax = (0.05 * (income-250000))
        print(int(income-tax))
    elif (income >500000) and (income <=750000):
        tax = ((0.05*(500000-250000)) + (0.10*(income-500000)))
        print(int(income-tax))
    elif (income >750000) and (income <= 1000000):
        tax = ((0.05*(500000-250000)) + (0.10*(750000-500000)) + (0.15*(income-750000)))
        print(int(income-tax))
    elif (income > 1000000) and (income <= 1250000):
        tax = ((0.05*(500000-250000)) + (0.10*(750000-500000)) + (0.15*(1000000-750000)) +(0.2*(income-1000000)))
        print(int(income-tax))
    elif (income > 1250000) and (income <= 1500000):
        tax = ((0.05*(500000-250000)) + (0.10*(750000-500000)) + (0.15*(1000000-750000)) +(0.2*(1250000-1000000))+ (0.25*(income-12500000)))
        print(int(income-tax))
    elif (income > 1500000):
        tax = ((0.05*(500000-250000)) + (0.10*(750000-500000)) + (0.15*(1000000-750000)) +(0.2*(1250000-1000000))+ (0.25*(1500000-12500000))+ (0.30*(income-15000000)))   
        print(int(income-tax))
    else:
        pass
    
