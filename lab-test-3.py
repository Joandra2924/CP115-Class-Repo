# Programmer : Joandra Joy
# Problem description :  calculates and displays the amount of the bill to be paid after receiving the discount. 

monthly_usage = float(input("Enter monthly usage: "))

if monthly_usage < 50 :
    discount = 0

elif monthly_usage <= 100 :
    discount = 0.05

else : 
    discount = 0.20

bill = monthly_usage * (1 - discount) 

print(f"total bill = RM{bill:.2f}")