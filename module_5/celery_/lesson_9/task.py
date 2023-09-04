
import time
import celery

app = celery.Celery("main" , broker='redis://localhost:6379/0')

@app.task()
def task1():
    time.sleep(20)
    return "Task 1 finished"

@app.task()
def task2():
    time.sleep(20)
    return "Task 2 finished"

@app.task()
def task3():
    time.sleep(20)
    return "Task 3 finished"