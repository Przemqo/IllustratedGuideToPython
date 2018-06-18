def calculator(num1, num2, operator):
    try:
        if operator == '+': return num1 + num2
        elif operator == '-': return num1 - num2
        elif operator == '*': return num1 * num2
        elif operator == '/': 
            try:
                return num1 / num2
            except ZeroDivisionError:
                return 'Division by zero'
        else:
            return('Please use proper operator')
    except TypeError:
        return('Wrong type of numeric input')
    

print(calculator(3,'s','-'))