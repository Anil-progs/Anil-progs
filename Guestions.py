# 1 first question

# create a class called person with attributes name and age. Create an object of the class and print its attributes.abs
class person:
    def __init__(self, name, age, l_name, f_name):
        self.name = name
        self.age = age
        self.L_name = l_name
        self.f_name = f_name
        self.jap = "Teacher"  # defult value

    # this show that those things you want to use in your method if it be attributes you
    # need to initionalize it.
    def persinality(self):
        print(f"he is {self.name},that is good for our jap")
        print(f"last name of him is {self.L_name},his father name is {self.f_name}")
        print(f"he is {self.age}  years old and his jap is {self.jap}")

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # 2 sencond question

    # Add a method called greet to the person class that print a greeting massage including the person's name.
    def greet(self, person):
        answer = f"Hi Mr {self.name}, good morning!,  good morning too Mr {person}"
        print(answer)
        return answer


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# from Class and Object import person
answer = person("Ahmad", 23, "Ahmady", "Khan")
answer.persinality()  # method can print without using from motule print()

print(answer.age)  # to print the atterbutes we need to print() it
d = answer.name
print(d)
print("---------------------------------------------------------------------------------------------------")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
answer.greet("Mohammad")  # because we take argument in here , it has parameter in greet method
# because we use return in method
print(answer.greet("Mohammad"))

