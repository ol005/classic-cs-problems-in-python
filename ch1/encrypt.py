# one time pad encryption
# dummy data + original data -> Product (encrypted text)
# need both the dummy data and product to decrypt the text

#dummy data must be same length as original
#dummy data must be truly random 
#dummy data must be completely secret

#Challenge question 1.7-4
#Use a one-time pad to encrypt and decrypt images.



import secrets
import sys

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

def encrypt_img(original: bytes) -> tuple[int, int]:
    original_key: int = int.from_bytes(original, 'big')
    dummy: int = random_key(len(original))
    encrypted: int = original_key ^ dummy

    return dummy, encrypted

def decrypt_img(key1: int, key2: int) -> bytes:
    xor: int = key1 ^ key2
    byte_str = xor.to_bytes((xor.bit_length() + 7) // 8, 'big')
    return byte_str

#encrypt and rewrite the input jpg
def main() -> None:
    sys.set_int_max_str_digits(10000000)
    with open('ch1/imgs/bunny_s.jpg', 'rb') as image:
        f: bytes = image.read()
    b: bytes = bytes(f)
    dummy: int
    encrypted: int 
    dummy, encrypted = encrypt_img(b)
    de_c: bytes = decrypt_img(dummy, encrypted)
    print(f"dummy: {dummy}, encrypt: {encrypted}")
    print(b == de_c)

    with open('ch1/imgs/bunny_decrypted.jpg', 'wb') as output_img:
        output_img.write(de_c)
    #print(b)
if __name__ == '__main__':
    main()