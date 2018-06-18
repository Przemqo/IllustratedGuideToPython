info = {'first':'Peter','last':'Best'}
print(type(info))

info2 = dict(first='Peter', last='Best')

info['age'] = 20
info['job'] = 'Drummer'

print(info['age'])

print('Band' in info)
print('first' in info)

laster = info.get('last')
print(laster)

genre = info.get('Genre','Rock')
print(genre)

names = ['Ringo', 'Paul', 'John', 'Ringo']

count = {} #empty dictionary
print(type(count))

for name in names:
    count.setdefault(name,0)
    count[name] += 1
    print(count)
    print(type(count))

band_1_names = ['John', 'George','Paul', 'Ringo']
band_2_names = ['Paul']

names_to_bands = {} #again

for name in band_1_names:
    names_to_bands.setdefault(name,[]).append('Beatles')

for name in band_2_names:
    names_to_bands.setdefault(name,[]).append('Wings')

print(names_to_bands)
print(names_to_bands['Paul'])

#removing key from dictionary {}
del names_to_bands['Ringo']

print(names_to_bands)

#iteration
data = {'Adam': 2,'Zeek': 5, 'Brian': 3}

for obiekt in data:
    print(obiekt)

#display value instead key

for obiekt in data.values():
    print(obiekt)

#display both

for klucz,wartosc in data.items():
    print(klucz, wartosc)

#rev sort
for obiekt in sorted(data.keys(),reverse = True):
    print(obiekt)