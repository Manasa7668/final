#basic dictionary syntax 
dict ={
    "name":"manasa",
    "boolean" : True,
    "year" :2024
} 
print(type(dict))
print(dict["name"])

#	Write a python program to  add a key to a dictionary ?

dict ={
    "name":"manasa",
    "boolean" : True,
    "year" :2024
} 
dict["address"] = "hyderabad"

print(dict)

#
"""dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 15, 'd': 25}
x= dict1 =+ dict2
print(x)
"""

"""x=int(input("enter x value:"))
y=int(input("enter x value:"))
sum=x+y
print("sum of values is:",sum)
"""


class rectangle:
    def area(self,l,w):
      return l*w
r=rectangle()
print(r.area(4,5))

print("**************************")


class company:
    def __init__(self,name,empid,companyname,salary):
        self.name=name
        self.empid=empid
        self.companyname=companyname
        self.salary=salary
    def getdetails(self):
        print("name is :",self.name)
        print("empid is:",self.empid)
        print("company name is:",self.companyname)
        print("salary is:",self.salary)
c=company("manasa",10101,"skywaves",12000)
c.getdetails()
print("**************************")

class metro:
    def __init__(self,startingpoint,endpoint,centerpoint,noofstops):
        self.startingpoint = startingpoint
        self.endpointpoint = endpoint
        self.centerpoint = centerpoint       
        self.noofstops = noofstops
    def getvalues(self):
        print("startingpoint is:",self.startingpoint)
        print("endpoint is:",self.endpointpoint)
        print("centerpoint is:",self.centerpoint)
        print("noof stops are:",self.noofstops)
m=metro("lbnagar","raidurg","ameerpet",22)
m.getvalues()
print("*************************************************")


class values:
    def __init__(self,x,y):
     self.x=x
     self.y=y
    def numbers(self):
        print("x value is:",self.x)
        print("y value is:",self.y)
m=values(5,6)
m.numbers()
print("*******************************************")
    
class arithematic:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mult(self,x,y):
        return x*y
    def expo(self,x,y):
        return x**y
    def mod(self,x,y):
        return x//y
    def division(self,x,y):
        return x%y
a=arithematic()
print(a.add(4,6))
print(a.sub(4,6))
print(a.mult(4,6))
print(a.expo(4,6))
print(a.mod(4,6))
print(a.division(4,6))
print("*********************************************")

class logical:
    def anddd(self,a,b):
        return a and b
    def orrr(self,a,b):
        return a or b
    def notttt(self,a,b):
        return not b
l=logical()
print(l.anddd(True,False))
print(l.orrr(True,False))
print(l.notttt(True,True))
print("*******************************")

class subjects:
    def __init__(self,subject1,subject2,subject3):
        self.subject1=subject1
        self.subject2=subject2
        self.subject3=subject3
    def getsubject(self):
        print("subject1 is:",self.subject1)
        print("subject2 is:",self.subject2)
        print("subject3 is:",self.subject3)
s=subjects("maths","python","science")
s.getsubject()
print("***********************")



















