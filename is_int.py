def is_int(x):
    """ consider int also numbers with zero after the decimal, e.g. 7.0 """
    if (int(x)-x == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    n=5.3
    print(f'is {n} int? {is_int(n)}')