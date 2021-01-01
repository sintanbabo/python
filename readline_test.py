# readline
f = open("new.txt",'r')
while True :
	line = f.readline()
	if not line : break
	print(line)
f.close()

# readlines
f = open("new.txt",'r')
lines = f.readlines()
for line in lines :
	print(line)
f.close()

# read
f = open("new.txt",'r')
data = f.read()
print(data)
f.close()
