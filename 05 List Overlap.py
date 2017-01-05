import random

a = [random.randint(0, 20) for number in range(0, random.randint(0, 10))]
b = [random.randint(0, 20) for number in range(0, random.randint(0, 10))]


# # alternative to list comprehension - a bit too randpm
# a, b = [], []
# for lenght in range(0, random.randint(0, 20)):
#     number = random.randint(0, 20)
#     random.choice([a, b]).append(number)


# Unzipping alternative...two list comprehension is maybe faster and
# definitely more readable
# a, b = zip(*[(random.randint(0, 20), random.randint(0, 20)) for number in range(0, random.randint(0, 10))])

new = []
for item in a:
    if item in b:
        new.append(item)
for item in b:
    if item in a and item not in new:
        new.append(item)

print a
print b
print list(set(new))

# the easiest solution
# print list(set(a) & set(b))
