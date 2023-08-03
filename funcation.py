print('-'*80)
print(f'funcation')
print('-'*80)

import math

def performOperation(num1, num2, operation='sum', message='Default message'):
    print(f'{message}')
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2

print('-'*80)
print(performOperation(2,3))

print('-'*80)
print(performOperation(2,3,message='A new message', operation='multiply'))
print('-'*80)

def performOperation(*args,operation='sum'):
    if operation == 'sum':
        return sum(args)
    if operation == 'muliply':
        return math.prod(args)

print('-'*80)
print(performOperation(1,2,3,4,5,6,7, operation='sum'))
print('-'*80)
print(performOperation(1,2,3,4,5,6,7, operation='muliply'))
print('-'*80)