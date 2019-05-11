def count(sequence, item):
    sum = 0
    for i in sequence:
        if i == item:
            sum += 1
    print(sum)
    return sum


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 1, 7, 1, 9, 1]
    item = 1
    print('sequence:', sequence)
    print('item:', item)
    print('occurrences:')
    count(sequence, item)