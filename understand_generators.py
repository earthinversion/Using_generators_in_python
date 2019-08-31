import time, psutil
import numpy as np

def memory_total():
        mem_total = psutil.virtual_memory().total
        mem_used = psutil.virtual_memory().used
        return (mem_total,mem_used)

## Function to take squares of numbers
def squares(num):
        results=[]
        for i in num:
                results.append(i**2)
        return results

def squares_gen(num):
        for i in num:
                yield i**2


num = np.arange(1,10000000)

# Using Function
print('--> --> Function')
## List
print('--> List')
print('Memory (total, used)',memory_total())
t1l = time.process_time()
resl = squares(num)
t2l = time.process_time()
ttl = t2l-t1l
print('Elapsed time for list: {} Seconds'.format(ttl))
print('Memory (total, used)',memory_total())

## Generators
print('--> Generators')

print('Memory (total, used)',memory_total())
t1g = time.process_time()
resg = squares_gen(num)
t2g = time.process_time()
ttg = t2g-t1g
print('Elapsed time for generators: {} Seconds'.format(ttg))

print("Difference between the two: {} Seconds".format(ttl-ttg))
print('Memory (total, used)',memory_total())




# Using comprehension
print('--> --> Comprehension')
## List
print('--> List')

print('Memory (total, used)',memory_total())
t1l = time.process_time()
resl = [i**2 for i in num]
t2l = time.process_time()
ttl = t2l-t1l
print('Elapsed time for list: {} Seconds'.format(ttl))
print('Memory (total, used)',memory_total())


## Generators
print('--> Generators')

print('Memory (total, used)',memory_total())
t1g = time.process_time()
resg = (i**2 for i in num)
t2g = time.process_time()
ttg = t2g-t1g
print('Elapsed time for generators: {} Seconds'.format(ttg))
print("Difference between the two: {} Seconds".format(ttl-ttg))
print('Memory (total, used)',memory_total())