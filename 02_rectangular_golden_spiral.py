import turtle
from scipy.constants import golden as phi

"""
In a golden spiral, for every 90 degrees, the arm length of the spiral grows
by a factor of phi (which is approximately 1.618)

So if the spiral has so far turned 90 degrees i times, then the current arm
length will be:

initial_arm_length * (phi**i)
"""

### YOUR CODE STARTS HERE
for i in range(1, 50):
    turtle.forward(1.618**i)
    turtle.left(90)

### YOUR CODE ENDS HERE

turtle.exitonclick()