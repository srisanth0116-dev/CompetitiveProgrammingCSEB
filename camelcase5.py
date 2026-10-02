n = int(input())

words = input().split(',')

pattern = input().strip()

result = []

for word in words:
    word = word.strip()

    abbreviation = ""

    for ch in word:
        if ch.isupper():
            abbreviation += ch

    i = 0

    for ch in abbreviation:
        if i < len(pattern) and ch == pattern[i]:
            i += 1

    if i == len(pattern):
        result.append((abbreviation, word))

result.sort()

if len(result) == 0:
    print("No match found")
else:
    for abbreviation, word in result:
        print(word)
