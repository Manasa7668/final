#1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!"

#method1

def greet(name):

    return name

print("Hello,",greet("milo!"))#output:Hello,milo!







#method2

def greet(name):

    print(f'hello,{name}!')

greet("manasa")

print("_________________________________")



#Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers.



def add_numbers(x,y):

    sum=x+y

    return sum

print(add_numbers(5,10))

print(add_numbers(190,10))

print(add_numbers(5,1880))

print("_________________________________")



#3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.



def is_even(number):

    return number%2 == 0

       



print(is_even(4))

print(is_even(5))

print(is_even(47))

print(is_even(24))

print("_____________________________________")





#Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).



def factorial(n):

   

    if n==1:

     return n  

    else:

        return n*factorial(n-1)

print(factorial(5))

print("____________________________________________")



#Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.

#method1

def find_max(numbers):

    return max(numbers)

numbers=(2,7,87)

print("max number is:",find_max(numbers))



#method2

def find_max(a,b,c):

    return max(a,b,c)

print("max number is:",find_max(6,99,789))

print("_______________________________________________")



#6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

def count_vowels(str):

    vowels = "aeiou"

    count  = 0

    for char in str:

        if char in vowels:

            count += 1

    return count

   

print(count_vowels("python is easy to learning"))

print(count_vowels("string as left operand"))



print("________________________________________________")





#7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.



def is_prime(number):

    if number <= 1:

        return False

    for i in range(2, int(number**0.5) + 1):

        if number % i == 0:

            return False

    return True





print(is_prime(3))

print(is_prime(9))

print(is_prime(1))

print(is_prime(2))

print("_______________________________________________")



#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).

def recursive_sum(n):

    if n==1:

        return 1

    else:

        return n + recursive_sum(n - 1)

   

print(recursive_sum(5))

print(recursive_sum(7))

print("_________________________________")



#9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.

def calculator(a,b,operator):

    if operator == "+":

        return a+b

    elif operator == "-":

        return a-b

    elif operator == "*":

        return a*b

    elif operator == "/":

        return a/b

    else:

        return "invalid operator"

print(calculator(2,3,"+"))

print(calculator(2,3,"-"))    

print(calculator(2,3,"*"))    

print(calculator(2,3,"/"))    

print(calculator(2,3,""))  

print("_________________________")



#10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.

def find_common_elements(l1,l2):

    return list(set(l1)&set(l2))

print(find_common_elements([1,2,3,4,6,9],[2,3,5,9,0,23]))

print(find_common_elements(["apple","ball","cat"],["apple","dog","egg"]))



#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.

def reverse_string(str):

    return str[::-1]

print(reverse_string("hello world"))

print("_____________________________")



#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.

def sort_dict_by_value(input):

       return sorted(input.items(), key=lambda item: item[1])



s={'a':5,'b':9,'c':4}

print(sort_dict_by_value(s))







   















































