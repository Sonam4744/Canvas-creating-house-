import tkinter as tk

# Create the window
root = tk.Tk()
root.title("House with Animals and Moving Clouds")
root.geometry("800x500")

# Create the canvas
canvas = tk.Canvas(root, width=800, height=500, bg="skyblue")
canvas.pack()


# =========================
# MAIN HOUSE
# =========================

# House body - Rectangle
canvas.create_rectangle(
    200, 250, 500, 450,
    fill="lightyellow",
    outline="black",
    width=3
)

# Roof - Triangle
canvas.create_polygon(
    170, 250,
    350, 100,
    530, 250,
    fill="red",
    outline="black",
    width=3
)

# Left window - Square
canvas.create_rectangle(
    240, 290, 300, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window - Square
canvas.create_rectangle(
    400, 290, 460, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Door - Rectangle
canvas.create_rectangle(
    320, 350, 380, 450,
    fill="brown",
    outline="black",
    width=3
)


# =========================
# SUN - LEFT SIDE
# =========================

canvas.create_oval(
    50, 60, 130, 140,
    fill="yellow",
    outline="orange",
    width=3
)

# Sun rays
canvas.create_line(90, 40, 90, 60, fill="orange", width=3)
canvas.create_line(90, 140, 90, 160, fill="orange", width=3)
canvas.create_line(30, 100, 50, 100, fill="orange", width=3)
canvas.create_line(130, 100, 150, 100, fill="orange", width=3)
canvas.create_line(45, 55, 60, 70, fill="orange", width=3)
canvas.create_line(120, 130, 135, 145, fill="orange", width=3)
canvas.create_line(120, 70, 135, 55, fill="orange", width=3)
canvas.create_line(45, 145, 60, 130, fill="orange", width=3)


# =========================
# SMALL DOG HOUSE
# =========================

canvas.create_rectangle(
    600, 390, 700, 450,
    fill="burlywood",
    outline="black",
    width=3
)

# Dog house roof
canvas.create_polygon(
    585, 390,
    650, 335,
    715, 390,
    fill="brown",
    outline="black",
    width=3
)

# Dog house entrance
canvas.create_rectangle(
    630, 410, 670, 450,
    fill="black",
    outline="black",
    width=2
)


# =========================
# DOG
# =========================

# Dog body
canvas.create_oval(
    530, 405, 590, 440,
    fill="tan",
    outline="black"
)

# Dog head
canvas.create_oval(
    520, 375, 565, 415,
    fill="tan",
    outline="black"
)

# Dog ears
canvas.create_polygon(
    525, 380, 510, 365, 535, 375,
    fill="brown",
    outline="black"
)

canvas.create_polygon(
    550, 375, 570, 365, 560, 395,
    fill="brown",
    outline="black"
)

# Dog eyes
canvas.create_oval(532, 388, 537, 393, fill="black")
canvas.create_oval(550, 388, 555, 393, fill="black")

# Dog nose
canvas.create_oval(540, 398, 548, 405, fill="black")

# Dog tail
canvas.create_line(
    585, 415, 605, 400,
    fill="brown",
    width=5
)


# =========================
# CAT 1
# =========================

# Cat body
canvas.create_oval(
    120, 400, 170, 445,
    fill="gray",
    outline="black"
)

# Cat head
canvas.create_oval(
    115, 370, 160, 410,
    fill="gray",
    outline="black"
)

# Cat ears
canvas.create_polygon(
    118, 375, 120, 355, 135, 372,
    fill="gray",
    outline="black"
)

canvas.create_polygon(
    140, 372, 155, 355, 158, 378,
    fill="gray",
    outline="black"
)

# Cat eyes
canvas.create_oval(127, 385, 132, 390, fill="green")
canvas.create_oval(145, 385, 150, 390, fill="green")

# Cat nose
canvas.create_oval(136, 394, 142, 399, fill="pink")

# Cat tail
canvas.create_line(
    165, 415, 185, 395,
    fill="gray",
    width=5
)


# =========================
# CAT 2
# =========================

# Cat body
canvas.create_oval(
    430, 410, 480, 450,
    fill="orange",
    outline="black"
)

# Cat head
canvas.create_oval(
    425, 380, 470, 420,
    fill="orange",
    outline="black"
)

# Cat ears
canvas.create_polygon(
    428, 385, 430, 365, 445, 380,
    fill="orange",
    outline="black"
)

canvas.create_polygon(
    450, 380, 465, 365, 468, 388,
    fill="orange",
    outline="black"
)

# Cat eyes
canvas.create_oval(437, 393, 442, 398, fill="green")
canvas.create_oval(453, 393, 458, 398, fill="green")

# Cat nose
canvas.create_oval(445, 402, 451, 407, fill="pink")

# Cat tail
canvas.create_line(
    475, 420, 495, 400,
    fill="orange",
    width=5
)


# =========================
# MOVING CLOUDS
# =========================

# Cloud 1
cloud1 = [
    canvas.create_oval(180, 50, 230, 90, fill="white", outline="white"),
    canvas.create_oval(210, 35, 270, 90, fill="white", outline="white"),
    canvas.create_oval(250, 50, 300, 90, fill="white", outline="white"),
    canvas.create_rectangle(180, 65, 300, 90, fill="white", outline="white")
]

# Cloud 2
cloud2 = [
    canvas.create_oval(500, 80, 550, 120, fill="white", outline="white"),
    canvas.create_oval(530, 60, 590, 120, fill="white", outline="white"),
    canvas.create_oval(570, 80, 620, 120, fill="white", outline="white"),
    canvas.create_rectangle(500, 95, 620, 120, fill="white", outline="white")
]


# =========================
# MOVE CLOUDS
# =========================

def move_cloud(cloud, speed):
    for part in cloud:
        canvas.move(part, speed, 0)

    # Get the position of the first part
    x1, y1, x2, y2 = canvas.coords(cloud[0])

    # If cloud goes outside the right side,
    # move it back to the left
    if x1 > 800:
        for part in cloud:
            canvas.move(part, -900, 0)

    root.after(50, lambda: move_cloud(cloud, speed))


# Start cloud movement
move_cloud(cloud1, 2)
move_cloud(cloud2, 1.5)


# =========================
# GROUND
# =========================

canvas.create_rectangle(
    0, 450, 800, 500,
    fill="lightgreen",
    outline="green"
)


# Run the program
root.mainloop()