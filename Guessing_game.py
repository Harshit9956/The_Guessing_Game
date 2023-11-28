# importint the random Module

import random
# generating random number
a=random.randint(0,10)

# Taking uers answer
user_input=int(input('Enter your number '))
attempt=1

while user_input!=a:
    if user_input>a:
        print('Wrong guess\n  guess smaller number')
    else:
        print('Wrong guess\n  guess greater number number')
    user_input=int(input('Enter your number '))
    attempt=attempt+1

print('Right guess')
print(f'you guessed the right answer in {attempt} attempt')



