

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def list_alfabeth():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for position in alphabet:
        print(position)
     
def alf_encrypt(frace, numer, alf):
    frace1=[]
    
    for i in range(0, len(frace)):
        y = frace[i] 
        z = alf.index(y)
        a = z + numer
        frace1.append(alf[a])
        #print(y, z, a, alphabet[a])        
    return frace1


def alf_decrypt(frace1, numer, alf):
    frace2=[]
    for i in range(0, len(frace1)):
        y = frace1[i] 
        z = alf.index(y)
        a = z - numer
        frace2.append(alf[a])
    return frace2

Iniciar = True
while Iniciar != False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        encrip = alf_encrypt(text,shift, alphabet)
        print("The encoded text is "+"".join(encrip) )
    if direction == 'decode':
        decode = alf_decrypt(text, shift, alphabet)
        print("The decode text is "+"".join(decode) )