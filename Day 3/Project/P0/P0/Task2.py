"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def uniqueValue(calls):
    time = {}
    for i in calls:
        time[i[0]] = i[3]
    
    return time

def FindMaxValue(uniqueValue):
    maxValue = 0
    key = 0
    for i in uniqueValue.keys():
        if(maxValue < int(uniqueValue[i])):
            maxValue = int(uniqueValue[i])
            key = i
    return (key,maxValue)

if __name__ == "__main__":
    time = uniqueValue(calls)
    key, maxValue = FindMaxValue(time)

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key,maxValue))
    
    ## Wrost Case Complexity For this problem is O(n + n + n) = O(3n)
    ## So We Focus only on O(n)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

