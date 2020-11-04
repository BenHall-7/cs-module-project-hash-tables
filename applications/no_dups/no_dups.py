def no_dups(s):
    prev = set()
    new_word = []
    for word in s.split(" "):
        if word not in prev:
            new_word.append(word)
            prev.add(word)

    return " ".join(new_word)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))