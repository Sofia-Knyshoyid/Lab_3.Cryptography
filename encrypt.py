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
    count = 1
    start = 25
    while True:
        end = start * 100 + 25
        if start < n_value < end:
            return count
        start = end
        count += 1

def block_split(message, n_value):
    """Splits  the code into even 2N parts."""
    return  list(map(''.join, zip(*[iter(message)]* 2*len_block(n_value))))

def encrypt(message, e_val, n_val):
    """Encrypts the message."""
    numline = to_numline(message)
    blocks = block_split(numline, n_val)
    print(blocks)
    encoded = ""
    for block in blocks:
        encoded += str(int(block)**e_val % n_val).rjust(len(block), "0")
        # print(str(int(block)**e_val % n_val).rjust(len(block), "0"), "ENC")
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
    print(blocks, "Dec")
    decoded = ""
    for block in blocks:
        decoded += str(int(block)**d_val % n_val).rjust(len(block), "0")
    return to_wordline(decoded)


def check_messege(messege):
    """
    Defines length of required block.
    Edits the message if needed.
    """
    len_m = len(messege)
    len_bl = 0
    edited = False
    if len_m % 2 == 0:
        len_bl = 2
    elif len_m % 3 == 0:
        len_bl = 3
    else:
        len_bl = 2
        edited = True
        messege = messege + "A"
    return len_bl, messege, edited


messege_7 = "ABCDEFH"
block_need, mes, edited_7 = check_messege(messege_7)
print(block_need, mes, edited_7 )
lenb = 0
while lenb != block_need:
    p = generate_prime(block_need)
    q = generate_prime(block_need)
    n = p*q
    print(n, p, q)
    lenb = len_block(n)

e = second_key_part(p, q)
d = opposite_mod(e, (p-1)*(q-1))

print(f"p: {p}, q: {q}, n: {n}, e: {e}, d: {d}")
print(f"LENBLOCK: {len_block(n)}")

print("numline:", to_numline(mes))
en = encrypt(mes, e, n)
print("Encrypted", en)
de = decrypt(en, d, n)

if edited_7:
    print(de[:-1])
else:
    print(de)
