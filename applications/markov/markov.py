#in a markov chain all the information needed to predict the next event
#is contained in the most recent event

import random
import numpy as np

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()  

#keep punctuation
corpus = words.split()

#function that yields pairs of words from the input
def make_pairs(x):
    for i in range(len(x)-1):
        yield(x[i], x[i+1])

pairs = make_pairs(corpus)

#if the first word of the pair is already in the dictionary, append the
#next word to the list of words that follow that word. Otherwise,
#initialize a new entry in the dictionary
cache = {}    

for word_1, word_2 in pairs:
    if word_1 in cache.keys():
        cache[word_1].append(word_2)
    else:
        cache[word_1] = [word_2]


punc = ['.', '?', '!']
#first_word = np.random.choice(corpus)
#last_word = np.random.choice(corpus)

first_word = []
last_word = []

keys = cache.keys()

for key in keys:
    if (key[0].isupper() or key[0] == '"' and key[1].isupper()) and (key[-1] != '"') and (key[-1] not in punc):
        first_word.append(key)
    if (key[-1] in punc) or (key[-1] == '"' and key[-2] in punc):
        last_word.append(key)


#pick a random word for the beginning of the chain  and the end
chain = [word_1]

n_words = 100

#after 1st word every word in chain sampled randomly
for i in range(n_words):
    chain.append(np.random.choice(cache[chain[-1]]))

#returns string
''.join(chain)



# TODO: construct 5 random sentences
# Your code here

new = True
sentence = 0
while sentence < 5:
	if new:
		word = random.choice(first_word)
		print(word, end=" ")
		new = False
	else:
		if word in last_word:
			new = True
			sentence += 1
		else:
			cur_list = cache[word]
			word = random.choice(cur_list)
			print(word, end=" ")



