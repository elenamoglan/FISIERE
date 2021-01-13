with open ('input.txt', 'r') as f:
    a=int(f.readline())
with open ('output.txt', 'w') as f:
    for i in range(a-2,a+3):
        f.write(str(i)+' ')