import tkinter as tk

# Create the window
root = tk.Tk()
root.title("House with Dog House and Sun")
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

# Sun circle
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
# SMALL DOG HOUSE - RIGHT SIDE
# =========================

# Dog house body - smaller rectangle
canvas.create_rectangle(
    600, 390, 700, 450,
    fill="burlywood",
    outline="black",
    width=3
)

# Dog house roof - smaller triangle
canvas.create_polygon(
    585, 390,
    650, 335,
    715, 390,
    fill="brown",
    outline="black",
    width=3
)

# Smaller dog house entrance
canvas.create_rectangle(
    630, 410, 670, 450,
    fill="black",
    outline="black",
    width=2
)

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