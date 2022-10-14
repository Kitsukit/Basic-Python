#Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reservestring():
    text=input("String eingeben: ")

    reserved= ""
    for i in range (len(text)):
        reserved= reserved+text[-1-i]

    #print(reserved)
    return reserved
