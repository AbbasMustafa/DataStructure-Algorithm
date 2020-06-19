"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

if __name__ == '__main__':
    callSenders = {}
    callReceivers = {}
    messageSenders = {}
    messageReceivers = {}

    for call,text in zip(calls,texts):
        callSenders[call[0]] = call[0]
        callReceivers[call[1]] = call[1]
        messageSenders[text[0]] = text[0]
        messageReceivers[text[1]] = text[1]

    finalList = []
    for i in callSenders:
        if i not in callReceivers and i not in messageSenders and i not in messageReceivers:
            finalList.append(i)

    print("These numbers could be telemarketers: ")
    for i in sorted(finalList):
        print(i)

    ## Wrost Case Complexity For this problem is O(n + n + n + n) = O(4n)
    ## So We Focus only on O(n)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

