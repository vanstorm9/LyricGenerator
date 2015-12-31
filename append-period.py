i=0
f=open('text/combined.txt')
for line in f.readlines():
    print 'l:', line
    print 'p:', line[len(line)-2]
    
    
