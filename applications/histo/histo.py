# Your code here

stops = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")



with open("robin.txt") as f:
    words = f.read()

cache = {}


for word in words.split():
    hist = ""
    for char in word:
        if char not in stops:
            hist += char
    word = hist.lower()

    if word in cache:
        cache[word] += 1
    elif word == "" or word == " ":
        break
    else:
        cache[word] = 1

#sort cache by word count
items = list(cache.items())
items = sorted(cache.items(), key=lambda x: (-x[1], x[0]))

cache = (dict(items))
for (string, value) in cache.items():
    max_len = len(max(string, key=len))
    print(f'{string} {" " * max_len} {"#" * value}')



