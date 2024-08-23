a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

smallest = a
largest = a

if b < smallest:
    smallest = b
if b > largest:
    largest = b

if c < smallest:
    smallest = c
if c > largest:
    largest = c

if d < smallest:
    smallest = d
if d > largest:
    largest = d

print("Smallest number:", smallest)
print("Largest number:", largest)
