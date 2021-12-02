import hashlib

notFound = True
solution = 0
padding = 6
basekey = "ckczppom"

while notFound:
    solution += 1
    hashkey = basekey + str(solution)
    result = hashlib.md5(hashkey.encode())
    md5 = result.hexdigest()
    md5_padding = md5[0 : padding]
    if len(set(md5_padding)) == 1:
        if str(md5_padding[0]) == '0':
            print(solution)
            break


'''
# encoding GeeksforGeeks using encode()
# then sending to md5()
result = hashlib.md5(hashkey.encode())
  
# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
'''
