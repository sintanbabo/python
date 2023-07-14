#------------------------------------------------------------
print("=" * 50)
print("02-2.py")
print("=" * 50)

#-------------------------------------------------------------
# string expression

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says'
print(say)

multiline = "Life is too short\nYou need python"
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)

multiline = '''
Life is too short
You need python
'''
print(multiline)

#-------------------------------------------------------------
# string operation

head = "Python"
tail = " is fun!"
print(head+tail)

#------------------------------------------------------------
# indexing
a = "Life is too short, You need python"
print(len(a))
print("\n")

#------------------------------------------------------------
# slicing
a = "Life is too short, You need python"
print(a[3])
print(a[0:5])
print(a[:19])
print(a[19:])
print("\n")

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year)
print(day)
print(weather)
print("\n")

#------------------------------------------------------------
# formatting
a = "I eat %d apples." % 3
print(a)

a = "I eat %s apples." % "five"
print(a)

number = 3
a = "I eat %d apples." % number
print(a)

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

b = "Error is %d%%" % 98
print(b)

print("%10s" % "hi\n")

print("%-10sjane." % "hi")

print("%10.4f" % 3.14134234)