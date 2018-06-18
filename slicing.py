imie = 'Przemek'
print(imie[0])
print(imie[-1])

filename = 'wirus.exe'

print(filename[-3:])

print(filename[:-4])

def is_palindrome(text):
    palindrome = True
    for i in range(len(text)):
        if text[i] != text[-i-1]:
            palindrome = False
    
    return palindrome

print(is_palindrome('ankna'))
