import datetime

with open("/home/dilshod/PycharmProjects/p14_group/module_4/DB/lesson_9/user.txt" , 'a') as f:
    f.write(str(datetime.datetime.now())+'\n')
