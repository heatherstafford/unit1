#Heather Stafford
#1/25/18
#isItATriangle.py

sideA = int(input('Enter Side A: '))
sideB = int(input('Enter Side B: '))
sideC = int(input('Enter Side C: '))
big = max(sideA,sideB,sideC)
small = min(sideA,sideB,sideC)
perimeter = int(sideA + sideB + sideC)
medium = (perimeter - big - small)
small + medium > big
