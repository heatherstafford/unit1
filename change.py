#Heather Stafford
#1/25/18
#change.py

change = int(input('Enter amount of cents: '))
quarters = int(change/25)
print('Quarters:', quarters)
remainder1 = change%25 
dimes = int(remainder1/10)
print('Dimes: ',dimes)
remainder2 = int(remainder1%10)
nickles = int(remainder2/5)
print('Nickles: ',nickles)
remainder3 = int(remainder2%5)
pennies = int(remainder3/1)
print('Pennies: ',pennies)