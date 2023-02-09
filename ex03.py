message = 'hello world HELLO WORLD'
offset = 15


for i in message:
    if ord('a') <= ord(i) <= ord('z'):
        print(i)
    else:
        print("@!@")
    
    if ord('A') <= ord(i) <= ord('Z'):
        print(i)
    else:
        print("@!@")

