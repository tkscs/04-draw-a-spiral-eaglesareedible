import turtle
from scipy.constants import golden as phi

"""
If the spiral has so far turned degrees_turned_so_far degrees, then the current
arm length will be:

initial_arm_length * (phi**(degrees_turned_so_far / 90))

The aloe polyphylla plant grows in a pattern with five golden spirals
eminating from the same center. Make a function that draws a single golden
spiral, and use that to draw a shape like the aloe polyphylla.

You may find these functions useful:

turtle.up()

turtle.down()

turtle.setposition(x, y)

turtle.setheading(degrees)

The turtle starts at position(0, 0) with heading 0 degrees.
"""
firstArm = 2
degreeCount = 0
firstArm * (phi**(degreeCount / 90))
   
for i in range(150):
    turtle.forward(firstArm * (phi**(degreeCount / 90)))
    degreeCount = degreeCount+5
    turtle.right(5)

turtle.exitonclick()