# Store information about a pizza being ordered.
pizza = {
	'crust': 'think',
	'toppings': ['mushrooms', 'extra cheese'],
	}
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " "with the followiing toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)