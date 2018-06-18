for letter in ['c', 'a', 't']:
    print(letter)

print(letter)

animals = ['Kot', 'Pies', 'Ptasior']
for index,value in enumerate(animals):
    print(index, value)


numbers = [3, 5, 9, -1, 7, 2]
wynik = 0
for item in numbers:
    if item < 0:
        break
    wynik += item

print(wynik)

#A teraz zamiast zatrzymania, pominmy ujemne

numbers = [3, 5, 9, -1, 7, 2]
wynik = 0
for item in numbers:
    if item < 0:
        continue
    wynik += item

print(wynik)



#membership

print("Pies" in animals)

print(animals.index('Pies'))


names = ['John', 'Paul', 'George', 'Ringo']
names_to_remove = []

for name in names:
    if name not in ['John', 'George']:
        names_to_remove.append(name)

for name in names_to_remove:
    names.remove(name)

print(names)

#else w petli for jest wykonywane zawsze jezeli reszta zostala wykonana
Negative = True

for number in numbers:
    if number < 0:
        break
else:
    Negative = False

print('Negative: ', Negative)

n = 3
while n > 0:
    print(n)
    n = n - 1

n = 3

while True:
    print(n)
    n = n - 1
    if n == 0:
        break

