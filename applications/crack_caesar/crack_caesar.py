# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

letter_count = 0
letter_dist = dict(map(lambda c: (c, 0), "QWERTYUIOPASDFGHJKLZXCVBNM"))
FREQUENCIES = [
    "E",
    "T",
    "A",
    "O",
    "H",
    "N",
    "R",
    "I",
    "S",
    "D",
    "L",
    "W",
    "U",
    "G",
    "F",
    "B",
    "M",
    "Y",
    "C",
    "P",
    "K",
    "V",
    "Q",
    "J",
    "X",
    "Z",
]

with open("ciphertext.txt") as f:
    text = f.read()

for c in text:
    if c in letter_dist:
        letter_count += 1
        letter_dist[c] += 1

cipher = dict(zip(
    map(
        lambda x: x[0],
        sorted(letter_dist.items(), key=lambda c: c[1], reverse=True)
    ),
    FREQUENCIES
))
new_text = "".join(map(lambda c: cipher[c] if c in cipher else c, text))
print(new_text)
