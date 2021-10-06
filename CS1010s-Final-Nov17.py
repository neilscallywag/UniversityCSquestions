'''
Connect Four is a two-player game played using a vertically suspended grid. Players take turns
dropping their tokens into a column of the grid. The tokens will fall straight down, occupying
the bottom-most available row of the column. For example, in the figure below, a token dropped
into the third column from the left will end up on the third row from the bottom.
Figure 1: An example midway into a Connect Four game.
A player wins the game if they are the first to form a continuous horizontal, vertical or diagonal
line of at least four of their own tokens.
We can represent the game state of a Connect Four game in Python using a list of lists. Each
element of the list represents a row of the grid, which is a list of elements. An empty spot on the
grid can be represented by None , and a player’s token can be a string or integer. For example,
one player might use the string "P1" and the other might use the integer 42 as their tokens.
You may assume the two players will not use the same value as their tokens.
A. [Warm up] The function make_grid takes as inputs the number of rows and columns of
a playing grid, and returns an empty grid of the given size, represented as a list of lists as stated
above. Provide an implementation for make_grid .

'''

def make_grid(rows,col):
    return [[None for i in range(col)] for j in range(rows)]


m = make_grid(10,5)
from pprint import pprint
pprint(m)
print(m)

def rows(m):
    return print(len(m[0]))
def cols(m):
    return print(len(m))
def get(m,row,col):
    z = []
    for y in range(col,len(m)):
        for x in range(row,len(m[y])):
            m[y[x]]
    return z[0]

rows(m)
cols(m)

r =[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
 [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
 [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
 [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]]
print(get(r,2,2))

        
    
