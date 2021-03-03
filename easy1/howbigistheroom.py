#getting user input for the length and width of a room
# logs the area in square meters and feet
length = int(input("Enter the length of the room in meters: "))
width = int(input("Enter the width of the room in meters: "))

area_in_meters = length * width
area_in_feet = round(area_in_meters * 10.7639, 2)

print(f'The area of the room is {area_in_meters} square meters ({area_in_feet} square feet)')