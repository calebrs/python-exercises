#write a function that takes an integer argument and returns true
# if absolute value is odd.

def is_odd(num):
  return abs(num) % 2 == 1


print(is_odd(2))
print(is_odd(5))
print(is_odd(-17))
print(is_odd(-8))
print(is_odd(0))
print(is_odd(7))