
def product(seq):
    """ takes a list of integers as input and returns the product of all of the elements in the list."""
    prod = 1.
    for i in seq:
        prod = prod * i
    return int(prod)

if __name__=='__main__':      # is file being called from prompt?
    arr = [4,2,3,4]
    print(f'array: {arr}, product: {product(arr)}')
