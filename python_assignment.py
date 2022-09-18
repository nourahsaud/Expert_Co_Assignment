# This file includes 3 python tasks for Expert co assessment.
################################################################

# Task 1 
#________________________________________________________________
## Given a list of names, create a running Python project that sorts it alphabetically,
## Python has this functionality built-in, but see if you can do it without using sort()!
#________________________________________________________________

# A list of names to check the functionality of the task
from numpy import true_divide


names = ['norah', 'sara','yara', 'ahmed', 'fahad', 'nourah', 'saud', 'reema']

# a recursive function to sort the names
def sortalpha(list):
    # checks if the list length = 1 to end the recursion
    if len(list) == 1:
        return list
    # store the smallest value in sorted_list
    sorted_list = [min(list)]
    # remove the smallest from the original list
    list.remove(min(list))
    # recursion
    return sorted_list + sortalpha(list)

# Print the result
print(sortalpha(names))
#----------------------------------------------------------------
#################################################################


# Task 2
#________________________________________________________________
## Create a running Python project that can take two dates as input, and then
## calculate the amount of time between them.
#________________________________________________________________

# imports
import datetime

# input dates
print ('This program will calculate the amount of time between two dates of your choice !!!')
strdate1 = input('Enter a date in DD/MM/YYYY format ')
strdate2 = input('Enter another date in DD/MM/YYYY format ')

# split the string and change the type to int
year, month, day = map(int, strdate1.split('/'))
date1 = datetime.date(day,month,year)
year, month, day = map(int, strdate2.split('/'))
date2 = datetime.date(day,month,year)

# find the diffrence 
year = date1.year - date2.year
month = date1.month - date2.month
day = date1.day - date2.day

# print the result
print('{} Years, {} Months, {} Days'.format(year,month,day))

#----------------------------------------------------------------
#################################################################

# Task 3
#________________________________________________________________
# Create a running Python project to check if all digits of a number divide it; given a
# number n, find whether all digits of n divide it or not.
#________________________________________________________________

# take a number from the user
number = input('Enter any number ')
intnum = int(number)

flag = True
counter = 0

# strprint to store a string value to be printed later  
strprint = ''

# for loop to iterate through the digits and check if they divide the number or not 
for i in number:
    digit = int(i)
    if digit == 0 or intnum % digit != 0:
        flag = False
        break
    else:
        if counter + 1 == len(number):
            strprint += 'and {} % {} == 0'.format(intnum,digit)
        else:
            strprint += '{} % {} == 0, '.format(intnum,digit)
            counter += 1
            
if flag == False: 
    print('No')
else:
    print('Yes')
    print(strprint)
#----------------------------------------------------------------
#################################################################