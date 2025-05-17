# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

def prime_factors(n):
    factors = []
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    
    my_set=set(factors)
    length=len(my_set)
    return length

def main():
    number = int(input("Enter a number to find its prime factors: "))
    factors = prime_factors(number)
    print(f"Prime factors of {number} are: {factors}")

if __name__ == "__main__":
    main()       