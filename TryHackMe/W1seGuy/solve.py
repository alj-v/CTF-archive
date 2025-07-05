import string
from itertools import product

hex_string = "153f2b3e0870160a2b0c040f12040c3543052e1b00191476192d3b1f2d2d33031f750d330f293705"
xored_bytes = bytes.fromhex(hex_string)

charset = string.ascii_letters + string.digits

def xor_decrypt(data, key):
    return ''.join(chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(data))

for key_tuple in product(charset, repeat=5):
    key = ''.join(key_tuple)
    decrypted = xor_decrypt(xored_bytes, key)
    
    if decrypted.startswith("THM{") and decrypted.endswith("}"):
        print(f"[+] Possible key: {key}")
        print(f"[+] Decrypted: {decrypted}")
        input("Try this one and press Enter to continue...")
