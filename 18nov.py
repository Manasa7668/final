class Myntra:
    def display(self,url):
         self.url = url #public variable
         print(self.url)
    def login(self,username,password):
         self.__username=username #private variable
         self.__password=password
         print("username is:",self.__username)
         print("password is:",self.__password)
    def cart(self,carttt):
         self._carttt=carttt #protected variable
         print("cart_item is:",self._carttt)
m=Myntra()
m.display("htps://www.myntra.com")
m.login("manasa","12man")
m.cart("phone")
print("____________________________________")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary 
    
    def showsalary(self):
        return f"{self.name}'s salary is ${self.__salary}"
    
    def display(self, amount):
        if amount > 0:
            self.__salary += amount
            print(amount)
        else:
            print("Invalid raise amount.")

e = Employee("manasa", 20000)
print(e.showsalary())  
e.display(5000)      
print(e.showsalary())  


