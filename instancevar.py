#Create a class Person that has instance variables name, age, and gender. Add methods to:
#Initialize these variables.
#Update the age.
#Display the person's information.
 #Exercise:
 #> Create multiple instances of the Person class.
 #> Change the age of one person and display the updated information.

class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def newage(self,updatedage):
        self.age=updatedage
    def display(self):
        print(self.name)
        print(self.age)
        print(self.gender)
p1=person("manasa",25,"female")
p2=person("ravi",27,"male")
p3=person("harini",21,"female")
p4=person("milo",5,"male")
p1.display()
print("________")
p2.display()
print("________")
p3.display()
print("________")
p4.display()
print("________")
print("updated age of person is:")
p2.newage(30)
p2.display()
print("______________________________")



#Create a class Company that keeps track of the total number of employees using a static variable total_employees. 
#Each employee has instance variables name and department. Every time an employee is added, the total_employees should increment.
#Exercise:
#>Create multiple employee instances.
#>Print the total number of employees after adding each new employee.
#>Check whether changing the total_employees in one instance affects the others.

class Company:
    totalemployees = 0

    def __init__(self, name, empid):
        self.name = name
        self.empid = empid
        Company.totalemployees += 1

    def display(self):
        print(self.name)
        print(self.empid)

    @staticmethod
    def get_totalemployees():
        print(Company.totalemployees)

e1 = Company("manasa", 1001)
Company.get_totalemployees()  

e2 = Company("hari", 1002)
Company.get_totalemployees()  

e3 = Company("teja",1003)
Company.get_totalemployees() 

e1.totalemployees = 10  


print("employee1 details:",e1.totalemployees)
print("employee2 details:",e2.totalemployees)
print("employee3S details:",e3.totalemployees)

Company.get_totalemployees()  
print("_____________________________")

#Create a class Rectangle that has instance variables length and width. 
#Add a method calculate_area that calculates and prints the area of the rectangle using local variables inside the method.
#Exercise:
#>Create instances of the Rectangle class with different lengths and widths.
#>Calculate and print the area for each rectangle.

class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        area = self.length * self.width
        print("Area of a rectangle:",area)
r1=rectangle(5,6)
r2=rectangle(5.5,6.6)
r3=rectangle(7,7)
r1.calculate_area()
r2.calculate_area()
r3.calculate_area()
print("________________________")

#Create a class Employee where:
#Each employee has an instance variable salary.
#There is a static variable bonus shared by all employees. The bonus is applied to each employee's salary.
#Write a method total_salary that calculates the total salary for an employee (including the bonus).
#Exercise:
#>Create several employee instances with different salaries.
#>Change the bonus amount (static variable) and see how it affects all employees.
#>Calculate and print the total salary for each employee

class employee:
    bonus=1000
    def __init__(self,salary):
        self.salary=salary
    def display(self):
        total = self.salary + employee.bonus
        print("employee bonus is:",total)
e1=employee(10000)
e1.display()
e2=employee(20000)
e2.display()
e3=employee(30000)
e3.display()



        
