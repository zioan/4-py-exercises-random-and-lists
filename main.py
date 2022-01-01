import random
import my_module
print(my_module.pi)


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()  # 0.00000 - 0.99999999...
print(random_float)

if random_float < 0.5:
    print("Heads")
else:
    print("Tails")


random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

random_float_nr = random.random() * 5  # 0.0000 - 4.99999...
print(random_float_nr)
