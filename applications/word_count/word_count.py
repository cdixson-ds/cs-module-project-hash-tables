
def word_count(s):
    dicto = {}
    word = s.lower()
    stop = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")
    for c in stop:
        word = word.replace(c, "")

    for w in word.split():
        if w == "":
            continue
        if w not in dicto:
            dicto[w] = 1
        else:
            dicto[w] += 1
    return dicto



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))