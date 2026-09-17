def check_for_word():
    word = "learning"
    with open("practice.txt", "w") as f:
        f.write(word)
    with open("practice.txt", "r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("found")
        else:
            print("not found")


def check_for_line():
    word="learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1

print(check_for_line() )