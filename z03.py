num = int(input("enter number of ticket:"))
a = 123456
first_num = num // 1000
second_num = num - 1000 * first_num
first_sum = (first_num// 100 + (first_num//10)%10 + first_num % 10)
second_sum = (second_num// 100 + (second_num//10)%10 + second_num % 10)
print(f"is {num} a happy ticket?:")
if first_sum == second_sum:
    print("YES")
else:
    print("NO")

