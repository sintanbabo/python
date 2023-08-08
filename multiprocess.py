print('='*60)
print(' multiprocess')
print('='*60)

from multiprocess import Process
import time

def longSquare(num, results):
    time.sleep(1)
    results[num] = num ** 2

results = {}
p1 = Process(target=longSquare, args=(1,results))
p2 = Process(target=longSquare, args=(2,results))

p1.start()
p2.start()

p1.join()
p2.join()

# threads = [threading.Thread(target=longSquare, args=(n, results)) for n in range(0,100)]
# [t.start() for t in threads]
# [t.join() for t in threads]

print(results)
