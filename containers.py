#working with lists

#there are two ways to create an empty list

#using the keyboard

fruit = list()
print (fruit)
#using correct square brackets

fruit = []
#If i want to satrt with items in the list
#          0         1        2
fruit = ['Apple','Orange','Banana']

# interable = positional index in containers
#Mutable = you can add or take away from list

#Entire list?
print(fruit)
#Specific item from the list? Use positional Index
#want Orange

print(fruit[1])
#want to add to list?
fruit.append('Blueberry')

print(fruit)
#append any data type to list

fruit.append (8)
print (fruit)

#remove last item from list using .pop
fruit.pop()
print (fruit)
#to change data: call its positional index
fruit[2] = 'Mango'
print(fruit)
#if u want to remove
fruit.remove ('Apple')
print(fruit)
#determine length of list
print (len(fruit))
#check to see if something is 'in' a list

ask = input('Enter a fruit: ')
if ask in fruit:
    print('this fruit is in the list')
else:
    print ('fruit is not in the list')

#sort list
fruit.sort()
#sorts alphabetically if string, numerically if an interger
import random
nums = []
for i in range (1000):
    x = random.randint(0,10)
    nums.append(x)
