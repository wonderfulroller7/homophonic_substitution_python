import json
import random
import digraph

"""
Returns the outer hill climibing assignment i.e
the frequency map
"""
def get_frequency_map():
	with open('frequency.json','r') as file_object:
		data = json.load(file_object)
	return data

"""
Returns a key for encryption in dictionary pattern
"""
def generate_key_for_encryption() :
	frequency_map = get_frequency_map()
	key_map = {}
	used_index = []
	for key in frequency_map:
		sub_list = []
		while (len(sub_list) != frequency_map[key]):
			index = random.randint(0,105)
			if index not in used_index:
				sub_list.append(index)
				used_index.append(index)
		key_map[key] = sub_list
	return key_map

"""
Returns key for decrytion in array pattern
"""
def generate_key_for_decryption(key_map):
	decrypt_key = [0]*106
	for key in key_map:
		for val in key_map[key]:
			try:
				decrypt_key[val] = key
			except:
				print("Exception at " + str(val))
	return decrypt_key

"""
Swaps key using distances
"""
def key_swap(key, pos, distance):
#	print("Before swap:")
#	print(key)
#	print("Swapping {},{} with {},{}".format(key[pos],pos,key[pos+distance], pos+distance))
	temp = str(key[pos])
	key[pos] = str(key[pos + distance])
	key[pos + distance] = temp
#	print("After swap:")
#	print(key)
	return key