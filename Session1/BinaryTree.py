import random
import pygame

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def add(self, node):
        if node.value > self.value:
            if self.right is None:
                self.right = node
            else:
                self.right.add(node)
        elif node.value < self.value:
            if self.left is None:
                self.left = node
            else:
                self.left.add(node)
    def visit(self,value):
        if self.value == value:
            print("Founded")
        elif value < self.value and self.left is not None:
            self.left.visit(value)
        elif value > self.value and self.right is not None:
            self.right.visit(value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, value):
        n = Node(value)
        if self.root is None:
            self.root = n
        else:
            self.root.add(n)

    def inOrder(self, node):
        if node is None:
            return
        else:
            self.inOrder(node.left)
            print(node.value)
            self.inOrder(node.right)

    def search(self,value):
        self.root.visit(value)
tree = BinaryTree()
for i in range(1,10):
    tree.addNode(random.randint(1,100))
pygame.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Binary Tree")

isLooping = True
while isLooping:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            isLooping = False

            





