"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
caller = []
receiver = []
    
calls = []
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def AreaCodes(calls):
    callByBanglore = []
    for i in calls:
        if(i[0].find("080") >= 0):
            if(i[1].find("(") < 0):
                callByBanglore.append(i[1][:4])
            else:
                callByBanglore.append( i[1][ i[1].find("(") : i[1].find(")")+1 ] )
      
    return callByBanglore 




def UniqueCode(areaCode):
    code = set()
    for i in areaCode:
        code.add(i)
      
    return code
    
def Sorting(code):
    finalList = []
    for i in code:
        finalList.append(i)
      
    return sorted(finalList)

# # Part A
def PrintList(finalList):
    print("The numbers called by people in Bangalore have codes: ")
    for i in finalList:
        print(i)

# Part B
def calcPercentage(areaCode):
    count = 0
    for i in areaCode:
      if(i == "(080)"):
          count+=1

    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".
                          format(round(count/len(areaCode),4)*100))



if __name__ == "__main__":
    areaCode =  AreaCodes(calls)
    uniqueCode = UniqueCode(areaCode)
    finalList = Sorting(uniqueCode)
    PrintList(finalList)
    calcPercentage(areaCode)
    
    ## Wrost Case Complexity For this problem is O(n + n + n + n + n) = O(5n)
    ## So We Focus only on O(n)
    





"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
