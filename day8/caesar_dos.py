

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def revisar_indice(indic, numer):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(alphabet) < indic + numer:
        a = indic + numer - len(alphabet)
        return a 
    return indic + numer

    
def caesar(frace, numer, alf, direcc):
    frace1=[]
    
    for i in range(0, len(frace)):
        y = frace[i] 
        z = alf.index(y)
        if direcc == 'encode':
            a = revisar_indice(z, numer)
        else:
            a = z - numer
        frace1.append(alf[a])
    return frace1
  

Iniciar = True
while Iniciar != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
   
    encrip = caesar(text,shift, alphabet, direction)
    print("The encoded text is "+"".join(encrip) )
    

