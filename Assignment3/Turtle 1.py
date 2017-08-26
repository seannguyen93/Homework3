from turtle import*
colors = ["red", "blue", "brown", "yellow", "grey"]
speed (-1)
for i in range (3,8):
    pencolor (colors[i-3])
    for x in range (i):
        forward (100)
        left (360/i)
mainloop()