"""Module for encrypting and decrypting """
from keys import generate_prime, opposite_mod, second_key_part

def to_numline(messege):
    """Converts a messege into a number line."""
    code = ""
    for let in messege:
        code += str(ord(let) - ord("A")).rjust(2, "0")
    return code

def len_block(n_value):
    """Returns a N value."""
    if n_value < 26:
        return 0
    count = 1
    start = 25
    while True:
        end = start * 100 + 25
        if start < n_value < end:
            return count
        start = end
        count += 1

def modular_pow(base, exp, mod):
    """Memory-efficient modular power"""
    if mod == 1:
        return 0
    c_val = 1
    e_prime = 0
    while e_prime < exp:
        c_val = c_val * base % mod
        e_prime += 1
    return c_val


def block_split(message, n_value):
    """Splits  the code into even 2N parts."""
    return  list(map(''.join, zip(*[iter(message)]* 2*len_block(n_value))))

def encrypt(message, e_val, n_val):
    """Encrypts the message."""
    numline = to_numline(message)
    blocks = block_split(numline, n_val)
    # print(blocks)
    encoded = ""
    for block in blocks:
        encoded += str( modular_pow(int(block), e_val, n_val)).rjust(len(block), "0")
    return encoded

def to_wordline(encoded):
    """Turns a number line to a word line."""
    message = ""
    blocks = list(map(''.join, zip(*[iter(encoded)]*2)))
    for let in blocks:
        message += chr(int(let) + ord("A"))
    return message

def decrypt(encoded, d_val, n_val):
    """Decrypts an encoded message."""
    blocks = block_split(encoded, n_val)
    # print(blocks, "Dec")
    decoded = ""
    for block in blocks:
        decoded += str(modular_pow(int(block), d_val, n_val)).rjust(len(block), "0")
    return to_wordline(decoded)


def check_messege(num):
    """
    Defines length of required block.
    Edits the message if needed.
    """
    if num % 3 == 0:
        return 3
    if num % 2 == 0:
        return 2
    return 1

def gener_keys_get_message(message="ABCDEFH"):
    block_need = check_messege(len(message))
    print(block_need)
    print(f'the message for processing is: {message}')
    lenb = 0

    while (lenb != block_need):
        p = generate_prime(block_need)
        q = generate_prime(block_need)
        n = p*q
        if p != q:
            lenb = len_block(n)

    e = second_key_part(p, q)
    d = opposite_mod(e, (p-1)*(q-1))

    print(f"p: {p}, q: {q}, n: {n}, e: {e}, d: {d}")
    print(f"LENBLOCK: {len_block(n)}")

    print("numline:", to_numline(message))
    return message, e, n, d


def encrypt_message(mes, e, n):
    en = encrypt(mes, e, n)
    # print("Encrypted", en)
    return en

# block_need = check_messege(len(en)//2)

def decrypt_message(en, d, n, edited):
    de = decrypt(en, d, n)
    # print(de)
    return de
