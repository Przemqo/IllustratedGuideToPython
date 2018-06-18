digits = [0, 2, 2, 3, 5, 6, 8, 9]

set_digits = set(digits)

print(digits)
print(set_digits)

set_digits2 = {2, 3, 3, 4, 5, 7, 9}
print(set_digits2)

print(3 in set_digits2)
print(6 in set_digits2)

odd = {1, 3, 5, 7, 9}
print(type(odd))
even = set_digits - odd
print(even)

prime = set([2, 3, 5, 7])

prime_even = prime & even

print(prime_even)

prime_and_even = prime | even
print(prime_and_even)


first = {1, 2, 3, 4, 5}
second = {5, 6, 7, 8, 9}

xor = first ^ second
print(xor)