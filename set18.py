#Write a program to create a set.
s={"1","2","3"}
print(type(s))
print(s)
print("**********************")

#Write a Python program to add member to a set.
s1={"abc","def"}
s1.add("manasa")
print(s1)
print("**********************")

#Write a Python program to remove item from a given set.
s1={'manasa', 'abc', 'def'}
s1.remove('abc')
print(s1)
print("**********************")

#Write a python program to create a intersection of set
s1={1,2,3,4,5,6}
s2={5,6,7,8,1,2}
s3=s1.intersection(s2)
print(s3)
print("**********************")


#Write a python program to createa union of set ?
s1={1,2,3,4,5,6}
s2={5,6,7,8,1,2}
s3=s1.union(s2)
print(s3)
print("**********************")

#Write a python program to create set differance ?
s1={1,2,3,4,5,6}
s2={5,6,7,8,1,2}
s3=s2.difference(s1)
print(s3)
print("**********************")

#Write a python program to create a symmetric defferance ?
s1={1,2,3,4,5,6}
s2={5,6,7,8,1,2}
s3=s1.symmetric_difference(s2)
print(s3)
print("**********************")

#Write a Python program to remove items 10, 20, 30 from the following set at once.?
s1={1,2,3,10,20,30,40}
s2={10,20,30}
s1.difference_update(s2)
print(s1)
print("**********************")

#Write program to iterate over sets.
s1={1,2,3,4,5,6}
for i in s1:
  print(i)
print("**********************")

#write a python program to find max and min values in a set?
s1={1,2,3,4,5,6,10}
max=max(s1)
min=min(s1)
print(max)
print(min)
print("*********************")

#Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.
s1={1,2,3,4,5,6}
s2={7,8,3,4,9,10}
s1.difference_update(s2)
print(s1)
print("**********************")

#Check if two sets have any elements in common. If yes, display the common elements?
s1={1,2,3,4,5}
s2={1,2,4,7,8}
s3=s1.intersection(s2)
if s3:
  print("display the common elements:",s3)
else:
   print("display the not common elements")
print(s3)
print("******************")

#Update set1 by adding items from set2, except common items?
s1={1,2,3,4,5}
s2={2,5,6,7}
s1.symmetric_difference_update(s2)
print(s1)
print("*******************")

#Remove items from set1 that are not common to both set1 and set2?
s1={1,2,3,4,5}
s2={2,3,4,6,7}
s1.intersection_update(s2)
print(s1)