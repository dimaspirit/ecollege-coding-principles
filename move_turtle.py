import turtle

screenR = turtle.Screen()
pointer = turtle.Turtle()

# color: green / black 

def movePointer(direction):
  distance = 200

  if(direction == 'up'):
    pointer.sety(pointer.ycor() + distance)
  elif (direction == 'down'):
    pointer.sety(pointer.ycor() - distance)
  elif (direction == 'right'):
    pointer.forward(distance)
  elif (direction == 'left'):
    pointer.back(distance)

def drawRectangle():
  pointer.pendown()

  pointer.pencolor('green')
  movePointer('right')
  pointer.pencolor('black')
  movePointer('down')
  pointer.pencolor('green')
  movePointer('left')
  movePointer('up')

turtle.ontimer(drawRectangle, 6000)

turtle.mainloop()