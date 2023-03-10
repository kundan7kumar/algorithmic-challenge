weight = [12,15,19,30,45]
person =['Sam','Veronica','Ram','smith','zhu']

print(list(zip(person,weight)))

for i in zip(weight,person):
    print(i[0],i[1])

for weight,person in zip(weight,person):
    print(weight,person)

for weight,person in zip(weight,person):
    print("{}: {}".format(weight,person))


"""
 Zip Coordinates

Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points. 
Each string should be formatted as label: x, y, z. 
For example, the string for the first coordinate should be F: 23, 677, 4.
"""

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for i in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {}, {}, {}".format(*i))


for point in points:
    print(point)
    
"""
Zip Lists to a Dictionary
"""
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))
print(cast)

"""
 Unzip Tuples: Unzip the cast tuple into two names and heights tuples
"""
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here

names,heights =zip(*cast)
print(names)
print(heights)

"""
Transpose with Zip: Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
"""
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)