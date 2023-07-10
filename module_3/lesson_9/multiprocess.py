import asyncio
import multiprocessing
import threading
import time
from multiprocessing import Pool


# print(multiprocessing.cpu_count())

# def f(i):
#     file = open("test.txt" , "a")
#     file.write(str(i) + '\n')
#     file.close()


# start = time.time()

# p_list = []
# for i in range(10):
#     p = multiprocessing.Process(target=f, args=(i,))
#     p.start()
#     p_list.append(p)
# for i in p_list:
#     i.join()

# start = time.time()
#
# with Pool() as pool:
#     pool.map(f, list(range(1000)))
# print(time.time() - start)


# start = time.time()
# l = []
# for i in range(1000):
#     t = threading.Thread(target=f , args=(i,))
#     t.start()
#     l.append(t)
#
# for i in l:
#     i.join()
#
# print(time.time() - start)

