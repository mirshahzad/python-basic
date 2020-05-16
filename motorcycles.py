motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducat1'
print(motorcycles)

motorcycles.append('ducat1')
print(motorcycles)

motorcycles.insert(0, 'ducat1')
print(motorcycles)

del motorcycles[0]
print(motorcycles)


popped_motorcycle = motorcycles.pop()
print(motorcycle)
print(popped_motorcycle)