n = int(input('Enter the number: '))
num1 = 0
num2 = 1
nextNumber = num2
count = 1   
while count <= n:
    print(nextNumber, end=" ")
    count = count+1
    num1, num2 = num2, nextNumber
    nextNumber = num1+num2
print()
