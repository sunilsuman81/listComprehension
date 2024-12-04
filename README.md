# listComprehension
List comprehensions are a unique way to create lists in Python. A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.


1. Introduction
List comprehensions is a pythonic way of expressing a ‘for-loop’ that appends to a list in a single line of code.

So how does a list comprehension look? Let’s write one to create a list of even numbers between 0 and 9:

[i for i in range(10) if i%2 == 0]
[0, 2, 4, 6, 8]
And below is the for-loop equivalent for the same logic:

result = []
for i in range(10):
    if i%2 == 0:
        result.append(i)
result
[0, 2, 4, 6, 8]
I prefer list comprehensions because it’s easier to read, requires lesser keystrokes and it usually runs faster as well.

The best way to learn list comprehensions is by studying examples of converting for-loops and practicing sample problems.

2. Typical format of List Comprehensions
A list comprehension typically has 3 components:

The output (which can be string, number, list or any object you want to put in the list.)
For Statements
Conditional filtering (optional).
Below is a typical format of a list comprehension.


However, this format is not a golden rule.

Because there can be logics that can have multiple ‘for-statements’ and ‘if conditions’ and they can change positions as well. The only thing that does not change however is the position of the output value, which always comes at the beginning.

Next, Let’s see examples of 7 different types of problems where you can use list comprehensions instead of for-loops.

Example Type 1: Simple for-loop
Problem Statement: Square each number in mylist and store the result as a list.

The ‘For Loop’ iterates over each number, squares the number and appends to a list.

# For Loop Version
mylist = [1,2,3,4,5]
result = []

for i in mylist:
    result.append(i**2)

result
[1, 4, 9, 16, 25]
How to convert this to a list comprehension? Take the output in the same line as the for condition and enclose the whole thing in a pair of [ .. ].

# List Comprehension Version
[i**2 for i in [1,2,3,4,5]]
[1, 4, 9, 16, 25]
Example Type 2: for-loop with conditional filtering
What if you have an if condition in the for loop? Say, you want to square only the even numbers:

Problem statement: Square only the even numbers in mylist and store the result in a list.

# For Loop Version
mylist = [1,2,3,4,5]
result = []

for i in mylist:
    if i%2==0:
        result.append(i**2)

result
[4, 16]
In list comprehension, we add the ‘if condition’ after the for-loop if you want to filter the items.

# List Comprehension Version
[i**2 for i in [1,2,3,4,5] if i%2==0]
[4, 16]
Example Type 3: for-loop with ‘if’ and ‘else’ condition
Let’s see a case where you have an ‘if-else’ condition in the for-loop.

Problem Statement: In mylist, square the number if its even, else, cube it.

# For Loop Version
mylist = [1,2,3,4,5]
result = []

for i in mylist:
    if i%2==0:
        result.append(i**2)
    else:
        result.append(i**3)

result
[1, 4, 27, 16, 125]
In previous example, we wanted to filter the even numbers. But in this case, there is no filtering. So put the if and else before the for-loop itself.

# List Comprehension Version
[i**2 if i%2==0 else i**3 for i in [1,2,3,4,5]]
[1, 4, 27, 16, 125]
Example Type 4: Multiple for-loops
Now let’s see a slightly complicated example that involves two For-Loops.

Problem Statement: Flatten the matrix mat (a list of lists) keeping only the even numbers.

# For Loop Version
mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
result = []
for row in mat:
    for i in row:
        if i%2 == 0:
            result.append(i)

result
[2, 4, 6, 8, 10, 12, 14, 16]
Can you imagine what the equivalent list comprehension version would look like? It’s nearly the same as writing the lines of the for-loop one after the other.

# List Comprehension version
[i for row in mat for i in row if i%2==0]
[2, 4, 6, 8, 10, 12, 14, 16]
Example Type 5: Paired outputs
Problem Statement: For each number in list_b, get the number and its position in mylist as a list of tuples.

# For Loop Version
mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]

result = []
for i in list_b:
    result.append((i, mylist.index(i)))

result
[(6, 2), (4, 8), (6, 2), (1, 3), (2, 7), (2, 7)]
In this case, the output has 2 items instead of one. So pair both of them as a tuple and place it before the for statement.

