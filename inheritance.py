# single inheri 
class person:
    def fun():
        id=int(input("Enter id:"))
        name=input("Enter name:")
        print(id)
        print(name)

class child(person):
    def fun1():
        year=int(input("Enter current year:"))
        print(year)

ch=child
ch.fun()
ch.fun1()

# multi level 
class parent:
    def fun():
        print("One")

class child1(parent):
    def fun1():
        print("Two")

class child2(child1):
    def fun2():
        print("Three")

ch=child2
ch.fun()
ch.fun1()
ch.fun2()


# multiple_inheritance
class parent:
    def fun(self):
        print("Parent")

class parent2:
    def fun2(self):
        print("Parent1")

class child(parent,parent2):
    def fun3(self):
        print("child")

a=child()
a.fun()
a.fun2()
a.fun3()


# hierarchical inheritance
class parent():
    def fun():
        print("Parent")
class child1(parent):
    def fun1():
        print("Child 1")
class child2(parent):
    def fun2():
        print("Child 2")

a=child1
a.fun()
a.fun1()

a=child2
a.fun()
a.fun2()

#hybrid inheritance
class parent:
    def fun1(self):
        print("Parent")
class child1(parent):
    def fun2(self):
        print("child1")
class child2(parent):
    def fun3(self):
        print("Child 2")
class child3(child1,child2):
    def fun4(self):
        print("Child 3")
        
ch=child3()
ch.fun1()
ch.fun2()
ch.fun3()
ch.fun4()