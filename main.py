favorite_animals = ['Dog', 'Cat', 'Monkey', 'Rabbit']
print(favorite_animals) 
print(favorite_animals[1])
favorite_animals.remove('Monkey')
favorite_animals.append('Lion')
for fav in favorite_animals:
    print(f"I love {fav}")

numbers = [5, 4, 3, 2 , 1]
numbers_sum = 0
for num in numbers:
    numbers_sum += num
print(numbers_sum)