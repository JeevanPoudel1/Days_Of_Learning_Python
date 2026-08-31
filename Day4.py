phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


LearnDict = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in LearnDict.items():
    print("Phone number of %s is %d" % (name, number))

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

phonebook["Jake"] = 938277264
del phonebook["Jill"]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")