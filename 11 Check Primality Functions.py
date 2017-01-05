def is_prime(number):
    prime = True
    for num in range(2, number):
        if number % num == 0 or number == 1:
            prime = False
            break

    if prime:
        print "%i is prime.\n" % number
    else:
        print "%i is not prime.\n" % number


def user_input():
    return raw_input("Check this number is prime: ")

while 1 == 1:
    is_prime(int(user_input()))
