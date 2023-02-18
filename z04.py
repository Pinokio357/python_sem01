n = int(input("enter 'n' of chokolad:"))
m= int(input("enter 'm' of chokolad:"))
k = int(input("enter 'k' of chokolad:"))
if ((k % n == 0) or (k % m == 0)) and k < m * n:
    print("it is possible")
else:
    print("NO")




