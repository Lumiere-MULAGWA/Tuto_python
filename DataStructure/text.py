text ="bonjour le monde "
index=''
for i in range(len(text)):
    if text[i] == "o":
        index = index +","+ str(i)
        
print(index)