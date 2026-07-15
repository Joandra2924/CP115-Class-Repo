income = float(input())
if income <= 50000.0:
    totalTax = 0
else:
    if income <= 50000.0:
        totalTax = (income - 50000.0)* 0.01
    else:
        totalTax = (50000.0 * 0.01) + (income - 50000.0) * 0.02
print(totalTax)
