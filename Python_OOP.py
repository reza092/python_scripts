#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:04:13 2020

@author: rezaulkarim
"""

## IN PYTHON:
# CLASS CONSISTS OF TWO PARTS: INSTANTIATION(ATTRIBUTE BINDING, DATA ATTRIBUTES)
                                # METHOD FUNCTION(S), PROCEDURAL ATTRIBUTES (behavior,operations,methods)

# INSTANTIATION AND ATTRIBUTES BINDING

# class NewClass():
#     def __init__(self,attr1,attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2
#         #when the creation of an instance is invoked, this self will bind
#         #with the instance itself.
        
#     def new_method(self):
#         #do function
        
class Coordinate(object):
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
    def distance(self, other):# method/procedure always refer to the instance, thus self
                            # a second parameter, other, to method
                            # IS OTHER AN OBJECT?
        x_diff_seq = (self.x - other.x)
        y_diff_seq = (self.y - other.y)
        return (x_diff_seq + y_diff_seq)**0.5 # dot notation
        # dot notation is required to return the value of the method
        # this method is same as function but under Class
    
    # what if I print(c)?
    # special method, called string method
    def __str__ (self):
        #by definition, python has string method built in for calling
        # but we need to tell what that do!
        return ("<" + str(self.x) + "," + str(self.y) + ">")
    
    # another special method: substraction
    def __sub__ (self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    # SPECIAL method __eq__
    def __eq__ (self, other):
        assert type(other) == type(self), "Two data types are not the same"
        return (self.x, self.y)==(other.x,other.y)
    
    # SPECIAL __repr__ 
    def __repr__(self):
        r#eturn ("Coordinate"+str(self.x,self.y))
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'
        
    
c = Coordinate(3,4)
# it created new instance c with Coordinate frame
origin = Coordinate(0, 0)
#python automatically provide the self inside paren

## print(c.x) # get the value of c = frame> binding attribute x

## METHOD calling
print(c.distance(origin))#when c(=Coordinate class) was called,
#it initiated the Coordinate(3,4) frame
#distance calling automatically took the (3,4) via self
# the above is equivalent to
print(Coordinate.distance(c,origin))

# calling isinstance built-in method
print (isinstance(c,Coordinate))

print(c)

foo = c - origin # built-in method substraction has been redefined for the class
print(foo)

## ALIASING >> NEW

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
    def __str__(self):
        return ("Clock time "+ self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
boston_clock.time # ALIASING: boston_clock and paris_clock are same object
#with two names
print(Clock)



## CLASS INHERITENCE
    # POWER of OOP : bundle together some sharable attributes
    # create OWN CLASSES of objects on top of python's built in ones
    # bundling together provides abstraction without thinking much
    # powerful to make heirerchical class: base method > aditional method
    # There are differences between defining/using a class and implementing one
        # CLASS is the type itself
        # class defines data and methods common across all instances
        # Using same class, different objects with different value can be created 

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None #can also define attr that I am going to use
        
#myanimal = Animal(3)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name # getter should be used outside of class to access data attributes
    def set_age(self, newage):
        self.age = newage # getter should be used outside of class to set data attributes
    def set_name(self, newname=""):# newname set to a DEFAULT VALUE
        self.name = newname
    def __str__(self):
        return "Class animal:"+str(self.name)+":"+str(self.age)
        
# HIERARCHIES sharing the properties of ANIMAL class (parent)
    # sub-class can have methods with same name as superclass
    # also can have method name same with other sub-class
    # method calling will look for the method in sub-class
        # if doesnot find then it will look in class
        # if still can't find then it will throw up error
        # thus can package in layers
# class Rabbit(Animal):# SUB-CLASS: added attr or changed attr
#     def speak(self):
#         print('mip!')
#     def __str__(self):
#         return "Rabbit " +str(self.name) +" of age " +str(self.age) +" says mip"
    #peter = Rabbit(5) #peter is a Rabbit instance with Animal class
    #peter.speak() # invokes peter instance inheriting all attributes of Animal class
    
class Cat(Animal):
    def speak(self):
        print('meow!')
    def __str__(self): #over-write the Animal class method for this sub-class
        return "Cat " +str(self.name) +" of age " +str(self.age) +" says meow"
    

# additional sub-class
class Person(Animal):
    def __init__(self,name,age): # EXPLICIT CALLING of __init__ of Animal class
        #Notice: Person subclass has two attributes beyond self
        #You have access to all the methods. You also have access to any class attributes.
        #But you don't have access to data attributes that class will create in its instances 
        #UNTIL you run its __init__ which is why you need to run the super classes' inits.
        Animal.__init__(self,age)
        Animal.set_name(self,name)
        self.friend = [] # adding an attributes not in superclass
    def get_friends(self):
        return self.friends
    def add_friend(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self,other):
        # alternative: diff = self.age-other.age
        diff = self.get_age()-other.get_age()
        if self.age > other.age:
            print(self.name, 'is', diff, 'years older than', other.name)
        else:
            print(self.name,"is",-diff,'years younger than', other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
    
# SPECIAL class of person
class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name,age)
        self.major = major
    def change_major(self,major):
        self.major = major
    def speak(self):
        import random
        r = random.random()
        if r > 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I am hungry')
        else:
            print('I do not know')
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    
# DARA attributes
myAnimal = Animal(5)
myAnimal.age # direct way of accessing the age
myAnimal.get_age() # way to calling method and access the data


## CLASS VARIABLE

class Rabbit(Animal):
    tag = 1 # setting a class variable (could be class attributes)
            # outside of __init__
    
    def __init__(self, age, parent1=None, parent2=None): #making a mate pair
        Animal.__init__(self, age)
        self.age = age
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # subclass variable is utilized to give a 
                                # local unique ID to each new rabbit instance
        Rabbit.tag += 1         # increase value to keep track, data attribute 
                                # associated with the class not instance
        
    def get_rid(self):
        return str(self.rid).zfill(3)   #method on a string to pad the beginning with zeros
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
# peter = Rabbit(2) # peter a 2yr age rabbit
# peter.set_name('Peter') # seting name
# hopsy = Rabbit(3)
# hopsy.set_name('Hopsy')
# cotton = Rabbit(1,peter,hopsy) # cotton peter & hopsy's generation
# cotton.set_name('Cottontail') 
# # printing the peter, hopsy and cotton show that they are Animal class
# # Rabbit doesn't have __str__ mthod, so it will look into Anmal's __str__

# print(cotton.parent1)
# #>Class animal:Peter:2
# print(cotton.get_parent1())
# #>Class animal:Peter:2

# Let's make a new rabbit by mating parent1 and parent2
    def __add__(self, other):   # define + operator between two Rabbit instances
        # return object of same type as this class
        return Rabbit(0,self,other) # Rabbit will init (self, ...)
                                # age = 0, self = parent1, other = parent2
    
    def __eq__(self,other):
        parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
        parents_opposite = self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid
        return parents_same or parents_opposite
        # direct instances can't be compared
        # this is a nice way for comparison
#print (hopsy == cotton)


## BUILDING A CLASS

import datetime
#from datetime import date

class Person(object):
    
    def __init__(self, name):
        """Create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
        
    def get_last_name(self):
        """return self's last name"""
        return self.lastName
    
    def __str__(self):
        """return self's name"""
        return self.name
    
    def set_birthday(self, day,month,year):
        """set self's birthday to birthdate"""
        birthday = datetime.date(year,month,day)
        self.birthday = birthday
        return self.birthday
        
    def get_age(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
        """return True if self's name is lexicographically less than
        other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

##
class MITPerson(Person):
    nextIDnum = 0 # next ID number to assign for each instantiation
    
    def __init__(self,name):
        """Create MITPerson with a name"""
        #self.name = name # rather than binding the attribute (one by one) we can do the following
        Person.__init__(self,name) # initialize Person attribute(s), thus bind name with MITPerson
                                    # birthdate attr, last name attr
        self.idnum = MITPerson.nextIDnum #MITPerson unique ID (attribute)
        MITPerson.nextIDnum += 1
        
    def get_id_num(self):
        return self.idnum
    
    # sorting MIT Persons using their ID num not name
    def __lt__(self,other):
        return self.idnum < other.idnum

    def speak(self, word):
        return (self.get_last_name() + ' says: ' + word)
    
p2 = MITPerson('Harry Porter')
p1 = MITPerson('Robi Zul')
p3 = MITPerson('Taby Cohn')

p2.get_id_num()
p1.get_id_num()
p3.get_id_num()

p2 < p1

p2.speak('PK Pk pk')

person_list = [p1,p2,p3]

for a in person_list:
    print(a)
        
person_list.sort()
print()  

for a in person_list:
    print(a)    

# comparison based on unique ID number
m1 = MITPerson('John')
m2 = MITPerson('Edi')
m3 = Person('John')
m1 < m2
m1 < m3 # AttributeError 'Person' object has no attribute 'idnum'
        # becasue this calls m1.MITPerson.__lt__ method first (ID number)
        # then m3 calls for m3.Person.__lt__ (name)
        # it can't compare int vs string
m3 < m1 # this works, because first the Person.__lt__ is called (name)
        # then it calls, MITPerson method which does not work then goes for parent class method (Person.__lt__)
        # which provides name, thus name vs name are compared
m4 = Person('Delly')
m4 < m1

## Additing another class
#clean up class
class Student(MITPerson):
    pass
# ** SUBSTITUTION PRINCIPLE: Important behaviours of superclass should be supported by all subclasses.
    # Be careful when overriding methods in a subclass!
    
# class UG(MITPerson):
class UG(Student):
    def __init__(self,name,year):
        MITPerson.__init__(self, name)
        self.year = year
    
    def get_class(self):
        return self.year
    
    def speak(self,utterance):
        return MITPerson.speak(self, "Dude, " + utterance)
    
#class Grad(MITPerson):
class Grad(Student):
    pass

#class TransferStudent(MITPerson):
class TransferStudent(Student):
    pass

def is_student(obj):
    #return isinstance(obj,UG) or isinstance(obj, Grad) or isinstance(obj, TransferStudent)
    # A intelligent method could be used to clean up the heirarchy
    return isinstance(obj,Student)

s1 = UG('Matt Damon', 2017)
s2 = UG("Ben Afleck", 2018)
s3 = Grad('Len Di')
s4 = TransferStudent('Rober Dinero')

print(s1)
print(s1.get_class())
print(s1.speak('Where is the class?'))
print(s2.speak('I dont konw'))





