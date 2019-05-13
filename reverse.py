def reverse(text):
    nl = len(text)
    newstring = ""
    for i in range(nl):
        #print text[nl-i-1],
        newstring += text[nl-i-1]
    return newstring

if __name__ == "__main__":
    text = "this is just a test"
    print(f'text: {text}, reversed: {reverse(text)}')