def create_csv(filename, data):
    with open(filename, 'w') as fout:
        fout.write('name,address,age\n')
        for value in data:
            fout.write(','.join(str(i) for i in value))
            fout.write('\n')
        
#def read_csv(filename):
#    with open(filename, 'r') as fin:
#        header = fin.read()

data = [('Przemek', 'Sadlowina 3', 27), ('Arek', 'Kollataja 3', 25)]

create_csv('pliczek.csv',data)

dane={}
lista=[]
with open('pliczek.csv', 'r') as fin:
       header = list(fin.readline().split(','))
       for line in fin:
           name, address, age = line.split(',')
           dane['name']= name
           dane['address'] = address
           dane['age'] = age[:-1]
           lista.append(dane.copy())
           
print(lista)
       
#header = list(fin.readline().split(','))