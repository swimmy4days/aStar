import pygame
import tkinter as tk


class Node(object):
    """docstring for Node"""

    def __init__(self, parent=None, pos=None, goal=None):
        super(Node, self).__init__()
        self.goal = goal
        self.parent = parent
        self.position = pos
        self.n = 1
        self.f = 0
        self.child = []
        if self.parent:
            self.n = parent.n + 1
        self.f = self.n + self.distance(self, self.goal)

    def __eq__(this, other):
        return int(this.position[0]) == int(other.position[0]) and int(this.position[1]) == int(other.position[1])

    @staticmethod
    def distance(this, goal):
        return ((int(this.position[0])-int(goal[0]))**2)+((int(this.position[1])-int(goal[1]))**2)


def aStar(grid, start, end):
    openedList = []
    closedList = []
    visited = []
    newPos = None
    newNode = None
    path = []

    if start == end:
        print("start = end!")
        return [start.position]
    openedList.append(start)
    visited.append(start.position)
    currentNode = openedList[0]
    openedList.remove(currentNode)
    while True:
        if currentNode == end:
            break
        for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            newPos = [int(currentNode.position[0]) + x, int(currentNode.position[1]) + y]
            if newPos[0] > (len(grid) - 1) or newPos[0] < 0 or newPos[1] > (len(grid[len(grid)-1]) - 1) or newPos[1] < 0:
                continue
            if int(grid[newPos[0]][newPos[1]]) == 1:
                continue

            if newPos not in visited:
                openedList.append(Node(currentNode, newPos, currentNode.goal))
                visited.append(newPos)

        openedList.sort(key=lambda x: x.f)
        if len(openedList) >= 1:
            currentNode = openedList.pop(0)
            closedList.append(currentNode)
        else:
            return -1

    try:
        while True:
            path.append(currentNode.position)
            currentNode = currentNode.parent
    except Exception as e:
        return path[::-1]


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PINK = (255, 20, 147)
BLUE = (0, 0, 255)

GRID_X = 50
GRID_Y = 50

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 3

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_X):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_Y):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# grid[1][5] = 2

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(GRID_X * WIDTH) + (GRID_X * MARGIN) + MARGIN, (GRID_Y * HEIGHT) + (GRID_Y * MARGIN) + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("A* algorithem")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

tkinter = True

mouseState = False

draw = True

run = False
found = False
firstRun = True

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEMOTION and mouseState and draw:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            try:
                if grid[row][column] == 0:
                    grid[row][column] = 1
            except Exception as e:
                pass
            # print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.MOUSEBUTTONDOWN and draw:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if grid[row][column] == 0:
                grid[row][column] = 1
            mouseState = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseState = False
        elif event.type == pygame.KEYDOWN and draw:
            if pygame.key.get_pressed()[32]:
                draw = False
                run = True
    if run:
        end = Node(None, endPos, endPos)
        start = Node(None, startPos, end.position)
        if not steps:
            path = aStar(grid, start, end)
            for node in path:
                grid[int(node[0])][int(node[1])] = 5
            run = False
        else:
            if found:
                try:
                    while True:
                        path.append(currentNode.position)
                        currentNode = currentNode.parent
                except Exception as e:
                    path = path[::-1]
                    for node in path:
                        grid[int(node[0])][int(node[1])] = 5
                    run = False
            else:
                if firstRun:
                    openedList = []
                    closedList = []
                    visited = []
                    newPos = None
                    newNode = None
                    path = []

                    if start == end:
                        print("start = end!")
                        grid[start.position[0]][start.position[1]] = 5
                        found = True
                        run = False
                    openedList.append(start)
                    visited.append(start.position)
                    currentNode = openedList[0]
                    openedList.remove(currentNode)
                    firstRun = False
                if currentNode == end:
                    found = True
                    continue
                draw = True
                for x, y in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    newPos = [int(currentNode.position[0]) + x, int(currentNode.position[1]) + y]
                    if newPos[0] > (len(grid) - 1) or newPos[0] < 0 or newPos[1] > (len(grid[len(grid)-1]) - 1) or newPos[1] < 0:
                        continue
                    if int(grid[newPos[0]][newPos[1]]) == 1:
                        continue

                    if newPos not in visited:
                        grid[newPos[0]][newPos[1]] = 4
                        openedList.append(Node(currentNode, newPos, currentNode.goal))
                        visited.append(newPos)

                openedList.sort(key=lambda x: x.f)
                if len(openedList) >= 1:
                    currentNode = openedList.pop(0)
                    closedList.append(currentNode)
                    grid[int(currentNode.position[0])][int(currentNode.position[1])] = 2
                else:
                    print("ERROR")

    # Set the screen background
    screen.fill(GRAY)

    # Draw the grid
    for row in range(GRID_X):
        for column in range(GRID_Y):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 3:
                color = PINK
            elif grid[row][column] == 4:
                color = GREEN
            elif grid[row][column] == 5:
                color = BLUE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    if tkinter:
        tkinter = False
        master = tk.Tk()
        master.title("A*")
        master.columnconfigure(0, weight=1)
        tk.Label(master, text="start").grid(row=0)
        tk.Label(master, text="dest").grid(row=1)

        startPos = tk.StringVar()
        endPos = tk.StringVar()
        steps = tk.IntVar()

        startPos.set("0, 0")
        endPos.set("5, 5")
        steps.set(0)

        e1 = tk.Entry(master, textvariable=startPos)
        e2 = tk.Entry(master, textvariable=endPos)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        tk.Checkbutton(master, text="Show Steps", variable=steps).grid(row=3, column=1, sticky=tk.W)
        tk.Button(master, text='Go!', command=master.destroy).grid(row=4, column=1, sticky=tk.W, pady=4)

        master.mainloop()
        startPos = startPos.get().split(', ')
        endPos = endPos.get().split(', ')
        steps = steps.get()
        grid[int(startPos[0])][int(startPos[1])] = 3
        grid[int(endPos[0])][int(endPos[1])] = 3

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
