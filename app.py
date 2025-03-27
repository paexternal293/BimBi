def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number_prime = 17
print(f"Is {number_prime} a prime number? {is_prime(number_prime)}")

number_factorial = 5
print(f"Factorial of {number_factorial} is {factorial(number_factorial)}")