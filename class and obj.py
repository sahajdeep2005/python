class myclass:
 x=32
print(myclass)
p1=myclass()
print(p1.x)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("sahaj",16)
print(p1.name)
print(p1.age)
# class project 2


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
        print(self.age)
p1 = Person("sahaj", 36)
p1.myfunc()



