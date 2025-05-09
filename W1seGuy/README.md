# W1seGuy – TryHackMe Writeup📈

> **Platform**: TryHackMe  
> **Room**: [W1seGuy](https://tryhackme.com/room/w1seguy)  
> **Category**: Cryptography  
> **Difficulty**: Easy  
> **Completed on**: May 9, 2025  
> **Status**: Completed✅ 

---

## 🧠 Summary

In this room, I learned about XOR encryption and how brute-force can be used to recover unknown keys when the structure of the original message is predictable. The challenge was to connect to a server, receive an XOR-encrypted flag, and discover the encryption key.

---

## 📜 Files

- `solve.py`: Python script I wrote to brute-force the XOR key and recover the flag.
- `notes.txt`: Some personal insights and things I learned.
- `completed.png`: TryHackMe room marked as completed.
- `server.png`: Terminal showing the server connection and decrypted flag using the found key.
- `approach.png`: My solve script + output that cracked the XOR key successfully.
---

## ⚔️ Approach

1. Connected to the challenge server using `nc`.
2. Analyzed the provided Python script which XORs the flag using a 5-character key.
3. Extracted the encrypted flag string from the server.
4. Brute-forced all possible 5-character alphanumeric keys.
5. Checked for valid flag format (`THM{}`) in the decrypted result.
6. Sent the key back to the server and received the real flag.

---

## ⚡ Flag

|||
|---|---|
|**Key**| `AwfEx` *(replace with actual)* |
|**Flag1**| `THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}` |
|**Flag2**| `THM{BrUt3_ForC1nG_XOR_cAn_B3_FuN_nO?}` |
---

## 💭 Reflections

This room gave me a deeper understanding of XOR operations and how dangerous it is to use predictable key sizes. Also, it felt amazing writing a script that *actually cracked something real!* 😎

---

> ✨ "From curiosity to code — this is just the beginning!"  
> aleenjoyvettiyadan_
