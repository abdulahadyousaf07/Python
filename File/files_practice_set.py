
# f = open("poems.txt")
# content = f.read()

# if("Twinkle" in content):
#     print("YES")
    
    
# else:
#     print("NO")
# f.close()

# 02 Question
# import random
# def game():
#     print("You are playing a game ...")
#     score = random.randint(1 , 50)
#     # Fetch High Score
#     with open("hiscore.txt") as f:
#         hiScore = f.read()
#         if(hiScore != ""):
#             hiScore = int(hiScore)
#         else:
#             hiScore = 0
        
#     print(f"Your Score is : {score}")
    
#     if(score > hiScore):
#         with open("hiscore.txt" , "w") as f:
#             f.write(str(score))
            
#     return score

# game()

#04 Question
# word = "Donkey"
# with open("donkey.txt" , "r") as f:
#     content = f.read()
#     contentNew = content.replace(word , "######")
    
# with open("donkey.txt" , "w") as f:
#     f.write(contentNew)

#05 Question
words = ["Donkey" , "Man" , "Poor" , "carriage"]
with open("donkey.txt" , "r") as f:
    content = f.read()
    
    for word in words:
        content = content.replace(word , "#" * len(word))
    
with open("donkey.txt" , "w") as f:
    f.write(content)