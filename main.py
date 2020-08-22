# Heads or Tails algorithm made in Python
# Made by KaBoomBox

# Importing modules
import random

# Main loop
while True:

	# Randomly generates a number between 0 (heads) and 1 (tails)
	answer = random.randint(0, 1)

	# Asks the user if they think the answer is heads or tails
	userInput = input("Heads or tails?")

	# If the user input is heads and the randomly generated number is 0 then it will say Correct!
	if userInput == "heads" and answer == 0:

		print("Correct!")

	# If the user input is tails and the randomly generated number is 1 then it will say Correct!
	elif userInput == "tails" and answer == 1:

		print("Correct!")

	# If the user input is not the same as the randomly generated number then it will say Incorrect!
	else:

		print("Incorrect!")