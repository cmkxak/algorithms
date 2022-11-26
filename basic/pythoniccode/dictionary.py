import time
start = time.time()

data = [i for i in range(100000)]
for i in range(10000):
    if i in data:
        print(1)

print(f"{time.time()-start:.4f} sec")