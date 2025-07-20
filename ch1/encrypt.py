# one time pad encryption
# dummy data + original data -> Product (encrypted text)
# need both the dummy data and product to decrypt the text

#dummy data must be same length as original
#dummy data must be truly random 
#dummy data must be completely secret

import secrets

def random_key(length: int) -> int:
    tb: bytes = secrets.token_bytes(length)
    return int.from_bytes(tb, 'big')

def encrypt(original: str) -> tuple[int, int]:
    original_bytes: bytes = original.encode()
    original_key: int = int.from_bytes(original_bytes, 'big')
    dummy: int = random_key(len(original_bytes))
    encrypted: int = original_key ^ dummy

    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    xor: int = key1 ^ key2
    byte_str = xor.to_bytes((xor.bit_length() + 7) // 8, 'big')
    return byte_str.decode()