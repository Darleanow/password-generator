from random import choice
chars="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
specialchar="&#{'([-|_\^@)]}$*%/?!<>²"
possib=["char","number"]
lenght=int(input("Entrez la longueur de votre mot de passe : "))
specialchars=(input("Voulez vous des characteres spéciaux [O/n] : ")).upper()
majuscules=(input("Voulez vous des majuscules [O/n] : ")).upper()
if specialchars=="O":
    possib.append("specialchars")
if majuscules=="O":
    possib.append("majuscules")
passw=""
for i in range(lenght):
    choix=choice(possib)
    if choix=="char":
        choix=choice(chars)
        passw+=choix
    elif choix=="specialchars":
        choix=choice(specialchar)
        passw+=choix
    elif choix=="majuscules":
        choix=choice(chars)
        passw+=choix.upper()
    elif choix=="number":
        choix=choice(number)
        passw+=choix
print(passw)
