with open ('numere.txt', 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
with open ('produs.txt', 'w') as f:
    if a<b:
        f.write(str(a*3) + '\n' + str(b*2))
    if b<a:
        f.write(str(b*3) + '\n' + str(a*2))