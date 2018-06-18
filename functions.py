def add_2(num):
    '''
    Help for function add_2
    '''

    result  = num + 2
    return result

help(add_2)

print(add_2(3))

def add_2_num(a, b):
    return a + b

print (add_2_num(7,2))

#def parameters
def add_2_numv2(a, b=3):
    return a + b

print (add_2_num(7,2))
print(add_2_numv2(7))