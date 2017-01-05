import random


def make_number():
    """Make 4-digit number. Each digit is unique number."""
    digits = random.sample(range(0, 10), 4)
    # eliminates numbers starting with 0
    while len(digits) != 4 and digits[0] == 0:
        make_number()
    joint_digits = ''.join(map(str, digits))
    return int(joint_digits)


def guess(msg="Guess the number: "):
    user_input = raw_input(msg)
    # check if number is 4-digit long
    if len(user_input) != 4:
        guess("The number must be 4-digit number, try again: ")
    # check if each number is occurred at most once
    for item in user_input:
        if user_input.count(item) > 1:
            guess("Each number must be unique, try again: ")
    if user_input[0] == 0:
        guess("The number must start with non-0 number, try again: ")
    return int(user_input)


def check(guess, number):
    guess = [int(i) for i in str(guess)]
    number = [int(i) for i in str(number)]
    cow = 0
    bull = 0
    for pos in range(4):
        if guess[pos] == number[pos]:
            cow += 1
        if guess[pos] in number and guess[pos] != number[pos]:
            bull += 1
    return "%s cows, %s bulls" % (cow, bull)


if __name__ == '__main__':
    number = make_number()
    user_guess = guess()
    while user_guess != number:
        print check(user_guess, number)
        user_guess = guess()
    else:
        print 'Congratulations, you have guessed the right number!'
