def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    
    # Check Both Year is Same Or Not!
    # Which is Pass into CountDate Medthod
    flag = year1 != year2

    # Date According to Specific Months JAN: 31 etc
    dayInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    # Count Days In A given Year
    # How many days we lived in a given year
    days1 = CountDate(year1, month1,day1,dayInMonths,flag)
    days2 = CountDate(year2, month2,day2,dayInMonths)

    # Count Days Between Remining Years
    remainingDays = countDaysBetweenYear((year1+1),year2)
    

    # Check Both Year Is Same Or Not By Flag Variable
    totalDays = (days1+days2)+remainingDays if flag  else days2-days1
    
    return totalDays

# Count Days Between Remining Years
def countDaysBetweenYear(year1,year2):
    
    totalSum = 0
    for i in range(year1,year2):
        if( LeapYear(i) ):
            totalSum += 366
        else:
            totalSum += 365
    
    return totalSum

 
## Starts Here
## Calculate Days according to Month and Date
def CountDate(year, month, day, dayInMonths,flag=False):
    
    totalDays=0
    # Calculate Days Using dayInMonths List
    for index,value in enumerate(dayInMonths,1):
        if( index == month ):
            break
            
        # If Leap Year Add One More Day to this year    
        if(index == 2 and LeapYear(year)):
            totalDays+=1
            
        totalDays+=value
    
    # Add Remaining Days into the TotalDays
    totalDays+=day
    
    # Counts Remaining Day in a Specific Year
    # How many Days Remining in a given year
    if(flag):
        return EliminateDays(year,totalDays,month)
    else:
        return totalDays

# Count How many Days are Remining in a Given Month
def EliminateDays(year,Days,month):
    
    if(LeapYear(year) ):
        return 366-Days
    else:
        return 365-Days

# Is this a Leap Year Or Not
def LeapYear(year):
    if( year%4 == 0 and year%100 != 0):
        return True
    elif year%100 == 0 and year%400 == 0:
        return True
    else:
        return False

def testDaysBetweenDates():

    # test same day
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