words = {}
max_len = 0

with open("C:\\Users\\Breakfast\\Code\\Lambda\\cs_5\\cs-module-project-hash-tables\\applications\\histo\\robin.txt") as f:
    text = f.read()
    for word in text.split():
        word = "".join(filter(lambda ch: ch not in r"\":;,.-+=/\\|[]{}()*^&", word)).lower()
        words[word] = 1 if not word in words else words[word] + 1
        max_len = max(max_len, len(word))

for word, num in sorted(sorted(words.items()), key=lambda x: x[1], reverse=True):
    print(f"{word: <{max_len + 2}}", "#"*num)
