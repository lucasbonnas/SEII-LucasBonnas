weight = float(input("Weight: "))
answer = str.upper((input("(K)g or (L)bs: ")))

if answer == 'K':
    print(f"Weight in Lbs: {weight*2.2}")
elif answer == 'L':
    print(f"Weight in Kg: {weight/0.45}")

