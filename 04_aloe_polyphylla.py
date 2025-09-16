import turtle
from scipy.constants import golden as phi

"""
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

### YOUR CODE STARTS HERE
turtle.speed(100)
firstArm = 2
degreeCount = 0
for b in range(36):
    degreeCount = 0
    for i in range(50):
        turtle.forward(firstArm * (phi**(degreeCount / 90)))
        degreeCount = degreeCount+5
        turtle.right(5)
    turtle.up()
    turtle.setposition(0, 0)
    turtle.down()
    turtle.setheading(b*10)

### YOUR CODE ENDS HERE

turtle.exitonclick()