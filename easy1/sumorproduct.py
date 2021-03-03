# write a program that asks the user to enter an integer freater than 0, then asks whehter the user wants to determine the sum or the product of all number between 1
# and the entered integers

number = int(input("Please enter an integer greater than 0: "))
sum_or_product = input("Enter 's' to compute the sum, or 'p' to compute the product. ")

total = 0 if sum_or_product == 's' else 1
count = 1 
while count <= number:
  if sum_or_product == 's':
    total = total + count
  else:
    total *= count
  count += 1

print(total)
