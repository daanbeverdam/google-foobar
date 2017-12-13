
"""Solution to Google challenge Re-ID"""

ID_LENGTH = 5  # minion ID length


def stitch_list(l):
    """Stitches list of integers together and returns it as string."""
    l = [str(i) for i in l]  # Convert all elements to string
    l = ''.join(l)  # Stitch them together
    return l


def is_prime(number, prime_numbers):
    """Checks if number is prime, given all previous prime numbers. Returns truth value."""
    # Take square root of number and remove all primes below it from list:
    square_root = number ** (1 / 2.0)
    prime_numbers = [n for n in prime_numbers if n <= square_root]

    # Loop through already known primes:
    for prime in prime_numbers:

        # If number is divisible by a prime, it is composite:
        if number % prime == 0:
            return False

    # If the number is not divisible by any prime, it is a prime:
    return True


def generate_prime_numbers(length):
    """Returns string of concatenated prime numbers of at least the specified length."""
    prime_numbers = [2]  # Two is the only even prime, so it gets a special treatment
    number = 3  # We'll start the search at 3

    # Keep running while string length is under specified length:
    while len(stitch_list(prime_numbers)) < length:

        # If number is prime, add to list:
        if is_prime(number, prime_numbers):
            prime_numbers.append(number)

        number += 2  # Increase the number by two, because even numbers are never primes

    return prime_numbers


def answer(n):
    """Main function. Returns minion ID as string. Accepts index."""
    needed_length = n + ID_LENGTH + 1  # String length needed based on given index
    prime_numbers = generate_prime_numbers(needed_length)  # Generate prime numbers
    prime_string = stitch_list(prime_numbers)  # Stitch them together
    minion_id = prime_string[n:n + 5]  # ID slice
    return minion_id
