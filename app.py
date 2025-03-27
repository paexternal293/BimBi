def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"Divisor found: {i}")
            return False
    return True

number = 17
print(f"Is {number} a prime number? {is_prime(number)}")

# This is a modification in the main branch.
