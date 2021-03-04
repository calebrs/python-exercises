def isLeapYear(year):
  if (year % 400 == 0):
    return True
  elif (year % 100 == 0):
    return False
  else:
    return year % 4 == 0


print(isLeapYear(2016))      # true
print(isLeapYear(2015))      # false
print(isLeapYear(2100))      # false
print(isLeapYear(2400))      # true
print(isLeapYear(240000))    # true
print(isLeapYear(240001))    # false
print(isLeapYear(2000))      # true
print(isLeapYear(1900))      # false
print(isLeapYear(1752))      # true
print(isLeapYear(1700))      # false
print(isLeapYear(1))         # false
print(isLeapYear(100))       # false
print(isLeapYear(400))       # true


# Problem: 
# input: a year
# output: returns true if leap year, false if not
# rules: year is evenly divisible by 4
#        year is not divisible by 100
#        year is divisible by 400  

# Algorithm:
# 
