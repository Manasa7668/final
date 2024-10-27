#syntax for list
list=[]
print(type(list))


#Write a python program to merge two list?
#type 1
l1=[1,2,3,4]
l2=["a",2,2]
l3=l1+l2
print(l3)
print("**********************")

#type2
#l1=[1,2,3,4]
#l2=["a",2,2]
#l1.extend(l2)
#print(l1)
#print("**********************")


#Write a python program to delete element of given index in list ?

l1=["apple","ball","cat","dog"]
l1.pop(1)
print(l1)
print("***************************")
	
#	Write a pytho program to delete given element from the list?
l1=["apple","ball","cat","dog"]
l1.remove("cat")
print(l1)
print("***************************")

#Write  a python programe to remove duplicates from the list ?
l1=[1,2,2,333,3,3,3,4,5,4,5,5,5]
l2 =list(set(l1))
print(l2)
	
	
	

	