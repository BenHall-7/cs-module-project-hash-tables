import random

# {
#   'test': ["a", "b", "c" ...],
#    ...
# }
chains = {}
start_words = []

def is_start(word: str):
    if word[0] == "\"":
        return len(word) > 1 and word[1].isupper()
    else:
        return word[0].isupper()

def is_stop(word: str):
    if word[-1] == "\"":
        return len(word) > 1 and word[-2] in [".", "?", "!"]
    else:
        return word[-1] in [".", "?", "!"]

# Read in all the words in one go
with open("C:\\Users\\Breakfast\\Code\\Lambda\\cs_5\\cs-module-project-hash-tables\\applications\\markov\\input.txt") as f:
    words = f.read()
    prev = None
    for word in words.split():
        word = word.strip()
        if prev:
            if is_start(prev):
                start_words.append(prev)
            
            new_entry = (word, is_stop(word))
            if prev not in chains:
                chains[prev] = [new_entry]
            else:
                chains[prev].append(new_entry)

        prev = word

# construct 5 random sentences

for _ in range(5):
    first = random.choice(start_words)
    print(first, end=" ")
    if is_stop(first):
        continue

    cur = random.choice(chains[first])
    while True:
        print(cur[0], end=" ")
        if cur[1]:
            break
        cur = random.choice(chains[cur[0]])

