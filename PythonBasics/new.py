filex = open("ok.txt",'r')

filex.seek(0)

username = filex.readlines()[0].split(',')[0].rstrip('\n')

print(username)