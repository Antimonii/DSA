# OOPs

- We can create a class like so

```python
class Item:
    pass
```

- In Python the **init**() method is called the constructor and is always called when an object is created.

```python
def __init__(self):
    # body of the constructor
```

- Functions inside a class is called a **method**

```python
def calculate_total_price(self,x,y):  
        return x*y
```

here the function calcualate_total_price is the method 

- We can assign attributes dynamically like so:

```python
class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
    def calculate_total_price(self,x,y):  
        return x*y

item1 = Item('Phone',400,7) 

item2 = Item('Laptop',4000,3) 

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
```

Instead of doing :

```python
class Item:
    def __init__(self):
    def calculate_total_price(self,x,y):  
        return x*y

item1 = Item() 
item1.name = 'Phone'
item1.price = 400
item1.quantity = 7 

item2 = Item() 
item2.name = 'Laptop'
item2.price = 100
item2.quantity = 3 

```

- While defining a class we can also set an attributes default value as so:
    
    here we have set quantities  default value to 0 so even if we don't enter a value there it is fine 
    

```python
class Item:
    def __init__(self,name,price,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity 
```

The datatype can also be set from the method for each attribute

```python
class Item:
    def __init__(self,name:str,price:float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity 
```

Function **assert** can be used to validate our conditions for each attribute

```python
class Item:
    def __init__(self,name:str,price:float,quantity=0):
        
        assert price >= 0 
        assert quantity >= 0 
        
        self.name = name
        self.price = price
        self.quantity = quantity 
    def calculate_total_price(self):  
        return self.price * self.quantity
```

The method **__dict__** is used to obtain all the attributes in a dictionary format

```python
print(Item.__dict__)
print(item1.__dict__)

#OUTPUT
{'__module__': '__main__', '__init__': <function Item.__init__ at 0x000002AD81D411C0>, 'calculate_total_price': <function Item.calculate_total_price at 0x000002AD81D413A0>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
{'name': 'Phone', 'price': 400, 'quantity': 7}
```

The method __**repr__** can be used to display objects:

```python
def __repr__(self) :
        return f"Item('{self.name}',{self.price},{self.quantity})"
```

# **CLASSES AND INHERITENCE**

```python
class Employee():
    pass

emp1 = Employee() #an instance of the class employee
emp2 = Employee() #another instance of the class employee  

print(emp1)
print(emp2)
```

Code to return the fist and last name of all employees using a method

```python
class Employee():
    
    def __init__(self,first,last,pay):
        self.first = first #instance variable
        self.last = last #instance variable
        self.pay = pay #instance variable
        self.email = self.first + self.last + '@gmial.com' #instance variable

    def give_full_name(self):
         return '{} {}' .format(self.first,self.last)
        
emp1 = Employee('Pore', 'Man' , 4560) #an instance of the class employee
emp2 = Employee('Master', 'Shifu',5648) #another instance of the class employee  

print(emp1.give_full_name())
print(emp2.give_full_name())
```

```python
print(emp1.give_full_name())
print(Employee.give_full_name(emp1)) 
#both of these are the exact same
```

In methods we pass self as a parameter as when we try to print something from the class without it gives us an error as in the below case emp1 gets passed as a parameter and we get an error as we made the function/method take 0 arguments but was given 1  

```python
print(emp1.give_full_name())
```

# CLASS VARIABLES

Class variables are those variables that are shared by all instances of a class. 

In the below snippet we used a class variable that it raise_amount 

```python
class Employee():

    raise_amunt = 1.06 #class variable
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmial.com' 

    def give_full_name(self):
         return '{} {}' .format(self.first,self.last)
    
    def give_raise(self):
        self.pay = (self.pay * self.raise_amunt)
        
emp1 = Employee('Pore', 'Man' , 4560) #an instance of the class employee
emp2 = Employee('Master', 'Shifu',5648) #another instance of the class employee  

print(emp1.pay)
emp1.give_raise()
print(emp1.pay)

# print(emp1.give_full_name())
# print(Employee.give_full_name(emp1)) #both of these are the exact same
```

In another special case we can use the class variable and check updation accordingly

```python
class Employee():

    raise_amount = 1.06 
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmial.com' 

    def give_full_name(self):
         return '{} {}' .format(self.first,self.last)
    
    def give_raise(self):
        self.pay = (self.pay * self.raise_amount)
        
emp1 = Employee('Pore', 'Man' , 4560) #an instance of the class employee
emp2 = Employee('Master', 'Shifu',5648) #another instance of the class employee  

emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.pay)
print(emp1.raise_amount)
print(emp2.pay)
print(emp2.raise_amount)

# print(emp1.give_full_name())
# print(Employee.give_full_name(emp1)) #both of these are the exact same

1.06
4560
1.05
5648
1.06
```

