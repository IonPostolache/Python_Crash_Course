
cars=['bmw', 'audi', 'ford', 'mercedes', 'opel']
print(f"This is the initial list: {cars}")
cars.sort()
print(f"This is the list after sort: {cars}")
cars.sort(reverse=True)
print(f"This is the list after sort reverse: {cars}")
print(f"This is the list after applying sorted: {sorted(cars)}")
print(f"This is how the list looks like at the moment: {cars}")
length=len(cars)
print(length)
print(len(cars))
for car in cars:
    print(f"My new car may be a {car}")

squares=[]
print(squares)
for x in range(1,11):
    square=x**2
    squares.append(square)

print(squares)

#for number in range(1000001):
    #print(number)

#numbers=list(range(1,1000001))
#print(numbers)
