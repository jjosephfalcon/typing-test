

import time 
from threading import Thread

# myList = ['blue', 'green', 'yellow']

# for i in myList:
#   print(i)
#   time.sleep(1)

# print("Welcome to the type racer!")
# time.sleep(1)
# print('.')
# time.sleep(1)
# print('..')
# time.sleep(1)
# print('...')
# time.sleep(1)
# print('....')

# print("GET READY TO PLAY!")


# def check():
#   # Function waits 5+5 seconds before letting user know they lost
#   time.sleep(10)
#   print("You ran out of time!")
#   # returns False so we can check when function is over
#   return False

# print("Print the message below: ")
# message = "type this as fast as you can"
# print(message)

# while check() != False:
#   # Asking user to type their answer
#   Thread(target = check).start()
#   answer = input("")

#   # Check if answer is the same as message 
#   if answer == message:
#     print("You got it right!")
#     break
#   else: # If answer doesn't match print you lost 
#     print("You lost!")
#     break

import time
from threading import Thread

# We set answer to None (no value)
answer = None


messages = ["the cat catches the mouse", "the dog runs up the wall", "the fooysal lickes the salty pepper", "kemal codes like a pro!", "turtles are super fast", "i cannot believe you made it this far!"]



def check():
    time.sleep(7)
    # If answer has a value other than None, then end function.
    if answer != None:
        return
    # If function doesn't end, print the following: "SlowPok"
    print("Too SlowPok")

# Ignore this: Library used to check time
Thread(target = check).start()

score = 0

while True:
  # Loop through our messages: 
  for i in messages:
    
    print(f'<<< Score: {score} >>>')
    print("Print the message below: ")
    print('\n',i)
    answer = input("Type: ")

    if answer == i:
      print("You got it right!")
      score += 25
    else:
      print("You typed it wrong!")
  
  print("\nYou typed them all!")
  print(f"Final Score: {score}")
  break

