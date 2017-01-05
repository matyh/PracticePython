def reverse(string):
    words = string.split(' ')
    words.reverse()
    print ' '.join(words)


def uinput():
    return str(raw_input("Enter sentence: "))


while 1 == 1:
    reverse(uinput())
