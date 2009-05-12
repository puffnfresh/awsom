#!/usr/bin/env python
import Tkinter
import Image
import ImageDraw
import ImageTk
import random

import awsom

try:
    import psyco
    psyco.full()
except ImportError:
    pass

def main():
    root = Tkinter.Tk()
    root.title("awsom example")

    root.status = Tkinter.Label(root, text="Generating")
    root.status.pack()

    root.label = Tkinter.Label(root)
    root.label.pack()

    width, height = (50, 50)
    blocksize = 5

    som = awsom.SOM(width, height, 0.05, 12)

    image = Image.new('RGB', (width * blocksize, height * blocksize))
    draw = ImageDraw.Draw(image)

    weights = []
    for x in range(0, width):
        for y in xrange(0, height):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            node = awsom.Node(x, y, [r, g, b])
            som.addnode(node)

    while som.steps < 500:
        inputs = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        som.step(inputs)
        
        for node in som.nodes:
            color = []
            for weight in node.weights:
                color.append(int(weight))
                
            draw.rectangle(
                (
                    node.x * blocksize,
                    node.y * blocksize,
                    ((node.x + 1) * blocksize) - 1,
                    ((node.y + 1) * blocksize) - 1
                ),
                tuple(color)
            )
        
        root.image = ImageTk.PhotoImage(image)
        root.label.configure(image=root.image)
            
        root.update()
        
    root.status.configure(text="Finished")

    Tkinter.mainloop()

if __name__ == "__main__":
    main()
