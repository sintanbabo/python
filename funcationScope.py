print('-'*80)
print(f'funcationScope')
print('-'*80)

def performOperation(*args,**kwargs):
    print(args)
    print(kwargs)

print('----- first' + '-' * 30)
performOperation(1,2,operation='sum')

def performOperation(num1, num2, operation='sum'):
    print(locals())

print('----- second' + '-' * 30)
performOperation(1,2,operation='sum')

print('----- third' + '-' * 30)
print(globals())