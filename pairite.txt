# Correction exercice 25
parite = [2, 5, 3, 22, 3, 7, 18, 25, 63, 62, 100]

for nb in parite:
  if nb%2 == 0:
    file = open("pair.txt", "a")
    file.write(str(nb))
    file.write(" ") # espace entre les nombres
  else:
    file = open("impair.txt", "a")
    file.write(str(nb)) # espace entre les nombres
    file.write(" ")
file.close()

print("Test deployment git")
print("test de nouveau")