import random
Secret = "I made a number from 1 to 1000"
Case = random.randint(1,1000)
print(Case)
print(Secret)
Attempt = 0
Input = 0
while Input != Case :
  print("Guess the number: ", end="")
  Input = int(input())
  Attempt = Attempt + 1
  if Input < Case :
    print("Too small!")
  if Input > Case :
    print("Too big!")
  if Input == Case :
    print("Correctly!")
print("You tried " + str(Attempt) + " times.")


