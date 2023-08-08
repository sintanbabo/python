print('='*60)
print('thread')
print('='*60)

import threading
import time

def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2

results = {}
# t1 = threading.Thread(target=longSquare, args=(1,results))
# t2 = threading.Thread(target=longSquare, args=(2,results))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0,100)]
[t.start() for t in threads]
[t.join() for t in threads]

print(results)