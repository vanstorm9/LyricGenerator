import os

def replace_first_par(line, i):
    line = line.replace("(", ". ")

    # Uncomment to view changed line
    #if i == 544:
    #    print line
    
    return line

real_path = 'text/combined.txt'
temp_path = 'text/combined_0.txt'



f=open(real_path,'r')
w=open(temp_path,'w')

i = 0
for line in f.readlines():

    #print 'l:', line
    
    if line.strip():
        # Strip certain punctuation
        line = line.translate(None, "(){}<>-")

        #print 'p:', line[len(line)-2]
        if line[len(line) - 2]!= '.' and line[len(line) - 2]!= '!' and line[len(line) - 2]!= '?':
            #line += '.'
            line = line.replace("\n", ".\n")
            #print line
        
        w.write(line)

    i = i + 1
    
f.close()
w.close()

os.rename(temp_path, real_path)

print 'File formatting completed!'
    
    
