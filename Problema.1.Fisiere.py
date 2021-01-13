with open ('numere.txt', 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
with open ('minim.txt', 'w') as f:
    if a<b:
        f.write(str(a))
    elif b<a:
        f.write(str(b))
    else:
        f.write(str(a))