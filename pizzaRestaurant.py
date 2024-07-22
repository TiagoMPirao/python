print("Welcome to the pizza restaurant!")

def get_pizza_size():
    while True:
        size = input("What size pizza do you want? (S, M, L) ").upper()
        if size in ("S", "M", "L"):
            return size
        else:
            print("Invalid size. Please provide the size of the pizza EX: S for Small, M for Medium, and L for Large")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).upper()
        if answer in ("Y", "N"):
            return answer
        else:
            print("Invalid input. Please provide Y for Yes, N for No")

size = get_pizza_size()
add_pepperoni = get_yes_no("Do you want pepperoni? (Y for Yes, N for No) ")
extra_cheese = get_yes_no("Do you want extra cheese? (Y for Yes, N for No) ")

if size == "S":
    price = 12
elif size == "M":   
    price = 18
elif size == "L":   
    price = 22

if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    if size == "S":
        price += 1
    else:
        price += 2.5

print(f"Your order has been received. The total price is {price}€. Thank you!")
