import turtle
import random
import sys
from GetRandomStevenHeSlogan import randomSlogan

# Konstanten für Fenstergröße, Essensgröße, delay, Anzahl versuche, Tasten und Ab welcher Punktzahl erweitert wird
w = 500
h = 500
food_size = 10
food_border_distance = food_size * 5
delay = 100
count = 0
keys = ["Up", "Right", "Down", "Left"]
expand = [75, 200]

# Konstante, die die relative Verschiebung in die 4 Richtungen zeigen
offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

# Beendet das Programm
def shutdown():
    score = len(snake)
    print("Your score is {}".format(score))
    sys.exit(randomSlogan())

# Aufbau des UI
def reset():
    global snake, snake_dir, food_position, pen, count, score
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snake_dir = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    score_tu.write(len(snake))
    if count == 0:
        move_snake()
        count = 1
    else:
        shutdown()

# Bewegt die Snake durch Löschen des Letzten Pixels und lones des "Kopfes" wie in offsets angegeben
def move_snake():
    global snake_dir, score, w, h

    stop_listen()

    new_head = snake[-1].copy()
    new_head[0] = snake[-1][0] + offsets[snake_dir][0]
    new_head[1] = snake[-1][1] + offsets[snake_dir][1]
     
    listen()

    if new_head in snake[:-1]:
        score = len(snake) - 1
        shutdown()
    else:
        snake.append(new_head)

        if expand.count(len(snake) - 1) == 1:
            score = len(snake) - 1
            if score == expand[0]:
                w = 1000
                h = 500
            elif score == expand[1]:
                w = 1500
                h = 750
            turtle.setup(w, h)
            score_tu.goto(w / 2 - 50, h / 2 - 50)

        if not food_collision():
            snake.pop(0)
 
        if snake[-1][0] > w / 2:
#            snake[-1][0] -= w
            shutdown()
        elif snake[-1][0] < - w / 2:
#            snake[-1][0] += w
            shutdown()
        elif snake[-1][1] > h / 2:
#            snake[-1][1] -= h
            shutdown()
        elif snake[-1][1] < -h / 2:
#            snake[-1][1] += h
            shutdown()
 
        pen.clearstamps()
        
        for segment in snake:
            pen.goto(segment[0], segment[1])
            pen.stamp()

        score_tu.clear()
        score_tu.write(len(snake), font = 50)

        screen.update()
 
        turtle.ontimer(move_snake, delay)

# Überprüft, ob der "Kopf" das Essen berührt/isst
def food_collision():
    global food_position
    if get_distance(snake[-1], food_position) < 20:
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

# Erzeugt eine neue Position des Essens
def get_random_food_position():
    x = random.randint(- w / 2 + food_border_distance, w / 2 - food_border_distance)
    y = random.randint(- h / 2 + food_border_distance, h / 2 - food_border_distance)
    return (x, y)

# Ermittelt die Distanz zwischen zwei Punkten
def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance

# Funktionen des turtle.Screen().onkeypress() moduls
def go_up():
    global snake_dir
    stop_listen()
    if snake_dir != "down":
        snake_dir = "up"
def go_right():
    global snake_dir
    stop_listen()
    if snake_dir != "left":
        snake_dir = "right"
def go_down():
    global snake_dir
    stop_listen()
    if snake_dir!= "up":
        snake_dir = "down"
def go_left():
    global snake_dir
    stop_listen()
    if snake_dir != "right":
        snake_dir = "left"
 
# Definition des Fensters
screen = turtle.Screen()
screen.setup(w, h)
screen.title("Snake")
screen.bgcolor("blue")
screen.setup(500, 500)
screen.tracer(0)

#turtle, die den Score oben rechts in die Ecke schreibt
score_tu = turtle.Turtle()
score_tu.hideturtle()
score_tu.penup()
score_tu.goto(w / 2 - 50, h / 2 - 50)
score_tu.pendown()
score_tu.color("white")

# turtle Initiierung zum erzeugen der snake
pen = turtle.Turtle("square")
pen.penup()

# Definition der Essens-turtle
food = turtle.Turtle()
food.shape("square")
food.color("yellow")
food.shapesize(food_size / 20)
food.penup()

init_tu = turtle.Turtle()
init_tu.hideturtle()
init_tu.penup()
init_tu.goto(-200, 0)
init_tu.pendown()

# Init des turtle.Screen().onkeypress() moduls
def listen_1(): 
    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_right, "Right")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")
    if count == 0:
        init_tu.clear()
        reset()

def stop_listen():
    screen.listen()
    screen.onkeypress(None, "Up")
    screen.onkeypress(None, "Right")
    screen.onkeypress(None, "Down")
    screen.onkeypress(None, "Left")

def listen():
    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_right, "Right")
    screen.onkeypress(go_down, "Down")
    screen.onkeypress(go_left, "Left")

# wartet auf einen Tastendruck, um das Programm zu starten
screen.listen()
for myKey in keys:
    screen.onkeypress(listen_1, myKey)

init_tu.write("Press arrow key to start", font = 50)

turtle.done()
