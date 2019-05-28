# while petlja

import random

tajnibroj = random.randint(1,30)


while True:
    pogodi = int(input("Pogodi jedan broj izmedu 1 i 30:"))

    if tajnibroj == pogodi:

        print ("Bravo pogodio si! To je tajni broj", tajnibroj)

        break

    else:
        print ("Fulao si probaj ponovo...")

print ("Kraj igre")