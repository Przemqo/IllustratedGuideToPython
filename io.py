fin = open(r'C:\Users\Przemqo\Python\Code\plik.txt','r')

#print(fin.readline()) # one line read

#print(fin.readlines()) # lines as list

#print(fin.read()) # entire document


for line in fin:
    print(line)


fin.close()

fout = open(r'C:\Users\Przemqo\Python\Code\out.txt','w')
fout.write('Przemek')
fout.close()

with open(r'C:\Users\Przemqo\Python\Code\out2.txt','w') as fout2:
    fout2.write('Domel')
