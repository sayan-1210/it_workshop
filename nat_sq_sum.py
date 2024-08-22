n = int(input("Enter the range: "))

total_sum = 0
for i in range(1, n + 1):
    total_sum += i ** 2

print(f"The summation of the squares of natural numbers up to {n} is {total_sum}")
