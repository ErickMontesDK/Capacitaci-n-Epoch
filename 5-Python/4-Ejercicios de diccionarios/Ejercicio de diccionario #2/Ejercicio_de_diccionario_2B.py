from diccionario import morse_code
from_morse_to_letter = {code:letter for letter, code in morse_code.items()}

def translate_from_morse(code):
    code = code.replace("\n","")
    letters = code.split(";")
    sentence = ""

    for letter in letters:
        if letter in from_morse_to_letter: 
            sentence += from_morse_to_letter[letter]
    print(f"Código morse: {code}.\nTraducción:'{sentence}'")
    
if __name__=="__main__":
    morse_text = """.;-.; ;.;.-..; ;.;-..-;-;.;-.;...;---; ;
...;..-;.-.; ;-..;.; ;.-..;.-; ;-;..;.;.-.;.-.;.-; ;-..;
.; ;-.;.-;-..;..;.; ;...;.; ;-..;.;...;-.-.;..-;-...;.-.;
..;---; ;..-;-.;.-; ;-.-.;....;---;--..;.-; ;.-;...;..; ;
-.-.;---;--;---; ;.-;.-..;--.;..-;-.;---;...;"""
    
    translate_from_morse(morse_text)
    