# List Comprehension version
[(i, mylist.index(i)) for i in list_b]
[(6, 2), (4, 8), (6, 2), (1, 3), (2, 7), (2, 7)]
Example Type 6: Dictionary Comprehensions
Same problem as previous example but output is a dictionary instead of a list of tuples.

Problem Statement: For each number in list_b, get the number and its position in mylist as a dict.

# For Loop Version
mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]

result = {}
for i in list_b:
    result[i]=mylist.index(i)

result
{6: 2, 4: 8, 1: 3, 2: 7}
To make a dictionary output, you just need to replace the square brackets with curly brackets. And use a : instead of a comma between the pairs.

# List Comprehension version
{i: mylist.index(i) for i in list_b}
{6: 2, 4: 8, 1: 3, 2: 7}
Example Type 7: Tokenizing sentences into list of words
This is a slightly different way of applying list comprehension.

Problem Statement: The goal is to tokenize the following 5 sentences into words, excluding the stop words.

# Input:
sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']
# For Loop Version
results = []    
for sentence in sentences:
    sentence_tokens = []
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_tokens.append(word)
    results.append(sentence_tokens)

results
[['new', 'world', 'record', 'was', 'set'],
 ['holy', 'city', 'ayodhya'],
 ['eve', 'diwali', 'tuesday'],
 ['over', 'three', 'lakh', 'diya', 'or', 'earthen', 'lamps'],
 ['lit', 'up', 'simultaneously', 'banks', 'sarayu', 'river']]
If you wanted to flatten out the words in the sentences, then the solution would have been something like this:

print([word for sentence in sentences for word in sentence.split(' ') if word not in stopwords])
['new', 'world', 'record', 'was', 'set', 'holy', 'city', 'ayodhya', 'eve', 'diwali', 'tuesday', 'over', 'three', 'lakh', 'diya', 'or', 'earthen', 'lamps', 'lit', 'up', 'simultaneously', 'banks', 'sarayu', 'river']
But we want to distinguish which words belong to which sentence, that is the original grouping of sentences should remain intact as a list.

To achieve this, the entire second unit of for-loop, that is, the [word for word in sentence.split(' ') if word not in stopwords] part should be considered as an output and therefore will go at the beginning of the list comprehension.

# List Comprehension Version
[[word for word in sentence.split() if word not in stopwords] for sentence in sentences]
[['new', 'world', 'record', 'was', 'set'],
 ['holy', 'city', 'ayodhya'],
 ['eve', 'diwali', 'tuesday'],
 ['over', 'three', 'lakh', 'diya', 'or', 'earthen', 'lamps'],
 ['lit', 'up', 'simultaneously', 'banks', 'sarayu', 'river']]
3. Practice Exercises (increasing level of difficulty)
Question 1. Given a 1D list, negate all elements which are between 3 and 8, using list comprehensions
# Input
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Desired Output
# [1, 2, -3, -4, -5, -6, -7, -8, 9, 10]
[-i if  2 < i < 9 else i for i in mylist]
[1, 2, -3, -4, -5, -6, -7, -8, 9, 10]
Question 2: Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.
# Desired output
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
#  'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
#  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
#  's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
#  'y': 25, 'z': 26}
print({chr(i+97):i+1 for i in range(26)})
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
import string
print({string.ascii_lowercase[i]:i+1 for i in range(26)})
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
import string
print({a:i+1 for a,i in zip(string.ascii_lowercase, range(26))})
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
Question 3: Replace all alphabets in the string ‘Lee Quan Yew’, by substituting the alphabet with the corresponding numbers, like 1 for ‘a’, 2 for ‘b’ and so on.
# Desired Output:
# [12, 5, 5, ' ', 17, 21, 1, 14, ' ', 25, 5, 23]
[ord(a.lower())-96 if a is not ' ' else ' ' for a in 'Lee Quan Yew']
[12, 5, 5, ' ', 17, 21, 1, 14, ' ', 25, 5, 23]
import string
d = {a:i+1 for a,i in zip(string.ascii_lowercase, range(26))}
[d.get(a.lower(), ' ') for a in 'Lee Quan Yew']
[12, 5, 5, ' ', 17, 21, 1, 14, ' ', 25, 5, 23]
Question 4: Get the unique list of words from the following sentences, excluding any stopwords.
Hint: this is set comprehension

