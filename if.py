year = 2000
if (year % 4 == 0):
    if (year % 100 == 0 and year % 400 == 0):
        print('Leap Year')
else:
    print('Regular Year')

if (year % 2 == 0):
    print('Regular number')
else:
    print('Odd number')

matt = list('matt')
matt.append('Fred')
matt.insert(1,'George')
matt[3] = 'Mr T'
matt.remove('t')
del matt[2]
print(matt)
matt.sort()
print(matt)