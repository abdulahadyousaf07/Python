# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("Hey , I am good")
# engine.runAndWait()

# print("OR Truth Table")
# print("False and False is " , False or False)
# print("True and False is " , True or False)
# print("False and True is " , False or True)
# print("True and True is " , True or True)

# print("AND Truth Table")
# print("False and False is " , False and False)
# print("True and False is " , True and False)
# print("False and True is " , False and True)
# print("True and True is " , True and True)

# a = 2
# b = str(a)
# t = type(b)
# print(t)

# a = 2
# b = 3
# c = a + b
# print(c)

# a = input()
# b = type(a)
# print(b)

# a = 20
# b = 10
# if( a > b):
#     print(True)
# else:
#     print(False)

# a = int(input("Enter a Number : "))
# b = int(input("Enter a Number : "))

# c = a+b
# d = c/2

# print(d)

# a = int(input("Enter a Number : "))

# c = a*a

# print(c)

# a = "Ahad"
# b = type(a)

# print(a)
# print(b)

# a = "Abdul Ahad"
# nameshort = a[6:10]
# print(nameshort)

# a = "0123456789"
# b = a[1:7:3]
# print(b)

# a = input("Enter a Name: ")
# print("Good Afternoon ! "+a)
# print(f"Good Afternoon ! {a} ")

# letter = '''Dear <|Name|> You are selected! <|Date|>'''
            
# print(letter.replace("<|Name|>" , "Abdul Ahad").replace("<|Date|>" , "24 Sep 2050"))

# name = "Ahad is good  boy and"
# b = name.replace("  " , "    ")
# print(b)

# letter = "Dear Zaid ,\n\tThis python course is nice.\n Thanks!"
# print(letter)

# friends = ["Apple" , "Mango" , "Banana" , "False" , 00000]
# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])
# print(friends[4])

# print("----- After Changing Values -----")
# friends[0] = "Hamid"
# friends[1] = "Zohaib"
# friends[2] = "Ali"
# friends[3] = "Uzair"
# friends[4] = "Fahad umar"

# print(friends[0])
# print(friends[1])
# print(friends[2])
# print(friends[3])
# print(friends[4])

# numbers = [1 , 4 , 5 , 0 , 8 , 2 , 3 , 9 , 10 , 6 , 7]
# numbers.sort()
# numbers.append(11)
# numbers.remove(0)
# value = numbers.pop(5)
# numbers.insert(11 , 12)


# print(value)
# print(numbers)

# marks = []

# a = int(input("Enter marks"))
# marks.append(a)
# b = int(input("Enter marks"))
# marks.append(b)
# c = int(input("Enter marks"))
# marks.append(c)
# d = int(input("Enter marks"))
# marks.append(d)
# e = int(input("Enter marks"))
# marks.append(e)
# f = int(input("Enter marks"))
# marks.append(f)


# marks.sort()
# print(marks)

# l = [2 , 3 , 4, 5]
# print(sum(l))

# l = (7 , 0 , 8 , 0 , 9)
# value = l.count(0)
# print(value)

# a = {
#     "Harry" : 100,
#     "Ham" : 90,
#     "Joe" : 50,
# }

# print(a , type(a))

# d ={
#     "Kya hua" : "What Happen?",
#     "Beth jao" : "Sit Down!",
#     "Kitna" : "How much?"
# }

# word = input("Enter the word you want meaning of : ")

# print(d[word])

# s = set()

# l = input("Enter number 1 : ")
# s.add(int(l))
# l = input("Enter number 2 : ")
# s.add(int(l))
# l = input("Enter number 3 : ")
# s.add(int(l))
# l = input("Enter number 4 : ")
# s.add(int(l))
# l = input("Enter number 5 : ")
# s.add(int(l))
# l = input("Enter number 6 : ")
# s.add(int(l))
# l = input("Enter number 7 : ")
# s.add(int(l))
# l = input("Enter number 8 : ")
# s.add(int(l))

# print(s)

# s = set()
# s.add(20)
# s.add(20.5)
# s.add("20")

# print(len(s))

# d = {}

# name = input("Enter friends name : " )
# lang = input("Enter language name : " )
# d.update({name:lang})

# name = input("Enter friends name : " )
# lang = input("Enter language name : " )
# d.update({name:lang})

# name = input("Enter friends name : " )
# lang = input("Enter language name : " )
# d.update({name:lang})

# name = input("Enter friends name : " )
# lang = input("Enter language name : " )
# d.update({name:lang})

# print(d)


# a = int(input("Enter your age : "))

# if(a >= 18):
#     print("License Confirmed !!")
    
# else:
#     print("License Not Confirmed **")

def greet():
    print("Good Day !!" )
    
greet()
    