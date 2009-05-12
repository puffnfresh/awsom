#!/usr/bin/env python
import math
import random

class Node:
    def __init__(self, x, y, weights):
        self.x = x
        self.y = y

        self.weights = weights

class SOM:
    def __init__(self, width, height, rate, curve):
        self.width = width
        self.height = height
        self.rate = rate
        self.curve = curve

        self.steps = 0
        self.nodes = []

        self.length = None

    def addnode(self, node):
        if self.length is None:
            self.length = len(node.weights)
        elif len(node.weights) != self.length:
            # We can't mix nodes with a difference number of weights
            return
        
        self.nodes.append(node)

    def step(self, inputs):
        self.steps += 1

        best = None
        for node in self.nodes:
            distance = 0

            for i in range(len(inputs)):
                distance += (inputs[i] - node.weights[i]) ** 2

            if not best or distance < best[0]:
                best = (distance, node)

        for i in range(len(self.nodes)):
            node = self.nodes[i]
            xdiff = best[1].x - node.x
            ydiff = best[1].y - node.y
            distance = math.sqrt(xdiff ** 2 + ydiff ** 2)

            difference = math.exp(-(distance ** 2) / (2 * self.curve ** 2))

            weights = self.nodes[i].weights
                
            for j in range(len(weights)):
                closeness = inputs[j] - weights[j]
                weights[j] += difference * self.rate * closeness

            self.nodes[i].weights = weights
