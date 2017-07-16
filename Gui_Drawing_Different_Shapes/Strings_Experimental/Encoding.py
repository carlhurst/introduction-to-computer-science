

msg = input("please input a message: ")

print("the message is {} \n".format(msg))

# Teacher sees

msgls =[]

for c in msg:
    msgls.append(ord(c))
    print(ord(c),end="")
print("\n")
decode = []

for i in msgls:
    decode.append(chr(i))

for i in decode:
    print(i, end="")