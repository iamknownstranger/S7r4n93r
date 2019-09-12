'''S7r4n3r cipher is a low level cryptography cipher which can be used for day to day purposes.
In this the some of the characters from the string are replaced with the suitable number which might look like the the character itself
'''
def encrypt(plane_text):
    cipher_text = ''
    cypher = {'l': '1', 'e': '3', 'a': '4', 's': '5', 't': '7', 'b': '8', 'g': '9', 'o': '0'}
    for i in plane_text.lower():
        if i in cypher.keys():
            cipher_text += cypher[i]
        else:
            cipher_text += i
    return(cipher_text)

def decrypt(cipher_text):
    plane_text = ''
    cypher = {'1': 'l', '3': 'e', '4': 'a', '5': 's', '7': 't', '8': 'b', '9': 'g', '0': 'o'}
    for i in cipher_text.lower():
        if i in cypher.keys():
            plane_text += cypher[i]
        else:
            plane_text += i
    return(plane_text)

