# Day 1: Python Basics

# Python Shell
# The interactive interpreter allows us to execute Python code directly.
# >>> is the Python prompt.

# 1. Basic Calculations
print(1 + 2)
print(3 / 2.4)
print(3 * 9)

# 2. Variables and Strings
a = 1
b = 2

print(a + b)

name = "Python"
print(name)

# 3. Conditional Statements
a = 3

if a > 1:
    print("a is greater than 1")

# 4. For Loop
for a in [1, 2, 3]:
    print(a)

# 5. While Loop
i = 0

while i < 3:
    i = i + 1
    print(i)

# 6. Functions
def sum_numbers(a, b):
    return a + b

print(sum_numbers(3, 4))
