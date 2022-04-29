import hashlib
data = 'Sending encrypted'
data = data.encode('utf-8')
sha3_512 = hashlib.sha3_512(data)
sha3_512_hex_digest = sha3_512.hexdigest()
print('Printing hexadecimal output')
print(sha3_512_hex_digest)

data_2 = 'Sending encrypted'
data_2 = data_2.encode('utf-8')
sha3_512_hex_2 = hashlib.sha3_512(data_2)
sha3_512_hex_digest_2 = sha3_512_hex_2.hexdigest()
print('Printing second hexadecimal output')
print(sha3_512_hex_digest_2)


print('The messages are the same:', sha3_512_hex_digest==sha3_512_hex_digest_2)