#count occurrence of a given characters in string
"""s = "learning python is easy"
print(s.count('e'))

#to check if two Strings are Anagram
s1="sample"
s2="amples"
if (s1,s2):
    print("anagram")
else:
    print("not a anagram")"""


#
"""s="maars"
s1=isPalindrome(s) # type: ignore
if s1 :
 print("true")
else:
   print("false")"""

#replace the string space with a given character.
s="learning python is very easy"
s1=s.replace(" ","s")
print(s1)

#convert lowercase char to uppercase of string. 
s="easy to learn"
s1=s.upper()
print(s1)

#check given character is digit or not using isdigit() method.
#s=input("enter digit")
s="1234"
s1=s.isdigit()
print(s1)


#remove blank space from string.
s="learing python is easy"
s1=s.replace(" ","")
print(s1)


#concatenate two strings using join() method.
s1="python"
s2="easy"
conc="".join([s1,s2])
print(conc)

#concatenate two strings without using join() method. 
s1="abcd"
s2="efgh"
s3=s1+s2
print(s3)

#remove repeated character from string.
s="learing python is easy"
s1=s.replace("e","")
s2=s.replace("a","")
s3=s.replace("i","")
s4=s.replace("n","")
s5=s.replace("y","")
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

#check given character is digit or not. 
s="123"
s1=s.isdigit()
print(s1)


#print the highest frequency character in a String. 
s="A"
s1="a"
if s>s1:
    print("greater",s)
else:
    print("lessar",s1)
