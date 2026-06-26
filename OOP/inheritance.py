# class Employee:
#     company = "IIT"
#     def __init__(self , name):
#         self.name = name
#     def show(self):
#         print(f"The Employee name is : {self.name} ")
        
# class Programmer(Employee):
#     company = "IIT Info-tech"
#     def __init__(self , name , language):
#         super().__init__(name)
#         self.language = language
#     def showLanguage(self):
#         print(f"The {self.name} is good in : {self.language}")
        
        
# b = Programmer("Ali" , "Python")

# b.show()
# b.showLanguage()

class Person:
    def __init__(self, name):
        self._name = name   # private variable

    @property
    def name(self):   # getter
        return self._name

    @name.setter
    def name(self, value):   # setter
        if len(value) < 3:
            print("Name too short")
        else:
            self._name = value

p = Person("Ali")

print(p.name)   # getter
p.name = "Ah"   # setter (invalid)
p.name = "Ahmed"

print(p.name)