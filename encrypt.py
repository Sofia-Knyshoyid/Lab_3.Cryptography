from keys import generate_prime, opposite_mod, second_key_part
# Повідомлення перетворюють у цифрову форму, тобто записують у вигляді
# послідовності цілих чисел.

def to_numline(message):
    code = ""
    for let in message:
        code += str(ord(let) - ord("A")).rjust(2, "0")
    return code

# розбиваємо цей рядок на
# рівного розміру блоки з 2 N цифр, де 2 – N найбільше додатне число таке, що 3232…32 (для
# українського алфавіту), чи 2525…25 (для англійського) із 2 N цифр не перевищує n . У

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

p = generate_prime()
q = generate_prime()
n = p*q
e = second_key_part(p, q)
d = opposite_mod(e, (p-1)*(q-1))

print(f"p: {p}, q: {q}, n: {n}, e: {e}, d: {d}")
print(f"LENBLOCK: {len_block(n)}")

mes = "KATTYLOVESME"
print("numline:", to_numline(mes))
en = encrypt(mes, e, n)
print("Encrypted", en)
print(decrypt(en, d, n))
# print(to_numline("MYFAVOTITETIENDA"))
# en = encrypt("MYFAVOTITETIENDA", e, n)
# print(en)
# print(decrypt(en, d, n))
