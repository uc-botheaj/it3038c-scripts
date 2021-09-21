##python 3 encoder ring 

#declare the keys for encoding
keys = ['s','r','b','p']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
blackCodes = ['27','91','05','87','49','32','17','11','73','24','89','67','83','64','22','50','77','26','12','86','34','76','92','80','18','99']
purpleCodes = ['[',']','#','%','^','*','+','=','_','\\','~','<','>','.',',','?','\'','$','&','@','"','/','}','{','(',')']

#define functions for each cipher
def cipherSilver(s):
    output = ''
    for i in s:
        if i == ' ':
            output+=' '
        else:
            output+=alphabet[25 - alphabet.index(i)]
    print(output)

def cipherRed(s):
    output = ''
    for i in s:
        if i == ' ':
            output+='<space> '
        else:
            output+=str(alphabet.index(i)+11) + ' '
    print(output)

def cipherBlack(s):
    output = ''
    for i in s:
        if i == ' ':
            output+='<space> '
        else:
            output+=blackCodes[alphabet.index(i)] + ' '
    print(output)

def cipherPurple(s):
    output = ''
    for i in s:
        if i == ' ':
            output+=' '
        else:
            output+=purpleCodes[alphabet.index(i)]
    print(output)

#prompt user for which type of key they want to use
print("Enter key (\"'s' for silver, 'r' for red, 'b' for black, 'p' for purple \")")
key = input()
while key not in keys:
    print("please enter a key")
    key = input()

#prompt the user for their secret message
print("Enter secret message (letters and spaces only, please)")
secret = (input()).upper()

#based on the user input, run the function for encryption against the message
if key=='s':
    cipherSilver(secret)
elif key=='r':
    cipherRed(secret)
elif key=='b':
    cipherBlack(secret)
elif key=="p":
    cipherPurple(secret)
else:
    print('wrong ciphers')
