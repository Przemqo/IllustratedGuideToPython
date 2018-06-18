multiple = "This one is containing \nmultiple lines"
nsnake = '\N{SNAKE}'
backslash = '\\'
print(multiple)
print(nsnake)

slash_t=r'\tText \\'
print(slash_t)
normal='\tText \\'
print(normal)
two_lines="""Dwie
linie"""
print(two_lines)

name = "Przemek"
print('Witaj {}'.format(name))

print("Name: {:*^12}".format("Ringo"))
print("Percent: {:=+10.1%}".format(-44/100))
print("Binary: {:b}".format(12))
print("Hex: {:x}".format(12))
print("Decimal %d, Hex %x" % (12,13))

name = 'PrZemeK'
#print(f'My name is {name.capitalize()}')

print(name.lower())

print(f'Square root of two is: {2 ** 0.5:5.3f}')