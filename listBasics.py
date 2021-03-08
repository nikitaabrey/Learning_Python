#What is a list?
#It's a type of collection, it holds numerous things.

#Creating a List and Indexing:

ages = [12, 18, 28]		#list of numbers

people = ["Caleb", "Sabrina", "Emily"]	#list of strings

#you are able to mix different types in a list
my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]

#we can print an entire list by using the list name
print(ages)
print(people)
print(my_favourite_things)
#all of the print statements, prints the list

############################# INDEXING ################################
#Changing and Slicing a list:

#lists are mutable --> we can change them without creating a new one
#elements inside the list are immutable.

print(id(my_favourite_things))

my_favourite_things[0] = "Walking"	#use indexing to grab the 1st element
print(id(my_favourite_things)) #it is still the same list as before the change	
print(my_favourite_things)

print(len(my_favourite_things))	#tells you the number of elements in the list

#---------------------------------------------------------------------

######################## UPDATING AND SLICING #########################

#lists are different than strings in that the data can be changed.

#how to update a list:
ages[0] = 5
ages[1] = 10
ages[2] = 15
print(ages)	#updated

#slicing:
print(ages[1:])

#since lists are mutable, we can combine slicing with updating data:
ages[1:] = [6, 7]

#---------------------------------------------------------------------

########################## COPYING LISTS  ############################
#How to Copy a list:
my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]
print(my_favourite_things[1:2])	#start at index 1 and up to but not included
								#to 2	

print(my_favourite_things[:])	#prints the entire list

copy = my_favourite_things[:]	#assign list to a variable
print(copy)

#can change copy without changing the original list
copy[0] = "walking"

print(my_favourite_things, copy)
#they are now 2 seperate objects and a change in the one doesn't effect the
#other.

copy = my_favourite_things	#doesn't make a copy, we are making an alias.
#thus a change in copy will change the original list. 

#another way to make a copy:
copy = my_favourite_things.copy() #the dot operator attaches an object to a
								  #function

#functions attached to objects are known as methods.

copy[0] = "walking"
print(my_favourite_things, copy)

#---------------------------------------------------------------------

####################### NESTED LIST BASICS ###########################
#Intro to Nested Lists (2D Lists):
#A nested list is just a list inside of a list.

my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]

#want to grab the list inside of a list
print(my_favourite_things[2][1]) #grabs an element in nested list
#first [] is outer list. Second [] is inner list.

#can have many nested lists
my_favourite_things = ["Working out", 7, ['Amazon prime', ['netflix', 'hulu']]]
print(my_favourite_things[2][1][0])

#to get the number of elements on the 3rd list
print(len(my_favourite_things[2][1]))

#if you have a list of a list you have to be careful when copying it.

#---------------------------------------------------------------------

##################### SHALLOW COPY EXPLAINED  ########################

#When you make a shallow copy of a list, it means that any complex types
#will not be copied but rather available in both. 

my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]
my_favourite_things2 = my_favourite_things.copy()

#modify the original
my_favourite_things[2][0] = "Audible"
print(my_favourite_things2)	#contains Audible
#the copy points to the same data

#---------------------------------------------------------------------

############################# DEEP COPY ##############################
#How to Deep Copy a List:

my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]

copy = my_favourite_things.copy()	#shallow copy
print(my_favourite_things, copy)

copy[0] = "walking"					#only changes the copy
print(my_favourite_things, copy)

#if you change somehting in the list 
copy[2][0] = "Hulu"			#change happens in the copy and the main list
print(my_favourite_things, copy)

#shallow copies make a copy of all of the immutable data, but any of the
#mutable data that we can create an alias for (such as lists) those are not
#copied by value but rather there is just an alias to that same list.

print(id(copy[2])
print(id(my_favourite_things[2]))
#points to the same location

#To make a deep copy:
import copy

my_favourite_things = ["Working out", 7, ['Amazon prime', 'netflix']]

c = copy.deepcopy(my_favourite_things)	#makes a deep copy

print(my_favourite_things, c)

print(id(c[2])
print(id(my_favourite_things[2])
#points to different locations

#If you have many nested lists this method would still work, but it
#would hurt your memory if you have a big data structure. It is however
#safer to a deep copy.
#You are essentially making 2 of the same data structure so you will have
#to double the amount of memory that you use. 

#---------------------------------------------------------------------

####################### COMBINING LISTS #############################
#Combining Lists (Concatenation of Lists):

my_favourite_things = ["Working out", 7, ["amazon prime", "netflix"]]
least_favourite_things = ["onions", "javaScript"]

#we can use "+" to concatenate:
print(my_favourite_things + least_favourite_things)

#to add an element to the list:
least_favourite_things = least_favourite_things + ["editing"]
print(least_favourite_things)

#another way to add an element to the list:
least_favourite_things.append("editing")
print(least_favourite_things)

#append is better to use
