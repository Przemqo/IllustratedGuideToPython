names = ['Przemek', 'Arek', 'Heniek', 'Krysia']
sum = 0.0
i = 0.0

for name in names:
    sum = sum + len(name)
    i = i + 1
print (sum/i)

for name in names:
    if name == ['John']:
        print('Found it!')
        break
else:
    print('Cannot find it!')

przemek = ('Przemek', 'Domel', 27)
arek = ('Arek', 'Domel', 25)
krysia = ('Krysia','Domel', 62)
heniek = ('Heniek', 'Domel', None)

lista = [przemek, arek, krysia, heniek]
avg = 0.0
i=0.0
print(lista[1][2])
for delikwent in lista:
    if delikwent[2] is None:
        continue
    else:
        avg += delikwent[2]
        i += 1

avg = avg/i

for delikwent in lista:
    if delikwent[2] is None:
        print(delikwent[0:1])
        continue
    else:
        if delikwent[2] < avg:
            print(delikwent[0:1],'young')
        else:
            print(delikwent[0:1], 'old')
