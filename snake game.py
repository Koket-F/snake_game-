from turtle import *
import turtle 
import random
width = 500
Height = 500

food_size= 10

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}



#direction

def go_up():
 global set_direction
 if set_direction!= 'down':
    set_direction = 'up'
def go_down():
 global set_direction
 if set_direction!= 'up':
    set_direction = 'down'
def go_right():
 global set_direction
 if set_direction!= 'left':
    set_direction = 'right'
def go_left():
 global set_direction
 if set_direction!= 'right':
    set_direction = 'left'

def gameloop():
 stamper.clearstamps()
 new_head= snake[-1].copy()
 new_head[0]+= offsets[set_direction][0]
 new_head[1]+= offsets[set_direction][1]
 if new_head in snake or new_head[0]<-width/2 or new_head[0]> width/2 or new_head[1]<-Height/2 or new_head[1]>Height/2:
   reset()
 else:
  snake.append(new_head)
  if not foodcollision():
   snake.pop(0)
  for segment in snake:
   stamper.goto(segment[0],segment[1])
   stamper.stamp()
  screen.title(f'snakegame.score : {score} highscore:{high_score}')
  level()
  screen.update()
  turtle.ontimer(gameloop,DELAY)
 
def get_foodposition():
  x = random.randint(-width/2+food_size,width/2-food_size)
  y= random.randint(-Height/2+food_size,Height/2-food_size)
  return (x,y)
def reset():
  global score,snake,set_direction, food_pos,DELAY
  DELAY= 400
  score=0
  snake = [[0,0],[0,20],[0,40],[0,60]]
  set_direction='up' 
  food_pos = get_foodposition()
  food.penup()
  food.goto(food_pos)
  gameloop()
def foodcollision():
  global food_pos,score
  if get_distance(snake[-1],food_pos)<20:
    score+=1
    upgrade_highscore()

    food_pos= get_foodposition()
    food.goto(food_pos)
    return True
  return False
def get_distance(pos1,pos2):
  x1,y1 = pos1
  x2,y2 = pos2
  distance= ((x2-x1)**2 + (y2-y1)**2)**0.5
  return distance 
high_score=0 
try:
    with open("high_score.txt",'r') as file:
      high_score= int(file.read())
except FileNotFoundError:
  pass 
def upgrade_highscore():
  global high_score
  if score> high_score:
    high_score= score
    with open("high_score.txt", 'w') as file:
      file.write(str(high_score))

def level():
  global DELAY
  
  if 5<score<=20:
    DELAY= 200
  if score>20:
    DELAY= 100





screen = turtle.Screen()
screen.setup(width,Height)
screen.title('snake')
screen.bgcolor('pink')
screen.tracer(0)


# event handler 
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")


stamper = turtle.Turtle()
stamper.shape('circle')
stamper.color('blue')
stamper.penup()


food= turtle.Turtle()
food.shape('square')
food.color('red')
food.shapesize(food_size/20)

reset()
done()