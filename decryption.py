"""
Decrypt a cipher text
"""

def decrypt(cipher, decryption_key):
	cipher_key = cipher.split(",")
	message = ""
	for x in cipher_key:
		message = message + decryption_key[int(x)]
	return message