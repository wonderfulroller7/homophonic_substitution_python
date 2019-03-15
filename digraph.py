import json
import message_service
"""
Define a digraph matrix
"""

dimension = 27
# digraph = [[0]*dimension]*dimension

def letter_index_association():
	with open('letter_matrix_association.json','r') as file_object:
		data = json.load(file_object)
	return data

"""
Perfect digraph. Returns a digraph from a message for comparision
"""
def create_perfect_digraph(message):
	digraph = [[0 for x in range(dimension)] for y in range(dimension)]
	matrix_pos = letter_index_association()
	length = len(message) - 2
	for i in range(0, length):
		#print(message[i] + message[i + 1])
		char1 = matrix_pos[message[i]]
		char2 = matrix_pos[message[i + 1]]

		val = digraph[char1][char2] + 1
		digraph[char1][char2] = val
	return digraph


"""
Creates a floating point digraph depending on the output of 1000 messages.
Used for comparision with the present values
"""
def create_frequency_digraph_sample():
	digraph_count = [[0 for x in range(dimension)] for y in range(dimension)]
	digraph = [[0 for x in range(dimension)] for y in range(dimension)]
	messages = []
	for i in range(0,1000):
		digraph_temp = create_perfect_digraph(message_service.create_message())
		for i in range(0,dimension):
			for j in range(0, dimension):
				digraph[i][j] = digraph[i][j] + digraph_temp[i][j]
	for i in range(0,dimension):
		for j in range(0, dimension):
			val = digraph[i][j]/(1000*499)
			digraph[i][j] = float("{0:1.4f}".format(val))
	return digraph
	
def create_frequency_digraph(message):
	digraph = create_perfect_digraph(message)
	for i in range(0,dimension):
		for j in range(0, dimension):
			val = digraph[i][j]/499
			digraph[i][j] = float("{0:1.4f}".format(val))
	return digraph

def score(digraph_sample, digraph_guess):
	score = 0.0
	for i in range(0,dimension):
		for j in range(0, dimension):
			score = score + abs(digraph_sample[i][j] - digraph_guess[i][j])
	return score
