numInput = int(input()) #number of numbers in list
numList = list(map(int, input().split())) #typing down the list

maxi = 0
mini = 0

for i in range(numInput):
     maxi = max(numList)
     mini = min(numList)
print (mini, maxi)