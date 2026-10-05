import tkinter as tk

# Create the window
root = tk.Tk()
root.title("Simple House")
root.geometry("600x500")

# Create the canvas
canvas = tk.Canvas(root, width=600, height=500, bg="skyblue")
canvas.pack()

# House body - Rectangle
canvas.create_rectangle(
    150, 250, 450, 450,
    fill="violet",
    outline="black",
    width=3
)

# Roof - Triangle
canvas.create_polygon(
    120, 250,
    300, 100,
    480, 250,
    fill="red",
    outline="black",
    width=3
)

# Left window - Square
canvas.create_rectangle(
    190, 290, 250, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Right window - Square
canvas.create_rectangle(
    350, 290, 410, 350,
    fill="lightblue",
    outline="black",
    width=3
)

# Door - Rectangle
canvas.create_rectangle(
    270, 350, 330, 450,
    fill="brown",
    outline="black",
    width=3
)

# Run the program
root.mainloop()