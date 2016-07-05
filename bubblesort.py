import random
import datetime
start_time = datetime.datetime.now()
numList = [5,3,1,6,7,8,2,4]
# randNumList = []
# for i in range (0,100):
# 	randNumList.append(int((random.random()*100)))

def bubbleSort(numList):
	for i in range(0,len(numList)):
		for j in range(0,(len(numList)-(i+1))):
			if numList[j] > numList[j+1]:
				(numList[j], numList[j+1]) = (numList[j+1], numList[j])
		print numList

bubbleSort(numList)
# bubbleSort(randNumList)
print "Elapsed Time: " +str(datetime.datetime.now() - start_time)