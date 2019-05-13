def purify(seq):
    """ removes all odd numbers from a list """
    new_seq = []
    for i in seq:
        if i%2 == 0:
            new_seq.append(i)
    print(new_seq)
    return new_seq

if __name__ == "__main__":
    seq = [1,2,3,4,5,6,7,8]
    print(f'sequence: {seq}, purified: {purify(seq)}')