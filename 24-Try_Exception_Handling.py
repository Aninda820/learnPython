print("Enter 1st numebr")
num1 = input()
print("Enter 2nd number")
num2 = input()
try:
    print("The sum of these two numbers is ",int(num1) +int(num2))
except Exception as e:
    print(e)

print("This line is very inportent")