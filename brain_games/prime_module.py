# This module is used in 2 games: brain-gcd and brain-prime


def is_prime(number):
    divisor = number
    number_of_divisors = 0
    i = 1
    while divisor > 0:
        if number % divisor == 0:
            number_of_divisors += 1
        divisor -= 1
        i += 1
    if number_of_divisors == 2:
        return 'yes'
    return 'no'
