# Solution 1

def factorial(n):
	if n < 0:
		return 0
	elif n == 0 or n == 1:
		return 1
	else:
		fact = 1
		while(n > 1):
			fact = fact * n
			n -= 1
		return fact

# Driver Code
num = int(input('Enter the number: '))
print("Factorial of",num,"is",factorial(num))






# Solution 2
def factorial(n):
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# Driver Code
num = int(input('Enter the number: '))
print(f"Factorial of {num} is {factorial(num)}")