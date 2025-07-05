from binascii import unhexlify
from itertools import cycle

# Step 1: Load the data from out.txt
with open("out.txt", "r") as f:
    lines = f.read().splitlines()

iv_hex = lines[0]
enc_msg_hex = lines[1]
enc_flag_hex = lines[2]

# Step 2: Decode
iv = unhexlify(iv_hex)
enc_msg = unhexlify(enc_msg_hex)
enc_flag = unhexlify(enc_flag_hex)

# Step 3: Known plaintext
plaintext = (
    b"Our counter agencies have intercepted your messages and a lot "
    b"of your agent's identities have been exposed. In a matter of "
    b"days all of them will be captured"
)

# Step 4: Derive keystream
keystream = bytes([p ^ c for p, c in zip(plaintext, enc_msg)])

# Step 5: Decrypt flag
flag = bytes([k ^ c for k, c in zip(keystream, enc_flag)])
print(f"Flag: {flag.decode()}")
