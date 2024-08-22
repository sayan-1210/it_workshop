num=int(input("Enter a number: "))
dupnum=num
fact=int(1)
while num!=0:
    fact=fact*num
    num -= 1
print(f"The factorial of {dupnum} is {fact}")