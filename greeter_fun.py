def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

def greet_user(username):
	print(f"Hello, {username.title()}!")

greet_user('jesse')