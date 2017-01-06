with open("ex22_names.txt", "r") as f:
    names = f.read()

names = names.split("\n")  # convert to list
names_dict = {}

for name in names:
    if name not in names_dict and name != '':
        names_dict[name] = names.count(name)

for name in names_dict:
    print "%s %s" % (name, names_dict[name])
