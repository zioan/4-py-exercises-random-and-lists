import random
my_list = ['item1', 'second', 'car']

my_list[1] = "another_item"

my_list.extend(['tesla', 'bmw'])

print(my_list)


# exercise

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pick_random = random.randint(0, len(names) - 1)
capitalized_name = names[pick_random].capitalize()

print(f"{capitalized_name} is going to buy the meal today!")
