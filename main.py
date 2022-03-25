import time
def login():
   username = ["h.singh", "trav","paul","sheikh","aleks","ben","valentin","laylan","aiden","admin"]
   password = ["123", "456","789","abc","abc1","abc2","abc3","abc4","abc5","password"]

   global User
   y=False
   while y is False:
    User = input("enter username: ")
    Pass = input("enter password: ")
    
    if User in username :
     index=username.index(User)
     if Pass==password[index]:
      print("Get ready!")
      y= True
      return True
        
     else:
       print("incorrect password")
    else:
     print("incorrect username")
 

def quiz(): 
  import random
  x=0
  global score
  score=0
  while x<10:
   with open('playlist.csv') as file:
     playlist=file.readlines()
    
     song,artist=random.choice(playlist).split(',')
     music=song.split()
   
     Firstletters=[word[0] for word in music]
     print("guess the song: "+str(" ".join(Firstletters))+","+str(artist), end='' )
     answer=input("type answer: ")
     if answer == song:
                print("well done","\n")
                score = score + 3

                
     elif answer != song:
                answer = input("try again: ")
                
                if answer == song:
                    print("well done","\n")
                    score = score + 1
                

                
                else:
                   print("incorrect, the song was: "+str(song))
                   score = score - 1
                   break
                
   x+=1
              
  print("game finished, your score is: ", score)


def leaderboard(score):
  name=input("enter your name to save results: ")
  file=open("leaderboard.txt","a")
  file.write(str(score)+" points: "+name+"\n")
  file.close()

  file=open("leaderboard.txt","r")
  read=file.readlines()
  for lines in read:
   sort=sorted(read,key=lambda x:int(x.split()[0]),reverse=True)
  print("======================================")
  print("leaderboard:","\n")
  print("First place with "+str(sort[0]))
  print("second place with "+str(sort[1]))
  print("third place with "+str(sort[2]))
  print("fourth place with "+str(sort[3]))
  print("Fifth place with "+str(sort[4]))


def decision():
 while True:
  decision=input("to play as current user type 'current', to play as a differ user type 'differ'and to quit the game type'quit' "+"\n")
  if decision.lower()=="current":
     quiz()
     leaderboard(score)
  elif decision.lower()=="differ":
    login()
    quiz()
    leaderboard(score)
     
  else:
    return False




  

print("Welcome to guess the song where you get 3 points for gussing correct the first time and 1 on the second try but if your wrong you lose a point")
x=input("would you like to play, yes or no? " )
if x.lower()=="yes":
   if login() is True:
    time.sleep(1.5)
    quiz()
    time.sleep(1)
    leaderboard(score)
    decision()
    print("game over")
    
else:
  print("have a nice day")


