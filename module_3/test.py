import bcrypt

password = '123'
bytes = password.encode('utf-8')
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(bytes, salt)
print(hash)

passw = input(">>>").encode('utf-8')

print(bcrypt.checkpw(passw, hash))