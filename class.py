import random
import time

class Chair: # 1
    ''' A Chair on a chairlift ''' # 2
    max_occupants = 4 # 3
    
    def __init__(self, id): # 4
        self.id = id # 5
        self.count = 0

    def load(self, number): # 6
        new_value = self.check(self.count + number)
        self.count = new_value
    def unload(self, number): # 7
        new_value = self.check(self.count - number)
        self.count = new_value

    def check(self, number):
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid number:{}'.format(number))
        return number

chair = Chair(1)

print(chair.count)
print(chair.max_occupants)
chair.load(3)
print(chair.count)
chair.unload(2)
print(chair.count)

#Constant chairlifts number
NUM_CHAIRS = 100

#Initiating chairs list
chairs = []

for num in range(1,NUM_CHAIRS + 1):
    chairs.append(Chair(num))

#Avg number of filled chairs per chairlift

def avg(chairs):
    total = 0
    for c in chairs:
        total += c.count
    return total / len(chairs)

in_use = []
transported = 0

while True:
    #loading
    loading = chairs.pop(0)
    in_use.append(loading)
    in_use[-1].load(random.randint(0,Chair.max_occupants))

    #unloading (first chair gets to top)
    if len(in_use) > NUM_CHAIRS / 2:
        unloading = in_use.pop(0)
        transported += unloading.count
        unloading.unload(unloading.count)
        chairs.append(unloading)

    #Status message
    print('Loading Chair {} Load {} Avg. Load {:.2} Total Transported {}'.format
        (loading.id, loading.count, avg(in_use), transported))

    #Wait and repeat
    time.sleep(1)