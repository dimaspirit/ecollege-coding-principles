# Use the gmtime() function (in the time library module) to generate the current date and time.
# Use the strftime() function (also from the time library module), to format the date and time as a String.

from time import gmtime, strftime

print(strftime("%Y-%B-%d, %H:%M:%S"), gmtime())

