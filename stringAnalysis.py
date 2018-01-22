#Heather Stafford
#1/22/18
#stringAnalysis.py

text = input('Enter a sentence: ')
words = int(text.count(' '))
char = int(len(text))
print('Your sentence has',words,'words and',char,'characters and',(char - words),'letters')
search = input('Enter a character to search for, make it upper case: ')
phrase = text.upper()
letter = phrase.count(search)
print('your sentence has',letter,'of the character',search)

