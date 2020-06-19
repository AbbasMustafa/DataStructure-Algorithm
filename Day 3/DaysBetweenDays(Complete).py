# Days In Month
# include Leap Day Calculation
def DaysInMonth(year, month):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if(month == 2 and isLeapYear(year)):
        return (months[month-1]+1)
    
    return months[month-1]

# Return Next Day of Given Date
def nextDay(year, month, day):
    if day < DaysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

# Main Algorithm     
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
        
# Terminating Condition
def isDateBefore(start, end):
    return start <= end
    
# Calculating Leap Year
def isLeapYear(year):
    if(year%4 == 0 and year%100 != 0):
        return True
    elif(year%100 == 0 and year%400 == 0):
        return True
    else:
        return False

def testDaysBetweenDates():

    # # # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(1994, 1, 17,
                              2020, 6, 17)  == 9648)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()