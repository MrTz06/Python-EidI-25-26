text=input("Geben Sie einen Text ein: ")

for zeichen in text:
    print(zeichen,"->",ord(zeichen))

for i in range(len(text)):
    print(text[i],"->",ord(text[i]))
