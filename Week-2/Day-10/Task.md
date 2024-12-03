planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
Which planet is closest to the sun? Python uses zero-based indexing, so the first element has index 0.

What's the next closest planet?


Which planet is furthest from the sun?

Elements at the end of the list can be accessed with negative numbers, starting from -1:What are the first three planets? We can answer this question using slicing:

planets[0:3] is our way of asking for the elements of planets starting from index 0 and continuing up to but not including index 3.

The starting and ending indices are both optional. If I leave out the start index, it's assumed to be 0. So I could rewrite the expression above as:

planets[:3]
['Mercury', 'Venus', 'Earth']
If I leave out the end index, it's assumed to be the length of the list.
i.e. the expression above means "give me all the planets from index 3 onward".

We can also use negative indices when slicing:
# All the planets except the first and last
planets[1:-1]
# The last 3 planets
planets[-3:]
Changing lists
Lists are "mutable", meaning they can be modified "in place".

One way to modify a list is to assign to an index or slice expression.

For example, let's say we want to rename Mars:planets[3] = 'Malacandra'
planets
# How many planets are there?
len(planets)
# The planets sorted in alphabetical order
sorted(planets)
# Pluto is a planet darn it!
planets.append('Pluto')
planets.pop()
