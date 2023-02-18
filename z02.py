num = int(input("enter count:"))

if num % 6 == 0 :
    Petya = num // 6
    Serega = Petya
    Katya = num - (Serega + Petya)
    print(f"Katya make: {Katya} cranes, Serega makes: {Serega} cranes, Petya make: {Petya} cranes")
else:
    print("incorrect number, this can't be true!!!")





