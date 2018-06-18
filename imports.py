import json

name = 'Przemek'
age = 27
parse = {'name':name,'age':age}

jsonek= json.dumps(parse)

restore = json.loads(jsonek)