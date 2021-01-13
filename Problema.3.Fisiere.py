with open ('globulet.txt', 'r') as f:
    albe = f.readline()
    rosii = int(albe) + 2
    albastre = int(albe) + rosii - 2
with open ('bradut.txt', 'w') as f:
    f.write(str(int(albe) + rosii + albastre))