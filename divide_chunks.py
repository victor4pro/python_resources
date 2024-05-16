my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky', 'nerdy', 'geek',
           'love', 'questions', 'words', 'life']


# Yield successive n-sized
# chunks from l.
def divide_chunks(listx, n_slice):
    # looping till length l
    for i in range(0, len(listx), n_slice):
        yield listx[i:i + n_slice]


if __name__ == '__main__':
    # How many elements each
    # list should have
    n = 5
    x = list(divide_chunks(my_list, n))
    print(x)
    # output:
    # [['geeks', 'for', 'geeks', 'like', 'geeky'], ['nerdy', 'geek', 'love', 'questions', 'words'], ['life']]
