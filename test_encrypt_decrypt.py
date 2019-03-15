import encryption
import decryption
import message_service
import key_service

# Testing encryption
print("Key Guess")
key_map = key_service.generate_key_for_encryption()
print(key_map)
print("message:")
message = message_service.create_message()
print(message)
print("cipher:")
cipher = encryption.encrypt(message, key_map)
print(cipher)
decryption_key = key_service.generate_key_for_decryption(key_map)
print(decryption_key)
message = decryption.decrypt(cipher, decryption_key)
print(message)