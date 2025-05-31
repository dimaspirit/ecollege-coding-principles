# Use the gmtime() function (in the time library module) to generate the current date and time.
# Use the strftime() function (also from the time library module), to format the date as a String.

from time import gmtime, strftime

timestamp = strftime('%A, %d %b %Y', gmtime())
print("Today is", timestamp)

