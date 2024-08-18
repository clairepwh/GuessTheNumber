import random
import time

while True:
  choice = input("Enter a number from 1 to 9:")
  if choice.isdigit():
    choice = int(choice)
    break
  else:
    print("Please enter a valid integer.", end='\r')

for i in range(50):
  print(random.randint(1, 9), end='\r')
  time.sleep(0.05) 
  print(" ", end='\r')

final_number = random.randint(1, 9)
print("\nThe final number is...")
time.sleep(1)
print(final_number)

win_message = ".o...o..ooo..o...o..o...o.ooooo.o...o.\n..o.o..o...o.o...o..o...o...o...oo..o.\n...o...o...o.o...o..o.o.o...o...o.o.o.\n...o...o...o.o...o...o.o....o...o..oo.\n...o....ooo...ooo....o.o..ooooo.o...o."
lose_message = "YOU LOST!!!"
if final_number == int(choice):
  print(win_message)
else:
  for letter in lose_message:
    print(letter * 20)
# .o...o..ooo..o...o..o...o.ooooo.o...o.\n
# ..o.o..o...o.o...o..o...o...o...oo..o.\n
# ...o...o...o.o...o..o.o.o...o...o.o.o.\n
# ...o...o...o.o...o...o.o....o...o..oo.\n
# ...o....ooo...ooo....o.o..ooooo.o...o.
