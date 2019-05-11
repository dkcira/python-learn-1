
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for number in numbers:
            results.append(number)
    return results


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
    print('array:', arr)
    print('flattened:', flatten(arr))
