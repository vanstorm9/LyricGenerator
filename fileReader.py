i=0
f=open('text/combined.txt','r')
full_line = ""
for line in f.readlines():
    i = 0
    for letter in f.readline():
        full_line = full_line + letter
        i+=1
    print line

