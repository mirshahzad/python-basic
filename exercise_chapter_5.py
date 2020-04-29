#exercise 5.3
allien_color = 'yellow'
allien_color = 'red'
allien_color = 'green'

if allien_color == 'green':
	print("You just earned 5 points!")

#exercise 5.4
allien_color = 'green'

if allien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just earned 10 points!")

#exercise 5.5
allien_color = 'red'

if allien_color == 'green':
	print("You just earned 5 points!")
elif allien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 point!")


#exercise 5.6
person_age = 20

if person_age < 2 :
	print("You are a Baby!")
elif person_age < 4 :
	print("You are a toddler!")
elif person_age < 13 :
	print("You are a kid!")
elif person_age < 20 :
	print("You are a teenager!")
elif person_age < 65 :
	print ("You are an adult!")
else :
	print ("You are elder!")


#exercise 5.7
favorite_fruits = ['banana', 'apple', 'Pomegranates']

if 'kiwi' in favorite_fruits:
	print("I really like kiwi.")
if 'grapes' in favorite_fruits:
	print("I really like grapes.")
if 'banana' in favorite_fruits:
	print("I really like banana!")
if 'apple' in favorite_fruits:
	print("I really like apple.")
if 'Pomegranates' in favorite_fruits:
	print("I really like Pomegranates.")


#exercise 5.8
usernames = ['Alexander', 'Bob', 'Alice', 'admin', 'eric']

for username in usernames :
	if username == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + username + ", thank you for logging in again!")

#exercise 5.9
usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print("Hellow admin, would you like to see a status report?")
		else:
			print("Hellow " + username + ", thank you for logging in again!")
else:
	print("We need to find some users!")

#exercise 5.10
current_users = ['Alexander', 'Bob', 'Alice', 'admin', 'eric']
new_users = ['Alex', 'Bob', 'Alice', 'admn', 'abc']

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print("Sorry " + new_user + ", that name is already taken.")
	else:
		print("Great, " + new_user + "is still available.")

#exercise 5.11
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
