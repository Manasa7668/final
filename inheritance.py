#Inheritance :Inheritance is a method through which one class inherits the properties from its parent class
#types:
#single inheritance
#multiple inheritance
#multilevel inheritance
#hierarchical inheritance
#hybrid inheritance


#single inheritance
print("_____________single inheritance________________")
class parent:
    def person(self,name,empid):
        self.name=name
        self.empid=empid
        print(self.name)
        print(self.empid)


    
class child(parent):
    def display(self,salary):
        self.salary=salary
        print(self.salary)

        
c=child()
c.display(11101)
c.person("manasa",101)
c.display(20000)
c.person("sireesha",102)
print("******************************")

class stores:
    def display(self,brand,color):
        self.brand=brand
        self.color=color
        print("brand is:",self.brand)
        print("color is:",self.color)
class child(stores):
    def _cloth(self,size):
        self.size=size
        print("size is:",self.size)
c=child()
c._cloth("m")
c.display("h&m","red")
print("******************************")

class vehicles:
    def m1(self,brand,model):
        self.brand=brand
        self.model=model
        print("brand is:",self.brand)
        print("model is:",self.model)
class bike(vehicles):
    def funct1(self,clutch):
        self.clutch=clutch
        print("clutch is",self.clutch)
b=bike()
b.funct1("right")
b.m1("ktm","ktm5")
    



#multiple inheritance
print("____________multiple inheritance_________________")
class parent:
    def m1(self):
        print("method1 is created")
class subparent:
    def m2(self):
        print("method2 is created")
class child(subparent,parent):
    def m3(self):
        print("method3 is created")
c=child()
c.m1()
c.m2()
c.m3()
print("******************************")

class father:
    def m1(self,fathername,surname):
        self.fathername=fathername
        self.surname=surname
        
class mother:
    def m2(self,mothername,lastname):
        self.mothername=mothername
        self.lastname=lastname
        
class daughter(father,mother):
    def m3(self,surname,daughtername,lastname):
        self.lastname=lastname
        self.surname=surname
        self.daughtername = daughtername
        name=self.surname+self.daughtername+self.lastname
        print("daughter name is:",name)
s=daughter()
s.m3("maddela"," manasa"," reddy")
s.m2("aruna","reddy")
s.m1("yadaiah","maddela")
print("*******************")

class phone:
    def call(self,contacts):
        self.contacts=contacts
        print(self.contacts)
class camera:
    def c(self,quality,pixel):
        self.quality=quality
        print(self.quality)
        self.pixel=pixel
        print(self.pixel)
class screen:
    def sc(self,apps):
        self.apps=apps
        print(self.apps)
class main(phone,screen,camera):
    def display(self):
        print("software is updated")
m=main()
m.display
m.call(1234567890)
m.c("good","5pixel")
m.sc("teams")

#Multilevel Inheritance
print("____________multilevel inheritance_________________")

class parent:
    def funct1(self):
        print("this is parent class")
class subparent(parent):
    def funct2(self):
        print("this is sub_parent class")
class child(subparent):
    def funct3(self):
        print("this is child class")
c=child()
c.funct1()
c.funct2()
c.funct3()

print("*****************")

class company:
    def funct1(self,companyname):
        self.companyname=companyname
        print("company name is:",self.companyname)
class manager(company):
    def funct2(self, teamsize):
        self.teamsize=teamsize
        print("teamsize is=",self.teamsize)
class employee(manager):
    def funct3(self,name,empid):
        self.name=name
        self.empid=empid
        print("employee name is:",self.name)
        print("employeeid name is:",self.empid)
e=employee()
e.funct1("skywaves")
e.funct2(15)
e.funct3("manasa",1011)
print("******************")
class education:
    def displayed(self, name):
        self.name = name
        print(self.name)

class student(education):
    def studentinformation(self, name, studentid, grade):
        self.name = name
        self.studentid = studentid
        self.grade = grade
        print(self.name)
        print(self.studentid)
        print(self.grade)

class seminar(student):
    def display(self, topic):
        self.topic = topic
        print(self.topic)


s=seminar()
s.display("enviromental studies")
s.studentinformation("manasa",22,89)
s.displayed("rahul")



#hierarchical Inheritance
print("_______hierarchical inheritance_________________")

class parent:
    def funct1(self):
        print("this is hierarchical parent class")
class subparent(parent):
    def funct2(self):
        print("this is hierarchical sub_parent class")
class child(parent):
    def funct3(self):
        print("this is hierarchical child class")

c=child()
c.funct3()
c.funct1()
s=subparent()
s.funct2()
s.funct1()

print("*****************")
class employee:
    def f1(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        print(self.name)
        print(self.employee_id)

class engineer(employee):
    def f2(self,specialization):
        self.specialization = specialization
        print(self.specialization)

class manager(employee):
    def f3(self,team_size):
        self.team_size = team_size
        print(self.team_size)

class intern(employee):
    def f4(self,duration):
        self.duration = duration
        print(self.duration)
e=engineer()
e.f2("software developer")
m=manager()
m.f3(22)
i=intern()
i.f4("6-month")



print("************************")
class education:
    def displayed(self, name):
        self.name = name
        print(self.name)

class student(education):
    def studentinformation(self, name, studentid, grade):
        self.name = name
        self.studentid = studentid
        self.grade = grade
        print(self.name)
        print(self.studentid)
        print(self.grade)

class seminar(education):
    def display(self, topic):
        self.topic = topic
        print(self.topic)
s=seminar()
s.display("trignometery")
ss=student()
ss.studentinformation("manasa",101,23)

#hybrid inheritance
print("____________________hybrid inheritance________________")
class parent:
    def funct1(self):
        print("this is hierarchical parent class")
class subparent(parent):
    def funct2(self):
        print("this is hierarchical sub_parent class")
class child(parent):
    def funct3(self):
        print("this is hierarchical child class")
class main(subparent,child):
       def display(self):
           print("this is main class")

m=main()
m.display()
m.funct3()
m.funct1()
m.funct2()
print("**********************")
class person:
    def f1(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

class staff(person):
    def f2(self,staffid):
        self.staffid = staffid
        print(self.staffid)

class patient(person):
    def f3(self,patient_id, ailment):
        self.patient_id = patient_id
        self.ailment = ailment
        print(self.patient_id)
        print(self.ailment)

class doctor(staff):
    def f4(self,specialization):
        self.specialization = specialization
        print(self.specialization)

class nurse(staff):
    def f5(self,shift):
        self.shift = shift
        print(self.shift)

class main(doctor,staff):
    def display(self):
        print("data is saved:")
m=main()
m.display()
m.f1("manasa",45)
m.f2(10)

    

