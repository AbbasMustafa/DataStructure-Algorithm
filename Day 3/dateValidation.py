
def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    start = year1, month1, day1
    end = year2,month2,day2

    # Check Validation
    # Assume Eache month has 30 days
    if(not isDateBefore(start,end)):
        return "AssertionError"

    days = 0
    start = nextDay(year1, month1, day1)
    while( isDateBefore(start, end) ):
        days+=1
        start = nextDay(start[0],start[1],start[2])

    return days
        


def isDateBefore(start, end):
    return start <= end
    

def test():
    test_cases = [((2012,10,30,2012,10,30),0), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print("Test with data:", args, "failed")
            else:
                print("Test case passed!")
        except AssertionError:
            if answer == "AssertionError":
                print("Nice job! Test case {0} correctly raises AssertionError!\n".format(args))
            else:
                print("Check your work! Test case {0} should not raise AssertionError!\n".format(args))       


test()
    
