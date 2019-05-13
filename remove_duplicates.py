def remove_duplicates(myls):
    """ remove duplicates from list """
    newls = []
    for i in myls:
        if  not (i in newls):
            newls.append(i)
    return newls

if __name__ == "__main__":
    myls = [1, 2, 3, 2, 4, 2, 7, 2, 9, 11]
    print(f'list: {myls}, deduplicated: {remove_duplicates(myls)}')