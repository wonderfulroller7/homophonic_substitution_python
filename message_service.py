import random

def create_message(length=500):
	dictionary = []
	message = ""
	with open('english_words.txt', 'r') as file_object:
		for line in file_object:
				dictionary.append(line.replace("\n","").strip())
	while (len(message) <= length):
		message = message + dictionary[random.randint(0,len(dictionary) - 1)]
		message = message + " "
	return message[:500]
