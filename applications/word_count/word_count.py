def word_count(s):
    counts = {}
    for word in ''.join(filter(lambda c: c not in r"\":;,.-+=/\\\|[]}{()*^&", s)).lower().split():
        if len(word) > 0:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts)
    return counts

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))