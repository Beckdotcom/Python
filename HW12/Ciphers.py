#  File: Ciphers.py
#  Description: 

#
#  Date Created: 4/9 09:46PM
#  Date Last Modified: 4/11 07:51PM

def encode(key,plaintext):

    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    

    for i in range(0,len(plaintext)):
        
        textLetter = plaintext[i] #singles out letter
        textIndex = alphabet.find(textLetter) #alphabet index

        if (textIndex == -1): #in the lowercase alphabet?

            if ((textLetter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True):
                textIndex = alphabet.find(textLetter.lower()) #lowercase index
                keyLetter = key[textIndex]#key index
                ciphertext +=keyLetter.upper()#add uppercase
                
            else:
                
                ciphertext +=textLetter   
        else:
            keyLetter = key[textIndex]#key index
            ciphertext +=keyLetter
    
    return ciphertext

def decode(key,ciphertext):


    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    

    for i in range(0,len(ciphertext)):
        
        textLetter = ciphertext[i] #singles out letter
        textIndex = key.find(textLetter) #key index

        if (textIndex == -1):#in the lowercase alphabet?

            if ((textLetter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") == True):
                textIndex = key.find(textLetter.lower()) #lowercase index
                alphaLetter = alphabet[textIndex]#alpha index
                plaintext +=alphaLetter.upper()#add uppercase

            else:
                
                plaintext +=textLetter    
        else:
            alphaLetter = alphabet[textIndex]#alpha index
            plaintext +=alphaLetter

    
    return plaintext

def main():

    plaintextMessages = [
        ["This is the plaintext message.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Let the Wookiee win!",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Baseball is 90% mental. The other half is physical.\n\t\t- Yogi Berra",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["I used to think I was indecisive, but now I'm not too sure.",
         "mqncdaigyhkxflujzervptobws"],
        ["Einstein's equation 'e = mc squared' shows that mass and\n\t\tenergy are interchangeable.",
         "bludcmhojaifxrkzenpsgqtywv"] ]

    codedMessages = [
        ["Uijt jt uif dpefe nfttbhf.",
         "bcdefghijklmnopqrstuvwxyza"],
        ["Qnhxgomhqm gi 10% bnjd eho 90% omwlignh. - Zghe Xmy",
         "epqomxuagrdwkhnftjizlcbvys"],
        ["Ulj njxu htgcfj C'gj jgjm mjfjcgjt cx, 'Ep pej jyxj veprx rlhu\n\t\t uljw'mj tpcez jculjm'. - Mcfvw Zjmghcx",
         "hnftjizlcbvysepqomxuagrdwk"],
        ["M 2-wdme uxc yr kylc ua xykd m qxdlcde, qpv wup cul'v gmtd mlw\n\t\t vuj aue yv. - Hdeew Rdyladxc",
         "mqncdaigyhkxflujzervptobws"] ]


    for i in range(0,len(plaintextMessages)): #encode plaintextMessage
        
        plaintext = plaintextMessages[i][0]
        plainkey = plaintextMessages[i][1]
        encodedtext = encode(plainkey,plaintext)
        recodedtext = decode(plainkey,encodedtext)

        print( format("plaintext:","13s") + plaintext)
        print( format("encoded:","13s") + encodedtext)
        print( format("re-decoded:","13s") + recodedtext)
        print()

    print()
    
    for i in range(0,len(codedMessages)): #decode codedMessages
        
        ciphertext = codedMessages[i][0]
        cipherkey = codedMessages[i][1]
        decodedtext = decode(cipherkey,ciphertext)

        print( format("encoded:","13s") + ciphertext)
        print( format("decoded:","13s") + decodedtext)
        print()
        
          
main()
