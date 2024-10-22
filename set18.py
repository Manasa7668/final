#syntax for set

s={}

print(type(s))



#Write a program to create a set.

s={1,2,3,4}

print(s)

print("*********************************")



#Write program to iterate over sets.

s={1,2,3,4,5}

for i in s:

    print(i)

print("*********************")



#Write a Python program to add member to a set.

s={1,2,3,4,5}

s.add("manasa")

print(s)

print("********************")



#Write a Python program to remove item from a given set.

s={1,2,3,4,5}

s.remove(2)

print(s)

print("********************")



#Write a python program to create a intersection of set ?

s1={1,2,3,4,5}

s2={2,4,5,6,7}

s3=s1.intersection(s2)

print(s3)

print("********************")



#Write a python program to createa unionof set ?

s1={1,2,3,4,5}

s2={2,4,5,6,7}

s3=s1.union(s2)

print(s3)

print("********************")



#Write a python program to create set differance ?

s1={1,2,3,4,5}

s2={2,4,5,6,7}

s3=s1.difference(s2)

print(s3)

print("********************")



#Write a python program to create a symmetric defferance ?

s1={1,2,3,4,5}

s2={2,4,5,6,7}

s3=s1.symmetric_difference(s2)

print(s3)

print("********************")



#write a python program to find max and min values in a set?

s={1, 3, 6, 7}

s1=max(s)

print("max value is:",s1)

s1=min(s)

print("min value is",s1)



#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

s1={1,2,3,4,5}

s2={2,4,5,6,7}

s1.difference_update(s2)

print(s1)

print("*************************")





#Write a Python program to remove items 10, 20, 30 from the following set at once.?

s1={1,2,3,4,5,10,20,30,40}

s2={10,20,30}

s1.difference_update(s2)

print(s1)

print("****************************")



#Check if two sets have any elements in common. If yes, display the common elements?

s1={1,2,3,4,5,10,20,30,40}

s2={10,20,30}

s3=s1.intersection(s2)

if s3:

    print("common elements are :",s3)

else:

    print("no common elements")

print("*******************")





#Update set1 by adding items from set2, except common items?

s1={1,2,3,4,5,10,20,30,40}

s2={10,20,30}

s3=s1.difference(s2)

s1.update(s3)

print(s3)

print("**********************************")



#Remove items from set1 that are not common to both set1 and set2?

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 6, 7}
s1.symmetric_difference_update(s2)
print(s1)











