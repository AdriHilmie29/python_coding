# Write a function that determines how many days there are in a particular month. Your function will take
# two parameters: The month as an integer between 1 and 12, and the year as a four-digit integer. Ensure
# that your function reports the correct number of days in February for leap years. Include a main program
# that reads a month and year from the user and displays the number of days in that month.

-

month = int(input('Please enter a month in the form of digit : '))

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31

    year = int(input('Please enter the year : '))
    print('Number of days in month %d in year %d is %d' % (month, year, days))

elif month in (4, 6, 9, 11):
    days = 30

    year = int(input('Please enter the year : '))
    print('Number of days in month %d in year %d is %d' % (month, year, days))

elif month == 2:

    year = int(input('Please enter the year : '))
    if (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
        days = 29
    else:
        days = 28
    print('Number of days in month %d in year %d is %d' % (month, year, days))

else:
    print('You insert an invalid month')