In this case we see that the raise amount for every instance in the class remains the **same 1.06** but in the case of emp1 it changes as it was updated

instead of using .self in some places where we want global value same we use .(class_name) to keep things uniform 

# CLASS METHODS AND STATIC METHODS

To create a class method or a static method we use 

```python
@classmethod
@staticmethod
```

This is an exmaple of a class method where we set the raise amount 

```python
@classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

Employee.set_raise_amount(1.08)
```

Another example of class method where we parse string 

```python
@classmethod
    def get_emp_detials(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

emp_str1 = 'Poda-Myre-1500'
new_emp1 = Employee.get_emp_detials(emp_str1)
print(new_emp1.first)
print(new_emp1.last)
print(new_emp1.pay)
```

Now lets take a look at static methods, this is a special type of method where we do not pass anything automatically unlike class that passes cls and regular methods that have self

This is a static method we created to check if an inputted date is weekday or not

```python
@staticmethod 
    def check_weekday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True
import datetime
day_check = datetime.date(2020, 7 , 4)
print(Employee.check_weekday(day_check)) 

```

# INHERITENCE

To create a subclass we create a class the same way and add parenthesis and insert the class we want to inherit from in it 

Here developer is a subclass which inherits from Employee

```python
class Employee():
class Developer(Employee):
```

Here we created a subclass called Developer which takes inherits instance variables from the parent and uses super()

```python
class Developer(Employee):

    raise_amount = 1.10
    def __init__(self,first,last,pay,p_lang):
        super().__init__(first,last,pay) #both do same job of calling parent __init__ method
        #Employee.__init__(first,last,pay)
        self.p_lang = p_lang

```

There are two functions we can use 

`isinstance` - This checks if an object is an instance of a class

`issubclass` - This checks if a class is subclass of another class

# SPECIAL METHODS

There are several speical methods in python and here are some of them 

```python
def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

def __str__(self):
    return '{} - {}'.format(self.fullname(), self.email)

def __add__(self, other):
    return self.pay + other.pay

def __len__(self):
    return len(self.fullname())
```

The __repr__() method **returns a more information-rich, or official, string representation of an object**

# PROPERTY DECORATOR

# CODE SNIPPERT

```python
class Employee():

    raise_amount = 1.06 
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmial.com' 

    def give_full_name(self):
         return '{} {}' .format(self.first,self.last)
    
    def give_raise(self):
        self.pay = (self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def get_emp_detials(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    

    @staticmethod 
    def check_weekday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True
import datetime
day_check = datetime.date(2020, 7 , 4)
print(Employee.check_weekday(day_check)) 

emp_str1 = 'Poda-Myre-1500'
new_emp1 = Employee.get_emp_detials(emp_str1)
print(new_emp1.first)
print(new_emp1.last)
print(new_emp1.pay)

Employee.set_raise_amount(1.08)

emp1 = Employee('Pore', 'Man' , 4560) #an instance of the class employee
emp2 = Employee('Master', 'Shifu',5648) #another instance of the class employee  

print(Employee.raise_amount)
print(emp1.pay)
print(emp1.raise_amount)
print(emp2.pay)
print(emp2.raise_amount)

# print(emp1.give_full_name())
# print(Employee.give_full_name(emp1)) #both of these are the exact same

```

```python
class Employee():

    raise_amount = 1.06 
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + self.last + '@gmial.com' 

    def give_full_name(self):
         return '{} {}' .format(self.first,self.last)
    
    def give_raise(self):
        self.pay = (self.pay * self.raise_amount)

class Developer(Employee):

    raise_amount = 1.10
    def __init__(self,first,last,pay,p_lang):
        super().__init__(first,last,pay) #both do same job of calling parent __init__ method
        #Employee.__init__(first,last,pay)
        self.p_lang = p_lang

class Manager(Employee):

    def __init__(self, first, last, pay,dept):
        super().__init__(first, last, pay)
        self.dept = dept 
    
dev1 = Developer('Pore', 'Man' , 4560, 'C++') #an instance of the class employee
dev2 = Developer('Master', 'Shifu',5648,'Ruby') #another instance of the class employee  
man1 = Manager('Myre',"Randi",648787,'Goomy')
#print(help(Developer))

print(dev1.__repr__)
print(dev1.email)
print(man1.dept)

def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

def __str__(self):
    return '{} - {}'.format(self.fullname(), self.email)

def __add__(self, other):
    return self.pay + other.pay

def __len__(self):
    return len(self.fullname())
```