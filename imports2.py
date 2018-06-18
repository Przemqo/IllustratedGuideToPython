import os

def contents(path):
    ext = {}
    lista = os.listdir(path)

    for file in lista:
        ext.update({file[-3:] : 1})

    for file in lista:
        if file[-3:] in ext:
            ext[file[-3:]] += 1
    return ext


print(contents(r'C:\Users\Przemqo\Python\Code'))