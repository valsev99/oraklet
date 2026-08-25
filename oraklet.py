import random

svar = ["ja, helt klart.", "Absolut inte", "Fråga ingen imorgon.", "Det vill du inte veta."]

fråga = input("Fråga oraklet: ")
print("Du frågade:", fråga)
print(random.choice(svar))