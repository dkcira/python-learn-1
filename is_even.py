def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n=7
    print(f'is {n} even? {is_even(n)}')