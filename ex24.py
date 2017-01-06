def make_board(size):
    """Print board with size x size dimensions."""
    n = size
    while n > 0:
        print size * ' ---' + ' '
        print size * '|   ' + '|'
        n -= 1
    print size * ' ---' + ' '

if __name__ == '__main__':
    make_board(int(raw_input("Make board with dimensions: ")))
