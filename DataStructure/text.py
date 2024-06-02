text ="bonjour le monde "
def place(text,caractere):
    index=''
    for i in range(len(text)):
        if text[i] == caractere:
            index = index +","+ str(i)
            print(index)
place(text,"o")
