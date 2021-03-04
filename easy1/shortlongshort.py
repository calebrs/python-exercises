# write a function that takes two strings and determines which one is longer. then it concats the two strings the shorter one + longer string + shorter string
def short_long_short(str1, str2):
  if len(str1) > len(str2):
    return str2 + str1 + str2
  else:
    return str1 + str2 + str1

print(short_long_short('abc', 'defgh'))
print(short_long_short('adcde', 'fgh'))
print(short_long_short('', 'xyz'))


# 