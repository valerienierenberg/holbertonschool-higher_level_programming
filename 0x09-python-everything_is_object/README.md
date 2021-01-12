# 0x09-python-everything_is_object

0-answer.txt - What function would you use to print the type of an object?\
1-answer.txt - How do you get the variable identifier (which is the memory address in the CPython implementation)?\
2-answer.txt - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = 100
```
3-answer.txt - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = 89
```
4-answer.txt - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = a
```
5-answer.txt - In the following code, do a and b point to the same object?
```
>>> a = 89
>>> b = a + 1
```
6-answer.txt - What do these three lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```
7-answer.txt - What do these three lines print?
```
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```
8-answer.txt - What do these three lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```
9-answer.txt - What do these three lines print?
```
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```
10-answer.txt - What do these three lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```
11-answer.txt - What do these three lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```
12-answer.txt - What do these three lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
13-answer.txt - What do these three lines print?
```
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
14-answer.txt - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
15-answer.txt - What does this script print?
```
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
16-answer.txt - What does this script print?
```
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
17-answer.txt - What does this script print?
```
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
18-answer.txt - What does this script print?
```
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
19-copy_list.py - function def copy_list(l): that returns a copy of a list.
```
cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
```
20-answer.txt - a = () - Is a a tuple?\
21-answer.txt - a = (1, 2) - Is a a tuple?\
22-answer.txt - a = (1) - Is a a tuple?\
23-answer.txt - a = (1, ) - Is a a tuple?\
24-answer.txt - What does this script print?\
25-answer.txt - What does this script print?
```
a = (1, 2)
b = (1, 2)
a is b
```
26-answer.txt - What does this script print?
```
a = ()
b = ()
a is b
```
27-answer.txt - Will the last line of this script print 139926795932424?
```
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
28-answer.txt - Will the last line of this script print 139926795932424?
```
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
(Task 29 - blog post on Linkedin)\
100-magic_string.py - function magic_string() that returns a string “Holberton” n times the number of the iteration (see code)
```
cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())
```
101-locked_class.py - class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.
```
cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```
103-line1.txt - How many int objects are created by the execution of the first line of the script?
```
cat int.py 
a = 1
b = 1
```
103-line2.txt - How many int objects are created by the execution of the second line of the script?
```
cat int.py 
a = 1
b = 1
```
104-line1.txt - How many int objects are created by the execution of the first line of the script?
```
cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
104-line2.txt - How many int objects are created by the execution of the second line of the script?
```
cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
104-line3.txt - After the execution of line 3, is the int object pointed by a deleted?
```
cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
104-line4.txt - After the execution of line 4, is the int object pointed by b deleted?
```
cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
104-line5.txt - How many int objects are created by the execution of the last line of the script
```
cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
105-line1.txt - Before the execution of line 2 (print("Love")), how many int objects have been created and are
still in memory?
```
cat int.py 
print("I")
print("Love")
print("Python")
```
106-line1.txt - How many string objects are created by the execution of the first line of the script?
```
cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
106-line2.txt - How many string objects are created by the execution of the second line of the script?
```
cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
106-line3.txt - After the execution of line 3, is the string object pointed by a deleted?
```
cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
106-line4.txt - After the execution of line 4, is the string object pointed by b deleted?
```
cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
```
106-line5.txt - How many string objects are created by the execution of the last line of the script?
