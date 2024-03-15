# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def generate_primes(n):
#     primes = []
#     num = 2
#     while len(primes) < n:
#         if is_prime(num):
#             primes.append(num)
#         num += 1
#     return primes

# print(generate_primes(20))




# Another way
def is_prime(num):
  """
  This function checks if a number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

count = 0
num = 2
while count < 20:
  if is_prime(num):
    print(num)
    count += 1
  num += 1
