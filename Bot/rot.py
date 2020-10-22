from random import randint

""" Стартовые параметры (Start Parameters) """
rot_mover = randint(1,1000)

""" Функции (Functions) """

def rot_enc(text:str, rot_mover):
    text = [ord(elem) for elem in text]
    for move in range(len(text)):
        text[move] += rot_mover
        text[move] = chr(text[move])
    
    return ''.join(text)
    

def rot_dec(text:str, rot_mover):
    text = [ord(elem) for elem in text]

    for move in range(len(text)):
        text[move] -= rot_mover
        text[move] = chr(text[move])

    return ''.join(text)












