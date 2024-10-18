import random
a=["Heart ","Diamond ","Club ","Spade "]
b=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
deck=[]
for i in a:
    for j in b:
        deck.append(i+j)
random.shuffle(deck)
print(deck)
