#exercise 4.1
pizzas = ['chicken pizza', 'vegetable pizza', 'meat pizza']
for pizza in pizzas:
	print(pizza)

	print(f"I like {pizza.title()}.")

print("I really love pizza")


#exercise 4.2
animals = ['dog', 'cat', 'horse']
for animal in animals:
	print(animal)
	print(f"A {animal.title()} would make a great pet.")
print("Any of these animals would make a great pet")


#exercise 4.3
for value in range(1, 21):
	print(value)

#exercise 4.4
numbers = list(range(1, 1000001))
print(numbers)

#exercise 4.5
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#exercise 4.6
odd_numbers = list(range(1, 21, 3))
print(odd_numbers)

#exercise 4.7
numbers = list(range(3, 31, 3))
print(numbers)

#exercise 4.8
cubes =  []
for value in range(1, 11):
	cube = value ** 3
	cubes.append(cube)
print(cubes)

#exercise 4.9
cubes = [value**3 for value in range(1, 11)]
print(cubes)

#exercise 4.11
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)


#exercise 4.13
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print("- " + item)

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print("- " + item)