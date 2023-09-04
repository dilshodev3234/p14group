from datetime import timedelta

import redis

con = redis.Redis(decode_responses=True)
# con.set("userl:1", "Botirjon1" , 10)
# con.hset("user:1" , mapping=[1,3,4])
con.delete("botir")
# print(con.hgetall("user:1"))
# con.close()




