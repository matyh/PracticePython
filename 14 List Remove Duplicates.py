# remove duplicates by looping through list
def removeDuplicates(mylist):
    unilist = []
    for item in mylist:
        if item not in unilist:
            unilist.append(item)
    print unilist


# by using set
def removeDuplicatesSet(mylist):
    print list(set(mylist))

removeDuplicates([1, 2, 2, 3, 1, 'ahoj', 'hi', 'hello', 'ahoj'])