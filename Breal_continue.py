#break and continue statements in python

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
#prints 0,1,2,3,4

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
#prints 1,3,5,7,9


while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

for i in range(1,10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because "
    "for loop is terminated because of " \
    "break but if the loop was not " \
    "terminated then this would have been printed")

#prints out 1,2,3,4

for i in range(1,10):
    if(i%20==0):
        break
    print(i)
else:
    print("Then prints this because for loop is not terminated" 
          " because of break but if the loop was terminated" \
          " then this wouldn't have been printed")

#prints 1,2,3,4,5,6,7,8,9
# Then prints this because for loop is not terminated 
#because of break but if the loop was terminated 


"""
Loop through and print out all even numbers 
from the numbers list in the same order they are received.
Don't print any numbers that come after 237 in 
the sequence.
"""

print("solution")
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break
    elif number % 2 == 0:
        print(number)
    