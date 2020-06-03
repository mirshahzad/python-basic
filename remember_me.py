import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
	json.dump(username, f)
	print(f"We'll remember you when you come back, {username}! ")



import json

# Load the username, if if has been stored previously.
# Otherwise, prompt for the username and store it.
def greet_user():
	"""Greet the usr by name. """

filename = 'usrname.json'
try:
	with open(filename)as f:
		usrname = json.load(f)
except FileNotFoundError:
	usrname = input("What is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
		print(f"We'll remember you when you come back, {username}!")
else:
	print(f"Welcome back, {username}!")

greet_user()