with open('primenumbers.txt', 'r') as p, open('happynumbers.txt', 'r') as h:
    prime = p.read().split()
    happy = h.read().split()

# print subtraction (number which are unique in each list)
# print sorted(list(set(prime) - set(happy)), key=int)

common = [n for n in prime if n in happy]
print common
p.readlines()
