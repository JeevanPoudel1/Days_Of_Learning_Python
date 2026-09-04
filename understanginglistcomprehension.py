sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)


fruits = "there is a sentence containing fruits"
print(fruits)
lets_split = fruits.split()


print("now")
for fruit in lets_split:
    if fruit == "fruits":
        print("Found the word 'fruits' in the sentence!")

print("Number of words:", len(lets_split))
print("Words:", lets_split)



#create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers. 
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
for n in numbers:
    if n > 0:
        newlist.append(int(n))
print(newlist)