#!/usr/bin/env python
import Image
import ImageDraw
import random

import awsom

try:
    import psyco
    psyco.full()
except ImportError:
    pass

def main():
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
        
    image.save("example.png")

if __name__ == "__main__":
    main()
