#Write a program that prompts the user to enter a series of age (number) to be inserted in a list named age. 
#The size of the list is 10. The program then, will evaluate the status of ‘child’ or ‘adult’ based on the user input. 
#If the age is less than or equal to 18, the program will store it in the children list. 
#However, if the age is greater than 19, the program will store it in the adult list. 
#The program has to display the content of the three lists. 
#The program also has to calculate and display the total number of elements in all of the lists. Name the Python file as age.py.


-

total = 0
age = []

a = (input('Enter age: '))

while a != '':
	age.append(int(a))
	a = input()


for i in age:
	if i <= 0:
		print('This age is not defined')
	elif i in range(1, 18):
		print('Children')

	elif i >= 19:
		print('Adult')



print(' ')
print('List of number you just input is', age)

print(' ')
Sum = sum(age)
print('The total sum of numbers in this list are', Sum)

print(' ')
print('There are', len(age), 'elements in the input')
