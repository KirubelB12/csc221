import random
i = 1
x = random.randint(0, 1000)
print('Guess a number from 0 and 1000')
x = 1
while x < 100:
    print('x is', x)
    x = x + 610

from random import randint

while True:
    x = randint(1, 10)
    print(x)
    if x == 5:
        break
    print('x was not 5!')

from gasp.utils import read_number
read_number()