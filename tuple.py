#syntax of tuple
l=[1,2,3,4]
print(type(l))

# How do you create a empty tuple on python 
t=()
print(t)

#Write a python proram to convert tuple into a string ?
t=("s","b")
t1=str(t)
print(t1)

#write a python program to add an item to the tuple ?
t=("apple","ball")
t1=("cat",)
t += t1
print(t)


#Write a python program to unpack atuple into several variables ?
tuple=("apple","ball","cat","dog","egg")
(a,b,c,*d,e)= tuple
print(a)
print(c)
print(d)

