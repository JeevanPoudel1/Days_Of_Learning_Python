import statistics
import random
import sys

randomoutput= random.randrange(1, 10,4)
print(randomoutput)
#head and tail
coin= random.choice(["head","tails"])
print(coin)

#random number from 1 to 5
number = random.randint(1,5)
print(number)

#random suffle
cards = ["queen", "king", "jack", "Ace"]
random.shuffle(cards)
for card in cards:
    print(card)

#random statics
print(statistics.mean([41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]))

#sys takes an input from user at command line
#print("hello, my name is", sys.argv[1])

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("too few argument")


if len(sys.argv)<2:
    sys.exit("too few argument")
elif len(sys.argv)>2:
    sys.exit("too many argument")

print("hello, my name is", sys.argv[1])


if len(sys.argv) < 2:
    sys.exit("too few args")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)

