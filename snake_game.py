from tkinter import *
import random

# variables that we are not going to change(constants)
GAME_WIDTH = 700
GAME_HEIGHT = 700
# the lower the number in speed the fastest the game
SPEED = 200
SPACE_SIZE = 25
# how many parts the snake will have initially
BODY_PARTS = 4
SNAKE_COLOR = "#00FF00"  # green
FOOD_COLOR = "#FF0000"  # red
BACKGROUND_COLOR = "#000000"  # black

# state varibles that can change
score = 0
direction = "down"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
            # our snake will appear in the top left coordinates

        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


# use the __init__ method everytime you create an object inside a class
# place our food object randomly
# there is a given amount of spaces. 700/50 = 14 posible spots on the x axis and also 14 on the y axes
# we also need to draw our food object in our canvas
class Food:
    def __init__(self):
        x = random.uniform(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.uniform(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )


def next_turn(snake, food):
    x, y = snake.coordinates[0]  # head of the snake
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )
    snake.squares.insert(0, square)

    # increment the score if the snake head position and the food position are the same
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score: {}".format(score))
        # delete the food objetc
        canvas.delete("food")
        # create a new food object
        food = Food()
    else:
        # delete the last body part of the snake
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction == new_direction
    elif new_direction == "right":
        if direction != "left":
            direction == new_direction
    elif new_direction == "up":
        if direction != "down":
            direction == new_direction
    elif new_direction == "down":
        if direction != "up":
            direction == new_direction


def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

        return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
    )


# make the window with the imported Tk
window = Tk()
window.title("Snake Game")
# whether do you want the window to change sizes or not
window.resizable(False, False)

# .format() will be useful if we are creating dynamic text(the score in this case)
# the {} curly braces will be substituted with the argument inside format(..)
label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

# create the canvas to show the game board
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# center the window when it appears
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("700x700")

# create snake and food objects
snake = Snake()
food = Food()

# controls for our snake

window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))


next_turn(snake, food)


# display the window
window.mainloop()
