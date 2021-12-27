motorcycles=['honda', 'yamaha', 'ducatty', 'suzuki']
print(motorcycles)

motorcycles[0]='hyunday'
print(motorcycles)

motorcycles=['alibaba', 'aliexpress', 'amazon', 'ebay']
print(motorcycles)

motorcycles.append('argos')
print(motorcycles)

empty=[]
print(empty)

empty.append('ducatty')
empty.append('yamaha')
empty.append('honda')
print(empty)

empty.insert(1, 'suzuki')
print(empty)

del empty[1]
print(empty)

popped_empty=empty.pop()
print(empty)
print(f"\t {popped_empty}")

first_owned=empty.pop(0)
print(f"My first motorcycle was a {first_owned.title()}.")
print(motorcycles)
motorcycles.remove('ebay')
print(motorcycles)
