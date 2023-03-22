print("Welcome to my computer quiZ!!!")


playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
print("Okay! Let's Play :)")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print('Correct')
    score += 1
else:
    print("Incorrect!")
    
    
    
    
print("Your Score is: ", str(score))
    