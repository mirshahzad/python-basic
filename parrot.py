message = input("Tell me something, and I will repeat it back to you: ")
print(message)


# Letting the User Choose When to Quit
prompt = "\Tell me something, and I will repeat it back to you:"
prompt += "\Enter 'quit' to end the program."

message = ""
while message != 'quit':
	message = input(prompt)
	print(message)