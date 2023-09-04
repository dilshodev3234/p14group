from task import task1, task2, task3
import time


start = time.time()
task1.delay()
task2.delay()
task3.delay()
print(time.time() - start)
