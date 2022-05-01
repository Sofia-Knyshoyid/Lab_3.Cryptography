"""Method keys generator."""
from random import randint

def is_prime(num):
    """Checks if the number is prime."""
    for div in range(2, int(num**0.5) + 1):
        if num % div == 0:
            return False
    return True

def generate_prime(blocksize):
    """Generates a prime number."""
    prime = False
    while prime is False:
        num = randint(2, 10**blocksize)
        if is_prime(num):
            return num

def gcd(value_a, value_b):
    """Returns a greatest common divider."""
    while value_b != 0:
        value_a, value_b = value_b, value_a % value_b
    return value_a

def second_key_part(value_p, value_q):
    """Returns a coprime integer for (p−1)*(q−1)."""
    co_prime = (value_p-1)*(value_q-1)
    is_co_prime = False
    while is_co_prime is False:
        num = randint(2, 100)
        if gcd(num, co_prime) == 1:
            is_co_prime = True
    return num

def opposite_mod(coef, mod):
    """Returns an opposite by mod calculated with extended euclidead"""
    s_c , t_c = [1, 0], [0, 1]
    first, second = max([coef%mod, mod]), min([coef%mod, mod])
    remainder = first % second
    while remainder!=0:
        fraction = first // second
        s_c.append(s_c[-2] - fraction * s_c[-1])
        t_c.append(t_c[-2] - fraction * t_c[-1])
        first = second
        second = remainder
        remainder = first % second
    return t_c[-1] % mod


p = generate_prime(3)
q = generate_prime(3)
n = p*q
e = second_key_part(p, q)
d = opposite_mod(e, (p-1)*(q-1))
