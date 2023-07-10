
import threading
import time

def a():
    time.sleep(1)

def b():
    time.sleep(4)

# synchron mainthread

# start = time.time()
# a()  # 3
# b()  # 4
# print(time.time() - start)

# async MultiThread
# start = time.time()
# thread1 = threading.Thread(target= a)
# thread2 = threading.Thread(target= b)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(time.time() - start)

# start = time.time()
# l = []
# for i in range(1_000_000):
#     thread = threading.Thread(target=a)
#     thread.start()
#     l.append(thread)
#
# for i in l:
#     i.join()
#
# print(time.time() - start)



mail_list = ["saidakbaruraimov7@gmail.com",
"mohirmirahmadov@gmail.com",
"zoirbekergashev4567@gmail.com",
"khayrullo.devs@gmail.com",
"imonqulovf1234@gmail.com",
"samidilloravshanov13@gmail.com",
"shahrizodaxakimova12@gmail.com",
"shohjahonobruyev3@gmail.com",
"diyorbekdilmurodov1@gmail.com",
"suratovdoniyor@gmail.com",
"dilshodbekakhmatov@gmail.com",
"nurillayevezozbek@gmail.com",
"saidakbaruraimov7@gmail.com",
"mohirmirahmadov@gmail.com",
"zoirbekergashev4567@gmail.com",
"azamovshahboz06082001@gmail.com",
"boburkhonov99@mail.ru"
"doniyorbek068@gmail.com",
"ahmatovdilshodbek@gmail.com",
"isomiddinwtu@gmail.com",
"kodirovadilfuza9706@gmail.com",
"turgunovjamshid32@gmail.com",
"nabiyevadilnavoz736@gmail.com"]









