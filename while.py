from datetime import datetime

'''
wait_until = datetime.now().second + 2

while datetime.now().second != wait_until:
    continue
    print('Still waiting')
    
print(f'We are at {wait_until} seconds!')
'''

wait_until = datetime.now().second + 2

while True:
    if datetime.now().second < wait_until:
        continue
    break
    
print(f'We are at {wait_until} seconds!')