with open("ex22-2_sun_images.txt", "r") as f:
    cat_list = []
    l = f.readline().split('/')
    while l and len(l) > 2:
        cat_list.append(l[2])
        l = f.readline().split('/')  # error, l na konci se rovna '' a tento list nema index 2

cat_count = {}
for cat in cat_list:
    if cat not in cat_count:
        cat_count[cat] = cat_list.count(cat)

for item in cat_count:
    print "%s %s" % (item, cat_count[item])
