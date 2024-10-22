#tuple syntax

t=()

print(type(t))

print("************************************")



#How do you create a empty tuple on python ?

t=()

print(t)

print("************************************")



#Write a python program to unpack atuple into several variables ?

t=("apple","ball","cat","dog")

(a,b,*c,d)=t

print(a)

print(c)

print("**************************")



#write a python program to add an item to the tuple ?

t=("apple","ball","cat","dog")

t1=("egg",)

t3=t+t1

print(t3)

print("***************************")



#Write a python proram to convert tuple into a string ?

t=("apple","ball","cat","dog")

t1=str(t)

print(t1)

print(type(t1))

print("*********************************")



#Write a python program to find most frequent element in tuple ?

t = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5)

cnt = 0

res = t[0]

 

for i in t:

    curr_freq = t.count(i)

 

    if(curr_freq > cnt):

        cnt = curr_freq

        res = i


print("Maximum element frequency tuple : " + str(res))

