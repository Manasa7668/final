#1.Create a class Vehicle with attributes brand and year. The class should have a method get_info() that returns the brand and year of the vehicle. Then, create two subclasses:

#Car, which adds an attribute number_of_doors.
#Motorcycle, which adds an attribute has_sidecar.
#Both subclasses should override the get_info() method to include their respective additional attributes in the returned string.
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        print(self.brand)
        print(self.year)

class Car(Vehicle):
    def __init__(self, brand, year, number_of_doors):
        super().__init__(brand, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
       print(self.number_of_doors)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, has_sidecar):
        super().__init__(brand, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        m="has_sidecar" if self.has_sidecar else "no"
        print(self.has_sidecar)


v=Vehicle("motors",2201)
v.get_info()
c = Car("bmw", 2001, 4)
c.get_info()
mc= Motorcycle("ktm", 2004,True)       
mc.get_info()
print("_______________________________________")

#2.Define an abstract class Animal with an abstract method make_sound(). Then, create three classes that inherit from Animal:

#Dog with the sound "Woof".
#Cat with the sound "Meow".
#Cow with the sound "Moo".
#Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof"
class Cat(Animal):
    def make_sound(self):
        return "Meow"
class Cow(Animal):
    def make_sound(self):
        return "Moo"
def play_sound(animal):
    print(animal.make_sound())
d=Dog()
play_sound(d)
c=Cat()
play_sound(c)
cw=Cow()
play_sound(cw)
print("___________________________")

#3.Create an abstract class BankAccount with methods deposit(), withdraw(), and get_balance(). Then, create two subclasses:

#SavingsAccount, where the withdraw() method ensures that the balance cannot go below $500.
#CurrentAccount, where the withdraw() method allows the balance to go negative (up to $1000 overdraft).
#Ensure that only deposit() and withdraw() are exposed to the user, and the balance is encapsulated (hidden).
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self, initial_balance=0):
        self._balance = initial_balance
    @abstractmethod
    def deposit(self,amount):
        pass
    @abstractmethod
    def withdraw(self,amount):
        pass
    def get_balance(self):
        return self._balance
class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=500):
        super().__init__(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(self._balance)
        else:
            print("Deposit amount")
    
    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= 500:
            self._balance -= amount
            print(self._balance)
        else:
            print("Insufficient balance")
class CurrentAccount(BankAccount):


    def __init__(self, initial_balance=0):
        super().__init__(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(self._balance)
        else:
            print("Deposit amount")

    def withdraw(self, amount):
        if amount > 0 and (self._balance - amount) >= -1000:
            self._balance -= amount
            print(self._balance)
        else:
            print("Overdraft limit ")


savings_account = SavingsAccount(500)
current_account = CurrentAccount(400)

savings_account.deposit(400)          
savings_account.withdraw(400)         
current_account.deposit(3500)          
current_account.withdraw(200)        
print(savings_account.get_balance())  
print(current_account.get_balance()) 


#4.Create a base class Employee with attributes name and salary, and methods get_details() and get_salary(). Then create two subclasses:

#Manager, which adds an attribute department.
#Developer, which adds an attribute programming_language.
#Both subclasses should override the get_details() method to include their respective additional attributes in the returned string.

#Add a method increase_salary(percent) in the Employee class that increases the salary by a given percentage.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def get_details(self):
        print(self.name)
        print(self.salary)

    def get_salary(self):
        return self.salary
    
    def increase_salary(self,percent):
        self.salary += self.salary *(percent/100)
        print(self.salary)
    
    
        
class Manager(Employee):
    def __int__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def get_details(self):
        return self.department
    

class Developer(Employee):
    def __int__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language
    def get_details(self):
        return self.programming_language
    
e=Employee("manasa",20000)
print(e.get_details())
e.increase_salary(5)

m=Manager("sushi",30000,"IT")
print(m.get_details())
m.increase_salary(5)

d=Developer("sireesha",40000,"python")
print(d.get_details())
d.increase_salary(5)
print("____________________________________")

#5.Create an abstract class Media with an abstract method play(). Then create the following subclasses:

#Audio, which plays a .mp3 file.
#Video, which plays a .mp4 file.
#LiveStream, which plays a live stream.
#Implement a function start_media(media) that takes an object of type Media and calls its play() method. Demonstrate polymorphism by passing different types of media to this function.
from abc import ABC, abstractmethod

class Media(ABC):
    @abstractmethod
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("playing mp3 (.mp3)")


class Video(Media):
    def play(self):
        print("Playing mp4 (.mp4)")


class LiveStream(Media):
    def play(self):
        print("Playing live stream")


def start_media(media):
    media.play()


a = Audio()
v = Video()
ls = LiveStream()

start_media(a)      
start_media(v)      
start_media(ls)   
print("_________________________")

#6.Create an abstract class LibraryItem with abstract methods borrow() and return_item(). Then create two subclasses:

#Book, with attributes title, author, and num_copies.
#DVD, with attributes title, director, and duration.
#Implement a function borrow_item(item) that borrows the library item and decreases the number of available copies (for books) or marks the DVD as borrowed.

from abc import ABC, abstractmethod
class LibraryItem(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def borrow(self):
        if self.num_copies > 0:
            self.num_copies -= 1
            print(self.title)
            print(self.num_copies)
        else:
            print(self.title)

    def return_item(self):
        self.num_copies += 1
        print(self.title)
        print(self.num_copies)


class DVD(LibraryItem):
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title)
        else:
            print(self.title)

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title)
        else:
            print(self.title)


def borrow_item(item):
    item.borrow()


book = Book("apptitude", "dr.aggarwal", 2)
dvd = DVD("abc", "maths", "2h")

borrow_item(book)   
borrow_item(dvd)    
borrow_item(dvd)    
book.return_item()  
dvd.return_item()   

