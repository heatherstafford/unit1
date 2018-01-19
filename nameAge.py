#Heather Stafford
#1/17/18
#nameAge.py

name = input('What is your full name?')
age = int(input('What is your age?'))
first, last = name.split()
print('Your first name has',len(first),'letters')
print('Your last name has',len(last),'letters')
print('Next year you will be',age+1,'years old')
