
import time
import matplotlib.pyplot as plt

def fibonaci(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibo(num-1) + fibo(num-2)
    elif num == 0:
        return 0
    
    

dict1 = {}

for x in range(35):
    

    start = time.time()

    fibo(x)

    end = time.time()
    dict1[x] = (end - start)
    
print(dict1)

plt.bar(range(len(dict1)), list(dict1.values()), align='center')
plt.xticks(range(len(dict1)), list(dict1.keys()))

plt.show()
