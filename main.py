#Encrypt/decrypt a message inside a string
from random import randint
from time import strftime

def random_letter():
	rInt = randint(0, 26)
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	return alphabet[rInt]
	
def random_str():
	string = ""
	for a in range(10):
		string = string+random_letter()
	return string

def num_to_let(num):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	num = num-1
	return alphabet[num]

def let_to_num(let):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	location = alphabet.find(let)+1
	return int(location)

def multiply(letter, second):
	number = let_to_num(letter)*int(second)
	return number

def divide(number, second):
	num = int(number/second)
	letter = num_to_let(num)
	return letter

def encrypt():
	word = input("Please enter the message to be encrypted:\n").lower()
	seconds = int(strftime("%S"))
	encryption = []
	for l in word:
		encryption.append(multiply(l, seconds))
	msg = ""
	for m in encryption:
		msg=msg+num_to_let(randint(0, 26)) + str(m) + num_to_let(randint(0, 26))
	msg = msg+str(seconds)+"\n"
	print("\nYour Encrptyed Key is:\n" + msg + "\n")
	return msg

def decrypt():
	word = input("Please enter your encryption key:\n")
	word=word+"a"
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	numbers = "1234567890"
	string = ""
	list_string = []
	for v in word:
		if v in alphabet:
			word = word[1:]
			if string != "":
				list_string.append(int(string))
				string = ""
		elif v in numbers:
			string = string+v
	final_string = ""
	sec = list_string.pop()
	for p in list_string:
		if p == 0:
			final_string = final_string+" "
		else:
			final_string = final_string+divide(p, sec)
	print(final_string)
	return final_string
