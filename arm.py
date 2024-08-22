num = int(input("Enter a number: "))
sum_pow = 0
n_digits = len(str(num))
org_num = num

while num > 0:
    digit = num % 10
    sum_pow += digit ** n_digits
    num //= 10

if sum_pow == org_num:
    print(f"{org_num} is an Armstrong number")
else:
    print(f"{org_num} is not an Armstrong number")
