"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def SumUpCalls(calls):
    timeDict = {}
    for i in calls:
        if i[0] in timeDict:
            timeDict[i[0]] += int(i[3])
        else:
            timeDict[i[0]] = int(i[3])
            
        if i[1] in timeDict:
            timeDict[i[1]] += int(i[3])
        else:
            timeDict[i[1]] = int(i[3])
        
    return timeDict

    

def findMax(timeDict):
    maxValue = 0
    key = 0

    for i in timeDict.keys():
        if maxValue < timeDict[i]:
            maxValue = timeDict[i]
            key = i

    return (key,maxValue)

if __name__ == "__main__":
    timeDict = SumUpCalls(calls)
    key,maxValue = findMax(timeDict)

    print("{} spent the longest time, {} seconds, on the phone during September 2016".format(key,maxValue))
        
    ## Wrost Case Complexity For this problem is O(n+n) = O(n)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

