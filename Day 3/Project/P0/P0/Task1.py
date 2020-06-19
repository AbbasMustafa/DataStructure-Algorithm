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
    tell_no = set()
    for text, call in zip(texts, calls):
        tell_no.add(text[0])
        tell_no.add(text[1])
        tell_no.add(call[0])
        tell_no.add(call[1])

    print("There are {} different telephone numbers in the records.".format(len(tell_no)))

    ## Wrost Case Complexity For this problem is O(n + n ) = O(2n)
    ## So We Focus only on O(n)
    ## Linear Order

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
