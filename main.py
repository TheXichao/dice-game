import random
import os

userList = []
total1 = 0
total2 = 0

def authUser():    
    userUsername = input("Username: ")
    userPassword = input("Password: ")
    loginFile = open("login.txt", "r")
    for logins in loginFile.readlines():
        user, password = logins.strip().split(":",1)
        if (userUsername == user) and (userPassword == password):
            if user not in userList:
              userList.append(user)
              print ("Login successful!")
              return True
            else:
              print('Haha. Good one, you\'re trying to play with your self!')
    print ("Wrong username/password")
    authUser()
    
    
def welcomeScreen(user1,user2):
  os.system('clear')
  print(f'{user1} and {user2} has entered the game')

def rollDice(user1,user2):
  global total1, total2
  print(f'its {user1}\'s turn')
  input('Press enter when you are ready to continue: ')
  os.system('clear')
  roll1 = random.randint(1,6)
  total1 += roll1
  print(f'{user1} you rolled {roll1}, your total score is {total1}')
  print(f'its {user2}\'s turn')
  input('Press enter when you are ready to continue: ')
  os.system('clear')
  roll2 = random.randint(1,6)
  total2 += roll2
  print(f'{user2} you rolled {roll2}, your total score is {total2}')
  input('press enter to continue ')
    
def leaderBoard(player1,player2):
  os.system('clear')
  global total1, total2
  if total1 > total2:
    print(f'player1 ({player1}) with {total1} points, seems to be winning. player2 ({player2}) with {total2} points are behind')
  elif total1 < total2:
    print(f'player2 ({player2}) with {total2} points, seems to be winning. player1 ({player1}) with {total1} points are behind')
  else:
    print(f'you two are drawing with {total1} points')

def endScreen(player1,player2):
  os.system('clear')
  if total1 > total2:
    print(f'player2: {player2} with {total2} points won!!! Congrats. However, player1: {player1} with {total1} points are behind')
  elif total1 < total2:
    print(f'player2: {player2} with {total2} points won!!! Congrats. However, player1: {player1} with {total1} points are behind')
  else:
    print(f'you two are drew with {total1} points')
  


def main():
  authUser()
  authUser()
  player1 = userList[0]
  player2 = userList[1]
  welcomeScreen(player1,player2)
  for i in range(5):
    rollDice(player1,player2)
    leaderBoard(player1,player2)
  endScreen(player1,player2)
  

main()
