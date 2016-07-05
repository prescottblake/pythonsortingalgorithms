import random
import datetime
start_time = datetime.datetime.now()
randNumList = []
for i in range (0,100):
	randNumList.append(int((random.random()*100)))

numList = [8,5,2,6,9,3,5,4,8,7]

def selectionSort(numList):
	for i in range (0,len(numList)):
		min = numList[i]
		minIndex = i
		for j in range (i, len(numList)):
			if numList[j]< min:
				min = numList[j]
				minIndex = j
		(numList[i], numList[minIndex]) = (numList[minIndex], numList[i])
		print numList
	print numList
selectionSort(randNumList)
#selectionSort(numList)
print "Elapsed Time: " +str(datetime.datetime.now() - start_time)