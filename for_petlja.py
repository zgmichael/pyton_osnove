# for petlja

import random

tajnibroj = random.randint(1,30)


for x in range(5):


    pogodi = int(input("Pogodi jedan broj izmedu 1 i 30:"))

    print(x)

    if tajnibroj == pogodi:

        print ("Bravo pogodio si! To je tajni broj", tajnibroj)

        break

    else:
        print ("Fulao si probaj ponovo...")

print ("Kraj igre")