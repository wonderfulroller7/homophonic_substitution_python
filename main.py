import message_service
import key_service
import encryption
import decryption
import digraph
import time

message = message_service.create_message()
key = key_service.generate_key_for_encryption()
cipher = encryption.encrypt(message, key)
digraph_sample = digraph.create_frequency_digraph_sample()
print("Cipher:")
print(cipher)
timestr = time.strftime("%Y%m%d-%H%M%S")
write_log = open("logs/log"+timestr+".log", "a")
key_temp = key_service.generate_key_for_encryption()
key_guess = key_service.generate_key_for_decryption(key_temp)
for i in range(1,51):
	write_log.write("Guess " + str(i) + "\n")
	write_log.write("=======================\n")
	print("Message guess:")
	message_guess = decryption.decrypt(cipher, key_guess)
	print(message_guess)
	digraph_guess = digraph.create_frequency_digraph(message_guess)
	score = digraph.score(digraph_sample, digraph_guess)
	print("Score = " + str(score))
#	for i in key_guess:
#		write_log.write(i + " ")
	write_log.write("Score = " + str(score) + "\n")
	write_log.write("message guess before swap:"+"\n")
	write_log.write(message_guess+"\n")
	for distance in range(1,106):
		old_key = key_guess.copy()
		for i in range(0, 106 - distance):
			if (key_guess[i] != key_guess[i + distance]):
				key_swap_temp = key_service.key_swap(key_guess, i, distance)
				msg_temp_guess = decryption.decrypt(cipher, key_swap_temp)
				if "  " in msg_temp_guess or msg_temp_guess[0] == " ":
					#print("Key Discarded")
					key_guess = old_key.copy()
					#print("Old key restored")
					#print(key_guess)
					continue
				else:
					digraph_temp = digraph.create_frequency_digraph(msg_temp_guess)
					swap_score = digraph.score(digraph_sample, digraph_temp)
					if swap_score < score :
						key_guess = key_swap_temp.copy()
						#print("Updating key guess:")
						#print(key_guess)
						score = swap_score
write_log.close()