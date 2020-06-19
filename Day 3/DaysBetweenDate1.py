

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# Find Days Between Date
# Assume Each Month has 30 Days  
def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    start = nextDay(year1,month1,day1)
    end = year2,month2,day2
    days = 0
    
    while( isDateBefore(start, end) ):
        days+=1
        start = nextDay(start[0],start[1],start[2])

    return days
        


def isDateBefore(start, end):
    return start <= end
    

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

    
test()
    
