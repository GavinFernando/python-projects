# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for num in range(30,81):
    if num % 4 == 0:
        print(num, end=", ")  # new line
print()

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
for i in range (15,31,2):
    if i%2 == 1:
        print(i, end=", ")  # new line
print()

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for num in range(50,9,-5):
    print(num, end=", ")  # new line
print()

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
product = 1
for num in range(3, 31, 3):  # stepping by 3 directly
    product *= num
print(product)
print()
