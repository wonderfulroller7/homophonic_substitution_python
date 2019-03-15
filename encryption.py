import random

"""
Return encrypted message
"""
def encrypt(message, key):
	cipher = ""
	for c in message:
		sublist = key[c]
		val = sublist[random.randint(0, len(sublist) - 1)]
		cipher = cipher + str(val) + ","
	length = len(cipher)
	return cipher[:length - 1]