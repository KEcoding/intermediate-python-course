import random
def main():
  dice_rolls = int(input("How many dice would you like to roll?")) 
  dice_size = int(input("how many sides do the dice have?"))

  dice_sum = 0 
  for i in range (0, dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum = dice_sum + roll
    if roll == 1:
      print("Ew, you have a one! Game over!")
      break
    elif roll == dice_size:
      print("you have a 6! Critical success!")

    else:
      print(f'You rolled a {roll} !')
      
    
  print(f'You have a sum of {dice_sum}')


if __name__== "__main__":
  main()