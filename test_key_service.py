import key_service
from pprint import pprint

pprint(key_service.get_frequency_map())
print("Key used for encryption")
key_map = key_service.generate_key_for_encryption() 
print(key_map)
print("Key used for decryption")
print(key_service.generate_key_for_decryption(key_map))