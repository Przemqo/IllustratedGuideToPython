def is_odd(num):
    if (num % 2 == 0):
        return True
    else:
        return False

def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num % i == 0:
            return False
        else:
            return True


def binary_search(array, number):
    if len(array) == 0:
        return False
    else:
        midpoint = int(len(array)/2)
        if array[midpoint] == number:
            return True
        else:
            if number < array[midpoint]:
                return binary_search(array[:midpoint], number)
            else:
                return binary_search(array[midpoint+1:], number)

def binary_search_it(array, number):
    if len(array) == 0:
        return False
    else:
        start = 0
        end = len(array) - 1

        while start <= end:
            mid = int((start + end)/2)
            if array[mid] == number:
                return mid
            elif number < array[mid]:
                end =  mid - 1
            else:
                start = mid + 1         
        else:
                return -1

def convert(tekst,separator='_'):
    i = 1
    tekst = tekst[0].lower() + tekst[1:]
    while i < len(tekst) - 1:
        if tekst[i].isupper() == True:
            tekst = tekst[:i] + separator + tekst[i].lower() + tekst[i+1:]
            i += 2
        else:
            i += 1
    return tekst



print(is_odd(4))
print(is_odd(7))

print(is_prime(1))
print(is_prime(17))

ciag = [0, 1, 2, 3, 4, 5, 6]

#print(binary_search(ciag,4))
print(binary_search_it(ciag,7))

print(convert("ExampleCamelCase"))
print(convert("ExampleCamelCase",'-'))

