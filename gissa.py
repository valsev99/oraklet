import random

din_gissning = int(input("Gissa 1-10 "))

Datorns_gissning = int(random.randint (1, 10))

print (Datorns_gissning)


if Datorns_gissning < din_gissning:
    print("du van")
else:
    print("du förlorade")