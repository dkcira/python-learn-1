def anti_vowel(text):
    nl = len(text)
    newstring = ""
    the_vowel = ["a","e","i","o","u"]
    for i in range(nl):
        c = text[i]
        if not (c in the_vowel or c.lower() in the_vowel):
            newstring += c
    print(newstring)
    return newstring

if __name__ == '__main__':
    test_text = "test text for anti vowel"
    print('original:', test_text)
    print('anti vowel:')
    anti_vowel(test_text)