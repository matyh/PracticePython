def fibonacci(length):
    seq = [0, 1]
    if length == 1:
        seq.remove(1)
    else:
        # start from 2 since there is [0, 1] already
        for i in range(2, length):
                seq.append(seq[-1] + seq[-2])
    print seq


def user_input():
    return int(raw_input("Length of Fibonacci sequence: "))

while 1 == 1:
    fibonacci(user_input())