# Input
sentences = ["The Hubble Space telescope has spotted", 
             "a formation of galaxies that resembles", 
             "a smiling face in the sky sky"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

# Desired output:
# {'face', 'telescope', 'formation', 'smiling', 'hubble', 'spotted', 
# 'resembles', 'has', 'sky', 'galaxies', 'that', 'space'}
print({word for sentence in sentences for word in sentence.lower().split() if word not in stopwords})
{'galaxies', 'space', 'that', 'spotted', 'face', 'smiling', 'hubble', 'has', 'telescope', 'formation', 'resembles', 'sky'}
Question 5: Tokenize the following sentences excluding all stopwords and punctuations.
# Input
sentences = ["The Hubble Space telescope has spotted", 
             "a formation of galaxies that resembles", 
             "a smiling face in the sky", 
             "The image taken with the Wide Field Camera", 
             "shows a patch of space filled with galaxies", 
             "of all shapes, colours and sizes"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with']

# Desired Output
# [['hubble', 'space', 'telescope', 'has', 'spotted'],
#  ['formation', 'galaxies', 'that', 'resembles'],
#  ['smiling', 'face', 'sky'],
#  ['the', 'image', 'taken', 'wide', 'field', 'camera'],
#  ['shows', 'patch', 'space', 'filled', 'galaxies'],
#  ['all', 'shapes,', 'colours', 'sizes']]
[[word for word in sentence.lower().split() if word not in stopwords] for sentence in sentences]
[['hubble', 'space', 'telescope', 'has', 'spotted'],
 ['formation', 'galaxies', 'that', 'resembles'],
 ['smiling', 'face', 'sky'],
 ['image', 'taken', 'wide', 'field', 'camera'],
 ['shows', 'patch', 'space', 'filled', 'galaxies'],
 ['all', 'shapes,', 'colours', 'sizes']]
Question 6: Create a list of (word:id) pairs for all words in the following sentences, where id is the sentence index.
# Input
sentences = ["The Hubble Space telescope has spotted", 
             "a formation of galaxies that resembles", 
             "a smiling face in the sky"]

# Desired output:
# [('the', 0), ('hubble', 0), ('space', 0), ('telescope', 0), ('has', 0), ('spotted', 0),
#  ('a', 1), ('formation', 1), ('of', 1), ('galaxies', 1), ('that', 1), ('resembles', 1),
#  ('a', 2), ('smiling', 2), ('face', 2), ('in', 2), ('the', 2), ('sky', 2)]
print([(word, i) for i, sentence in enumerate(sentences) for word in sentence.lower().split()])
[('the', 0), ('hubble', 0), ('space', 0), ('telescope', 0), ('has', 0), ('spotted', 0), ('a', 1), ('formation', 1), ('of', 1), ('galaxies', 1), ('that', 1), ('resembles', 1), ('a', 2), ('smiling', 2), ('face', 2), ('in', 2), ('the', 2), ('sky', 2)]
Question 7: Print the inner positions of the 64 squares in a chess board, replacing the boundary squares with the string ‘—-‘.
# Desired Output:
# [['----', '----', '----', '----', '----', '----', '----', '----'],
#  ['----', (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), '----'],
#  ['----', (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), '----'],
#  ['----', (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), '----'],
#  ['----', (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), '----'],
#  ['----', (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), '----'],
#  ['----', (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), '----'],
#  ['----', '----', '----', '----', '----', '----', '----', '----']]
[['----' if any([k == v for k in (i,j) for v in (0,7)]) else (i, j) for i in range(8)] for j in range(8)]
[['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), '----'],
 ['----', (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), '----'],
 ['----', (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), '----'],
 ['----', (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), '----'],
 ['----', (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), '----'],
 ['----', (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----']]
[[(i,j) if not(i in (0, 7) or j not in (0, 7)) else ('----') for i in range(8)] for j in range(8)]
[['----', (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', '----', '----', '----', '----', '----', '----', '----'],
 ['----', (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), '----']]
