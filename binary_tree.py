from random import randrange
import numpy as np


def maze_g(n):

    matrix = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            dirs = []
            if i < n:
                dirs.append('E')
            if j < n:
                dirs.append('S')
            if(dirs):
                r_value = int(np.floor(randrange(0, len(dirs))))
                matrix[i][j] = dirs[r_value]

    return matrix


def print_matrix(matrix):
    n = len(matrix[0])
    print('___'*(n+1))

    for x in range(n):
        strin = ['|']
        for y in range(n):

            if(matrix[x][y] == 'E'):
                strin.append('___')
            else:
                strin.append('  |')
        if(strin[-1] == '-'):
            strin.append('|')
            print(''.join(strin))

        else:
            strin.append('  |')
            print(''.join(strin))

    print('|__', '___'*(n-1), '_|')


mat = maze_g(10)

for i in range(10):
    print(mat[i])
print_matrix(mat)


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