print("---------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# 3 third question

# Create a class called car with attributes make, model, and year, include a method to print out the car's details.abs
class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.time = year
        self.followers = 0  # defult value
        self.following = 0

    def car_details(self):
        print(f"The car made in {self.make},which has model of {self.model} it is made in {self.time}")
        return self.followers + 1
        return self.following + 1


Driver = car("China", "pp412", 2005)
print(Driver.make)
print(Driver.followers)

c = Driver.car_details()
print(c)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
print("--------------------------------------------------------------------------------------------------")


# 4 fourt question

# Create a class circle with a methods to compute the area. Initialize the class with radius
# A=pi*r**2
class Circle:
    def __init__(self, radius):
        self.r = radius
        self.pi = 3.14  # defult value

    def Area(self):
        compute = self.pi * (self.r) ** 2
        return compute


area = Circle(
    5)  # when you put parameter internal of __init__ you need to put argument internal of class that you put in object
print(area.Area())


# \\\\\\\\\\\\\\\\\\\
# second way to find the area of circle
class Circle:
    def __init__(self):
        self.pi = 3.14  # defult value

    def Area(self, radius):
        compute = self.pi * (radius) ** 2
        print(compute)


area = Circle()
area.Area(
    6)  # when you put parameter internal of method of class you need to put argument internal of the place you put object.Nme("sdkjhfkh")
# Use defult value instade of parameter in __init__
print("--------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 5 Fifth question

# Create a class rectangle with methods to compute the area and perimeter, initialzw the class with the length and width.abs
# 5 Fifth question
class rectangle:
    def __init__(self, length, weight):
        self.l = length
        self.w = weight

    def Area(self):
        compute = self.l * self.w
        return compute


area = rectangle(5, 6)
print(area.Area())


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
class rectangle:
    def __init__(self):
        pass

    def Area(self, weight, length):
        compute = weight * length
        print(compute)


area = rectangle()
area.Area(5, 7)


# 11 elevan question

# Create a class Account with private attrributes balance,provide public methods to deposit and withdraw money.

class Account:
    def __init__(self, balance):
        self.__balance = balance  # privite attribute

    def _deposite(self, money):  # protect method
        return f"Past balance {self.__balance}, Deposite money {money}, New money {self.__balance + money}"

    def __withdraw(self, money):  # privite method
        return f"Past balance {self.__balance}, Deposite money {money}, New money {self.__balance - money}"

    def display_withdraw(self):  # way to accuss to the privite method and privite attribute
        return self.__withdraw(87665)
        self.__balance


s = Account(8976545)
print(s._deposite(97786))
print(s.display_withdraw())  # way to accuss the privite method
print(s._Account__balance)  # way to accuss the privite attribute

print(
    "----------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# extra  example
class father:
    def __init__(self, name, l_name, age):
        self.name = name
        self._l_name = l_name
        self.__age = age

    def display(self):
        return f" The name of him is {self.name}, the l_last name of him is {self._l_name},the age of him is {self.__age}"

    def __play(self):
        return f" The name of him is {self.name}, the l_last name of him is {self._l_name},the age of him is {self.__age}"

    def display_play(self):
        return self.__play()
        self.__age


s = father("Ahmad", "Khan", 34)
print(s.display_play())
print(s._father__play)
# print(s._father__age)     this will take answer but only it will show the oject address of
print(
    "---------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Account:
    def __init__(self):
        self.balance = 500000

    def deposit(self, money):
        return f" Past baget {self.balance}, deposit money {money}, New paget {self.balance + money}"

    def withdraw(self, money):
        if money > self.balance:
            print("Sory you don not have enough money in your account")
        else:
            return f" Past baget {self.balance},Withdraw money {money}, New paget {self.balance - money}"


account = Account()
aset = account.deposit(60432)
print(aset)
print()
account = Account()
aset = account.withdraw(19034)
print(aset)
print(
    "-----------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 12 towelve question

# Create a class Book with private attributes title,author, and pages. Provide public methods to get and set these attributes.
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __get_book(self):
        print(f" Title= {self.__title}, author= {self.__author}, pages= {self.__pages}")

    def __set_book(self, title, author, pages):
        print(f"Title= {title}, author= {author}, pages= {pages} ")

    def show_play(self):
        return self.__get_book()

    def play(self):
        return self.__set_book("Horry patter", "Jack", 78)


show = Book("Kingdam", "Mohammad", 100)
print(show.show_play())  # privite method

print(show._Book__title)
print(show._Book__pages)  # privite attributs
print(show._Book__author)

print(show.play())  # privite method
print(
    "-----------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 13 thirden question

# Create a class of laptop with privite attribute brand, model, and price. privite a method to apply a discount
# and a method to deposit,withdraw, and check the balance
class Laptop:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__price = 56789

    def __deposit(self, balance):
        return f"Past balance={balance},New balance: {balance + self.__price},Brand :{self.__brand},model :{self.__model}"

    def __withdraw(self, balance):
        return f"Past balance={balance},New balance: {balance - self.__price},Brand :{self.__brand},model :{self.__model}"

    def Seller(self, balance):
        if balance > self.__price:
            return self.__deposit(654321)
        else:
            print("Sorry you do not have enough moeny")

    def Buyer(self, balance):
        if balance > self.__price:
            return self.__withdraw(5432)
        else:
            print("Sorry you do not have enough money")


seller = Laptop("HHP", "B24tp")
print(seller.Seller(320))

buyer = Laptop("HHP", "B@$tp")
print(buyer.Buyer(675432))
print(
    "---------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 14 fourthy question

# Create a class BankAccount with privide attributes account_number and balance. Privite mehtod to deposit, withdraw and check the balance.abs
class BanckAccount:
    def __init__(self, balance):
        self.__account_number = 123
        self.__balance = balance

    def __deposit(self, money):
        n = int(input("Enter your account number: "))
        if n == 123:
            return f" Past balance={self.__balance}, New balance ={self.__balance + money}"
        else:
            print("Sorry range account number")

    def __withdraw(self, money):
        n = int(input("Enter the account_number"))
        if n == 123:
            return f" Past balance ={self.__balance}, New balance = {self.__balance - money}"
        else:
            print("Sorry your password is incorrect")

    def show_deposit(self):
        return self.__deposit(6788998)

    def show_widthraw(self, money):
        if money > self.__balance:
            print("You do not have enough money in your account")
        else:
            return self.__withdraw(6788998)


your_bank = BanckAccount(234567)
print(your_bank.show_deposit())

your_bank_w = BanckAccount(234567)
print(your_bank_w.show_widthraw(67))

print(
    "----------------------------------------------------------------------------------------------------------------------------------------")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 15 fifth question

# Create a class student with privite attributes name, grade, and age. provide methods to get and set these attributes and a method to display
# the student's details.abs
# the examples from attributes get more we will Abstraction that Amshallah.
from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    @abstractmethod
    def get_info(self):
        return f"Name={self.name},Grade= {self.grade},age= {self.age}"


class S_s(Student):
    def __init__(self):
        super().__init__("Ahmad", "A", 23)

    def get_info(self):
        return f" Name of student:{self.name},Grade : {self.grade},age : {self.age}"


c = S_s()
print(c.get_info())


# 21 thony one quwstion

# Create a class fileManager with methods to read from and write to a file.abs
class FileManager:
    def __init__(self, n):
        self.n = n

    def create_file(self):
        file = open(f"{self.n}", "x")
        return file

    def read(self):
        file = open(f"{self.n}", "r")
        return file

    def write(self):
        file = open(f"{self.n}", "w")
        file.write(
            "This the way that we can learn the coding I know it is easy  but it will become easy the time that we try hard")
        return file

    def appends(self):
        file = open(f"{self.n}", "a")
        file.append("PPP this is the code that you open the log of my wallet that can proffe you can play with it")
        return file


make = FileManager("FileManager")
# print(make.create_file())
print(make.read())
print(make.write())
print(make.appends())

print(
    "----------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 22 thony two question

# Create a class Log with methods to write error massages to a log file.abs
class Log:
    def __init__(self, n):
        self.n = n

    def write(self):
        file = open(f"{self.n}", "w")
        file.write("Error massage")
        return file


log = Log("Log file")
print(log.write())

print(
    "------------------------------------------------------------------------------------------------------------------------------------")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 24 thony four question

# Create a class database that connect to a database and provides methods to execute queries, handle exception if the connection fails.

from abc import ABC, abstractmethod


class Student(ABC):
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    @abstractmethod
    def get_info(self):
        return f"Name={self.name},Grade= {self, grade},age= {self.age}"


class S_s(Student):
    def __init__(self):
        pass

    def get_info(self):
        return f" Name of student:{self.name},Grade : {self.grade},age : {self.age}"


c = S_s
print(c.get_info())


# 6 question

# Create a base class Animal with a method speak. Create two derived classes Dog and Cat that override the speak method
class Animal:
    def __init__(self, sound, eat):
        self.sound = sound
        self.eat = eat

    def speak(self):
        return f"The Animal {self.sound} is not good in here, they {self.eat} what?"


inf = Animal("sound", "eat")
print(inf.speak())

print("-----------------------------")


class Dog(Animal):
    def speak(self):
        return f" The Dog is {self.sound},because it see the {self.eat}"


inf_d = Dog("Barking", "Meit")
print(inf_d.speak())

print("---------------------------------")


class Cat(Animal):
    def speak(self):
        return f"The Cat is {self.sound},due to this that it just see the {self.eat}"


inf_c = Cat("Mow,Mow", "Fish")
print(inf_c.speak())
print(
    "---------------------------------------------------------------------------------------------------------------------------")
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 7 seven question
# Create a base class shape with a method area. Create drived class square and triangle that implement the area method.abs
n = int(input("Enter the wieght:"))
m = int(input("Enter the lenght:"))


class Shape:
    def __init__(self, weight, lenght):
        self.w = weight
        self.l = lenght

    def area(self):
        return f"the weight= {self.w}, the lenght= {self.l}"


Area = Shape(n, m)
print(Area.area())


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\
class Triangle(Shape):
    def area(self):
        return self.w * self.l


Area_t = Triangle(n, m)
print(f"The Area of Triangle: {Area_t.area()}")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\
class Square(Shape):
    def area(self):
        print(f"The answer of square is {self.w * self.l}")


Area = Square(n, m)
Area.area()
print(
    "----------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 8 Eight question

# Create a class Employee with attributes name and salary, Create a derived class Manager with an additional attribute department.
def password(n):
    if n == 123:
        class Employee:
            def __init__(self):
                self.name = "Ahmad"
                self.salary = 100000

            def inf(self, age):
                return f" The employee is {self.name}, he is {age}, have salary {self.salary}"

        inf_e = Employee()
        print(inf_e.inf(25))

        class Manager(Employee):
            def __init__(self):
                self.age = 25
                self.department = "Engineering of PPT"
                super().__init__()

            def inf_d(self):
                return f" name:{self.name}, age:{self.age}, salary:{self.salary}, department:{self.department}"

        inf_m = Manager()
        print(inf_m.inf_d())


n = int(input("Enter your ID number:"))
password(n)
print(
    "----------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 9 nine question

# Create a base class vehicle with a method drive, Create drived classess Bike and Truck that override the drive method.abs
class vehicle:
    def __init__(self, v, t):
        self.v = v
        self.t = t
        self.name = "Marex"

    def drive(self, model):
        return f"The name of the car is {self.name},model of that {model},The spead is v={self.v / self.t}"


inf_car = vehicle(137, 45)
print(inf_car.drive("XPAR"))


# \\\\\\\\\\\\\\\\\\\\\\\\\\\

class Bike(vehicle):
    def drive(self, made):
        print(f" The name of bike is BIkeww,made of {made},The spead of it is v={self.v / self.t}")


inf_bike = Bike(341, 70)
inf_bike.drive("China")


class Truck(vehicle):
    def __init__(self):
        self.usage = "To carry something"

    def drive(self, made):
        print(f"  It is use  {self.usage},it made of {made},The spead of it is v={self.v / self.t}")


inf_bike = Bike(107, 37)
inf_bike.drive("Iran")
print(
    "--------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 10 ten question

# create a base class bird with a method fly. Create derived classes Eagle and penguin. override the fly mehtod in penguin to indicate that penguins cannot fly.abs
class bird:
    def __init__(self, fly, speed):
        self.fly_bird = fly
        self.speed = speed

    def fly(self):
        print(f"one of the jap of birds is {self.fly},and they have speed {self.speed}")


s = bird("fly", "speed")
s.fly()


class Eagle(bird):
    def fly(self):
        print(f"The eagle can {self.fly},and have the speed of {self.speed}")


d = Eagle("fly", 340)
d.fly()


class Panguin(bird):
    def fly(self):
        print(f"The panguin can not {self.fly},can have the speed of {self.speed}")


g = Panguin("fly", 56)
g.fly()

# 16 sixten qustion
# Create a class library with attributes name and boooks(a list of boook object).provide to add and remove book.abs
books = ["Horry patter:2004", "PPT:1090", "Binary:2020"]


class Library:
    def __init__(self, name, books):
        self.name = name
        self.books = books

    def add(self, b):
        return f" The the library of {self.name} has the books like {self.books.append(b)}"

    def remove(self):
        print(books)
        e = input("YOU want to remove which of it :")
        if e == books[0]:
            print(books[1:])
        elif e == books[1]:
            print(f"The book by the name of {books[1]} is remove.")
        elif e == books[2]:
            print(f"The book by the name of {books[2]} is remove.")
        else:
            print("these books is not exit")


c = Library("kabul", books)
print(c.add("PTPT"))
print(books)

b = Library("Kabul", books)
print(b.remove())
print(
    "-------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 17 sventhy question

# Create a class school with attributes name and students (a list of student object).provide methods to add and remove student

# student=["Ahmad","Mohammad","Ali","getter"]
class School:
    def __init__(self, name):
        self.name = name
        self.student = ["Ahmad", "Mohammad", "Ali", "getter"]

    def add(self, args):
        return f"The school name is {self.name}, and student are {self.student.append(args)}"

    def remove(self):
        e = input("Which of that you want to remove  ")
        if e == self.student[0]:
            print(f"you remove {self.student[0]}")
        elif e == self.student[1]:
            print(f"you remove {self.student[1]}")
        elif e == self.student[2]:
            print(f"You remove {self.student[2]}")


t = School("Char qalha chardhi")
print(t.add("hgdjs"))
print(t.student)

p = School("Char qalha chardhi")
print(p.remove())
print(
    "--------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 18 eighten question

# Create a class team with attributes name and members (a list of person object). provide methods to add and remove member.abs

class Team:
    def __init__(self, name):
        self.name = name
        self.member = ["Ahmad", "Mohammad", "Ali", "getter"]

    def add(self, args):
        return f"The team name is {self.name}, and member are {self.member.append(args)}"

    def remove(self):
        e = input("Which of that you want to remove  ")
        if e == self.member[0]:
            print(f"you remove {self.member[0]}")
        elif e == self.member[1]:
            print(f"you remove {self.member[1]}")
        elif e == self.member[2]:
            print(f"You remove {self.member[2]}")


t = Team("Char qalha chardhi")
print(t.add("hgdjs"))
print(t.member)

p = Team("Char qalha chardhi")
print(p.remove())
print(
    "--------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 19 nineteen question

class Campany:
    def __init__(self, name):
        self.name = name
        self.employees = ["Ahmad", "Mohammad", "Ali", "getter"]

    def add(self, args):
        return f"The school name is {self.name}, and student are {self.employees.append(args)}"

    def remove(self):
        e = input("Which of that you want to remove  ")
        if e == self.employees[0]:
            print(f"you remove {self.employees[0]}")
        elif e == self.employees[1]:
            print(f"you remove {self.employees[1]}")
        elif e == self.employees[2]:
            print(f"You remove {self.employees[2]}")


t = Campany("Char qalha chardhi")
print(t.add("hgdjs"))
print(t.employees)

p = Campany("Char qalha chardhi")
print(p.remove())

print(
    "-------------------------------------------------------------------------------------------------------------------------------------")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# 20 thowny question

# Create a class zoo with attributes name and animal (a list of Animal object) Provide methods to add and remove animal.abs

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = ["Tiger", "lion", "Dog", "Cat"]

    def add(self, args):
        return f"The school name is {self.name}, and student are {self.animals.append(args)}"

    def remove(self):
        e = input("Which of that you want to remove  ")
        if e == self.animals[0]:
            print(f"you remove {self.animals[0]}")
        elif e == self.animals[1]:
            print(f"you remove {self.animals[1]}")
        elif e == self.animals[2]:
            print(f"You remove {self.animals[2]}")


t = Zoo("Kabul zooo")
print(t.add("hgdjs"))
print(t.animals)

p = Zoo("Kabul zoo")
print(p.remove())