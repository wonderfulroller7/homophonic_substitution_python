import message_service
import digraph

message = message_service.create_message()
print(message)
perfect_digraph = digraph.create_perfect_digraph(message)
for i in perfect_digraph:
	print(i)
frequency_digraph_sample = digraph.create_frequency_digraph_sample()
print("Frequency digraph Sample:")
for i in frequency_digraph_sample:
	print(i)
frequency_digraph = digraph.create_frequency_digraph(message)
print("Frequency digraph:")
for i in frequency_digraph:
	print(i)