f = open("yesterday.txt", 'r')

yesterday_lyric=''
while 1:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

n_of_yesterday_1 = yesterday_lyric.count("Yesterday")
n_of_yesterday_2 = yesterday_lyric.count("yesterday")
print("Number of Word 'Yesterday'", n_of_yesterday_1)
print("Number of Word 'yesterday'", n_of_yesterday_2)



number = "100"

def midterm(number):
    result = ""
    if number.isdigit() is True:
        if number is 100:
            if number/10 == 1:
                result = True
            else:
                result = False
    return result

print(midterm(number))
