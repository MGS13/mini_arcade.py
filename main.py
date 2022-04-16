import timeit

start = timeit.timeit()


end = timeit.timeit()
#print(end - start) 

my_list=[]
quantity=input("How many items do you have?")

prices=[1.95,4.50,0.99,5.99]
total=0
for add in prices:
  total+= add
 
print(total)

item1 = 10
item2 = 20




password="simonsnyc"
u_input= input("What is the password? ")
while u_input != password:
  u_input= input("Incorrect!, try again ")
else:
  print("Correct! You may enter!")


import random
counter=0
start = timeit.timeit()
num_games = int(input("How many games do you want to play?"))
for num in range(num_games):
  x = random.randint(1,10)
  print(x)
  counter+=1
  
  player_guess=int(input("What is your guess?\n"))
  print(counter)
  print("above this is the counter ^\n")
  if x>player_guess:
    print("Your guess is too low!")
  elif x<player_guess:
    print("Your guess is too high")
  else:
    print("You guessed correct!")
    

print("Thank you for playing!, it took you:", str(counter), " attempts!")