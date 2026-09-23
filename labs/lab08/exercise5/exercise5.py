main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    main_cost = 10
elif main_course == "Beef":
    main_cost = 12
else :
    main_cost = 11

if drink == "Soft Drink":
    drink_cost = 2
else :
    drink_cost = 3

if dessert == "Ice Cream":
    dessert_cost = 4
else :
    dessert_cost = 5

service_charge = float(main_cost + drink_cost + dessert_cost)*0.10
final_bill = float(main_cost + drink_cost + dessert_cost + service_charge)

print(f"{final_bill:.2f}")
