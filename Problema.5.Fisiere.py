with open ('numar.txt', 'r') as f:
    n=int(f.readline())
with open ('inmultire.txt', 'w') as f:
    for i in range(1,11):
        p = n * i
        f.write(str(i)+'x'+str(n)+'='+str(p)+'\n')
