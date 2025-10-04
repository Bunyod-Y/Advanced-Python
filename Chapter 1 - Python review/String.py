firstName ="Bunyod" #firstName is variable of string type
print(firstName) # Bunyod
fullName ="Bunyod Yokubov"
print(fullName) # Bunyod Yokubov

#input issued to take input from user
score1 = input("Enter the score 1:") #enter some value e.g. 12
score2 = input("Enter the score 2:") #enter some value e.g. 36
totalString =score1 + score2 # add score1 and score2
messageString= "Total score is %s"
#in below print, total string will be assinge to %s of message String
print(messageString % totalString) # 1236 (undesired result)

#score1 and score2 are saved as string above
#first we need to convert these into integers as below
totalInt =int(score1) + int(score2) #add score1 and score2
messageString= "Total score is %s"
print(messageString % totalInt) # 48

#change the input as integer immediately
score1 = int(input("Enter the score1: ")) #enter some value e.g. 12
score2 = int(input("Enter the score2: ")) #enter some value e.g. 36
total = score1 + score2 # add score1 and score2
messageString= "score1(%s) + score2[%s] = %s"
print(messageString % (score1, score2,total)) #score1(12) +score2[36] = 48