import random


def cows_and_bulls():
	answer = str(random.randint(0000, 9999))
	print ("To exit during play, type exit at any point")
	guesses = check = cow = bull = 0
	user_guess = ""

	while user_guess != answer:
		check = cow = bull = 0
		user_guess = input("Please enter a 4 digit number: ")
		if user_guess == "exit":
			print ("Thank you for playing")
			break
		elif user_guess != answer:
			for number in user_guess:
				if number == answer[check]:
					cow += 1
				elif number in answer:
					bull += 1
				check += 1
				continue
			print (str(cow) + " cows, " + str(bull) + " bulls")
		guesses += 1
	print ("You guessed " + answer + " correctly in " + str(guesses) + " guesses")


cows_and_bulls()
