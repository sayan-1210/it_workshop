ran=int(input("Enter a number: "))
num1=0
num2=1
print(f"The fibonacci series of range {ran} is")
if ran==1:
    print(num1)
else:
    print(f"{num1}\n{num2}")
for i in range(ran-2):
    temp=num2
    num2=num1+num2
    num1=temp
    print(f"{num2}")