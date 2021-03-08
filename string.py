#Creating a string
msg = "Hello World"
print(msg)

#----------------------------------------------------------------------
#string escape characters:

msg1 = "Hello"		#good
print(msg1)

msg2 = "Hello	Hey"	#good, you can put in a tab
print(msg2)

#msg3 = "Hello 
#Hey"			#bad, you can press enter
###print(msg3)

#to put a new line in a string:
msg4 = "Hello\nHey"
print(msg4)

#To do a tab char
msg5 = "Hello\tHey"
print(msg5)

#can also use the hexadecimal value: (Get all hex number from ASCII table)
msg6 = "\x41"	#to print A
print(msg6)

#To print a double quote ":
msg7 = "\""
print(msg7)

#if you want to print \t: (escape an escape char)
msg8 = "\\t"
print(msg8)

#-----------------------------------------------------
#Single quotes vs Double quotes:
	#They work exactly the same way in Python
	#It doesn't matter which one you use

msg9 = "Hello"
msg10 = 'Hello'
print(msg9)
print(msg10)
#prints the same thing

#example that works for double quotes but not single quotes:
msg11 = "You're pretty"
print(msg11)

#msg12 = 'You're pretty'
#print(msg12)

#example that works for single quotes but not double quotes:
msg13 = 'She said "eww"'
#msg14 = "She said "eww""

#if you want to use double quotes you can escape the double quote
msg15 = "She said \"eww\""

#you can also escape the double quote with a single quote, though it is
#not necessary
msg16 = 'She said \"eww\"'

#you can also escape the single quote if you want to use single quotes
msg17 = 'you\'re cute'

#Use quotation marks however you like but if you are going to have quotes in a
#string then use one of the other depending on the quote you'll have in the 
#string.

#you can also prefix with r which will make a raw string (ignoring escapes
#except same quotes)

print(r 'as raw as I\'ve ever seen, \/\/ () \/\/. \t' )	#only \' is escaped


####################### CONCATENATION ##################################

#-----------------------------------------------------------------------
#Concatenation:

#use a + to concatenate

#how to combine strings:
msg18 = "you're cute"
msg19 = "hmu"
print(msg18 + "..." + msg19)
print(msg18, msg19)
#expecting 1 argument --> concatenation

#can use comma seperated values in print. Automatically uses spaces between.

#Separate concatenation:
full_message = msg18 + "..." + msg19
print(full_message)

#----------------------------------------------------------------------
#Concatenation with literals:

msg20 = "you're cute"				#string literal that is hard coded
msg21 = "hmu"						#msg20 and msg21 are variables but in
									#quotation marks is literals

full_message1 = msg20 + "..." + msg21	#When working with literals you don't
										#have to use the plus operator

print("Hey" " " "there" "!")		#don't have to use operators

#if you want to break a string into multiple lines:
msg22 = "This is a ling string...."
"continued"

print(msg22)				#doesn't print the continued

#unless you put it in parenthesis:
msg23 = ("This is a long string...."
"continued")

print(msg23)				#now prints the continued

#
msg24 = "helllo"
#print(msg24 " there")			#won't work you have to have the plus operator
								#when working with variables

print(msg24 + " there")			#will work

#----------------------------------------------------------------------
#Multiline strings:

poem = ("This is all combined"
"as one happy string..."
"what was that sound? "
"it was a doorbell, ring."
" When I see you, my heart sings"
"here plz take this diamond ring")

print(poem)		#puts everything into 1 string

#To put new lines and spaces:
poem1 = """"This is all combined
as one happy string...
what was that sound?
it was a doorbell, ring.
When I see you, my heart sings
"here plz take this diamond ring"""

print(poem1)	#everything goes out on a new line
				#the new line char is automatically inserted
				#string is written out line by line

#If you want a mixture of both:
poem2 = """"This is all combined \
as one happy string...
what was that sound? \
it was a doorbell, ring. \
When I see you, my heart sings
"here plz take this diamond ring"""

print(poem2)	#to get rid of the new line char just put a backslash at the
				#end of the line.

########################## INDEXES  #####################################

#-------------------------------------------------------------------
#Indexes:

#how to grab a char with an index:
poem3 = "Where am I?"
print(poem3[0])		#gives "W"
print(poem3[1])		#gives "h"
print(poem3[5])		#gives " "

#if you put an index that is too large you get an error -->string index out of
#range

#Can also use negative numbers as an index to get chars from the right.

######################### SLICING  #####################################

#-------------------------------------------------------------------
#Slicing Strings:

#use slicing to grab a particular char or a range of char's (substring)

poem4 = "Where am I?"

print(poem4[5:])	#gives the substring from 5 to the end of the string
print(poem4[:5])	#gives the substring from the beginning of the string to
					#the 5th char

#When the number is on the left of the colon it is inclusive but when it is
#on the right it is exclusive

#-------------------------------------------------------------------
#Negatives with String Slicing:

#
poem5 = "Where am I?"

print(poem5[-1])	#gives "? --> it gives the 1st char from the right

print(0 == -0)		#true
print(1 == -1)		#false

#There is only 1 zero, that's why the first char on the right starts at 1.

print(poem5[5:])
print(poem5[-5:])

#when you do a positive 5, you start at index 5 and include that index.
#when you say negative 5, you start at the 5th index from the right and it is
#also inclusive

print(poem5[:7])
print(poem5[:-7])

#When you put a number after the colon, you are asking where you want to go up
#to (7th index not include). 
#When you put a negative number after the colon, you go up until the negative
#7th char (the -7th char is not included).

#-------------------------------------------------------------------
#Slicing with Two Numbers:

#how to grab a part of the string:
poem6 = "Where am I?"

print(poem6[6:8])

#starting position is always inclusive.
#ending position is not inclusive.

#gives the same output
print(poem6[6:-3])

#grab a particular amount of chars:
start = 6
print(poem6[start:start+2])			#grabs 2 chars


name = "Caleb Curry"
start_of_last = 6
print(name[start_of_last:start_of_last+3])

#Try to only use negative numbers on the right side of the colon
#Consider indices as the in between of chars.

####################### IMMUTABILITY ##################################

#-------------------------------------------------------------------
#Strings are Immutable:

task = "Subscribe"
print(id(task))		#prints the number that refers to the where the object is
					#located in memory

#if we have a string we can't change the string to something else. 

task = "like"
print(id(task))		#location changes because it is now a different value

task = task[0]		#gives a char
#task[0] = "s"		#gives an error because a string can't be changed

#But lists are mutable

#immutablity is good, because we can't change the data.
task = task + "!"		#replaces the old string
print(id(task))

different = task		#doesn't change the location of task
different = "hey"
print(task)				#location would change if mutable

task = ["Subscribe"]
different = task
different[0] = "hey"
print(task)				#now shows the change that was made

#strings and numbers --> immutable
#lists --> mutable

###################### GETTING STRING LENGTH ###########################

#-------------------------------------------------------------------
#len() Function:

msg = "please subsribe"
print(msg)

#can grab indices of this:
print(msg[6])

#Figure out the total number of indices:
msg1 = "please subscribe"
print(len(msg1))		#gives the total number of chars

#max index is always len-1

##################### MORE STRING WORK ###############################

#-------------------------------------------------------------------
#Convert Integer to String:

msg = "please subscribe"
print("Your message was "+ str(len(msg)) + "characters long")

#or you can use:
print("Your message was", len(msg), "characters long")

#when using comma's will automatically put spaces in the sentence.

#-------------------------------------------------------------------
#Nested Function Calls:

import math
age = 15
print(len(str(id(str(age)) + math.floor(2.6))))
