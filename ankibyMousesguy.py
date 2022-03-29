import csv
import random
from sys import exit

vocabulary = {}

def end():
	print('See you later!')
	print('...................')
	exit(0)


#Specify CSV full file name
filename = input('File name you want to study: ')

#Practice translating to English or foreign language
practice = input('Practice english translation, or foreign language? Type \'english\' or \'foreign\': ')

#Start the firstlanguage translation version
def first_language():
	max_rounds = int(input('How many words want to study? Enter number: '))
	print('...................')
	print('Let\'s get started!')
	print('...................')
	right = []
	wrong = []
	with open(filename) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			vocabulary[row['english']] = row['different']

	#Test with x rounds
	turns = 0	
	while turns < max_rounds: 
		for key in vocabulary:
			turns += 1   
			print(turns)
			vocab = str(random.choice(list(vocabulary.keys())))
			translation = str(vocabulary[vocab])
			print(vocab)
			guess = input('Translate this: ')
			if guess == translation:
				print('Correct!')
				right.append(vocab)
			elif guess != translation: #User gets one more try
				guess2 = input('Wrong! Try again: ') 
				if guess2 == translation: 
					print('Correct!')
					right.append(vocab)
				else:
					print('Wrong! Correct answer is: ', translation)
					wrong.append(vocab)	
			else: 
				print('Error. Try again')
				break
			
			break 

	#Provide summary of test performance	
	right_count = len(right)
	wrong_count = len(wrong)
	print('...................')
	print('Test results: ')
	print('Correct: %d' % right_count) #How many values are correct
	print('Wrong: %d' % wrong_count) #How many values are wrong
	print('...................')
	print('Great job! Study these words again:')
	study_again = ', '.join(wrong)
	print(study_again)
	print('...................')
	next = input("""Great job! Study again? Type y/n to (continue)\nOr start with (foreign)? Type w:""")
	print('...................')
	if next == 'y':
		first_language()
	elif next=='w':
		second_language()
	elif next == 'n':
		end()

#Start the fsecondlanguage language test
def second_language():
	max_rounds = int(input('How many words want to study? Enter number: '))
	print('...................')
	print('Let\'s start!')
	print('...................')

	right = []
	wrong = []

	with open(filename) as readFile:
		reader = csv.DictReader(readFile)
		for row in reader:
			vocabulary[row['different']] = row['english']

	turns = 0	
	while turns < max_rounds: 
		for key in vocabulary:
			turns += 1
			print(turns)
			vocab = str(random.choice(list(vocabulary.keys())))
			translation = str(vocabulary[vocab])
			print(vocab)
			guess = input('Translate this: ')
			if guess == translation:
				print('Correct!')
				right.append(vocab)
			elif guess != translation: #User gets one more try
				guess2 = input('Wrong! Try again: ') 
				if guess2 == translation: 
					print('Correct!')
					right.append(vocab)
				else:
					print('Wrong! Correct answer: ', translation)
					wrong.append(vocab)	
			else: 
				print('Error. Try again.')
				break
			break 

	#Provide summary of test performance	
	right_count = len(right)
	wrong_count = len(wrong)

	print('...................')
	print('Test results: ')
	print('Correct: %d' % right_count) #How many values are correct
	print('Wrong: %d' % wrong_count) #How many values are wrong
	print('...................')

	print('Great job! Study these words again:')
	study_again = ', '.join(wrong)
	print(study_again)
	print('...................')
	next = input('''Great job! Study again? Type y/n to (continue)\nOr start with (english)? Type w:''')
	print('...................')
if next == 'y':
	second_language()
elif next=='w':
	first_language()
elif next == 'n':
	end()


#Choose to practice english translations, or foreign lang translations
if practice == 'english':
	first_language()
elif practice == 'foreign':
	second_language()
elif practice!='english' or practice!='foreign':
	practice2=input('Type only english/foreign:')
	if practice2=='english':
		first_language()
	elif practice2=='foreign':
		second_language()
	else:
		print('Wrong input, please restart the program.')
else:
	print('Wrong input, please restart the program.')
	end(0)