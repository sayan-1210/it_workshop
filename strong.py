import math

num = int(input("Enter a number: "))
temp = num
sum_fact = 0

while num > 0:
    digit = num % 10
    sum_fact += math.factorial(digit)
    num //= 10

if sum_fact == temp:
    print(f"{temp} is a Strong number.")
else:
    print(f"{temp} is not a Strong number.")
