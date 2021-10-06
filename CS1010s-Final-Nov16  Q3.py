'''
Question 3: Travel Woes [30 marks]
Suppose we are given a bunch of cities, and the cost to travel between certain pairs of cities. We
can model the routes pictorially, for example:
A B
C D
5
6
4
2
7
The figure above shows 4 cities connected by links of different costs. Note that there is no direct
link between cities C and B, and we can assume that the cost for each link is the same going both
ways.
We can represent the routes between cities in Python using a nested list of pairs. For example,
the above routes can be stored as the list:
routes = [('A', [('B', 5), ('C', 6), ('D', 4)]),
('B', [('A', 5), ('D', 2)]),
('C', [('D', 7), ('A', 6)]),
('D', [('C', 7), ('B', 2), ('A', 4)])]
Each element of the list is a pair (city, links), where city is the name of the city, and
links is another list of pairs of a city with a direct link and the cost of the link. Note the lists
are unsorted. We shall denote this representation as “list-of-lists”.
Another way of representing the routes is using a “dictionary-of-dictionaries”. For example,
the same routes can be stored as the dictionary:
routes = {"A": {"B": 5, "C": 6, "D": 4},
"B": {"A": 5, "D": 2},
"C": {"A": 6, "D": 7},
"D": {"A": 4, "B": 2, "C": 7}}
The keys are the cities and the values are dictionaries which keys are the destination city and the
value the cost of the direct link to the city.
The function cost_between which takes as inputs the routes (in either one of the above representations), a source city (which is a string) and a destination city (which is a string). The
function outputs the cost of the direct link from the source to the destination city. If no direct
link exists, a NoRouteException is raised.
Example:
>>> cost_between(routes, 'A', 'B')
5
>>> cost_between(routes, 'C', 'B')
NoRouteException
8

A. Provide an implementation of the function cost_between which takes in the list-of-lists
representation of routes. and state the order of growth in terms of time for the function. You
may assume NoRouteException has been defined.
'''

routes = [('A', [('B', 5), ('C', 6), ('D', 4)]),
('B', [('A', 5), ('D', 2)]),
('C', [('D', 7), ('A', 6)]),
('D', [('C', 7), ('B', 2), ('A', 4)])]


def cost_between(r,s,d):
    for x,y in r:
        if x == s and y[0][0] == d:
            return y[0][1]
    print("Error")

print(cost_between(routes,'A','B'))



'''
B. Provide an implementation of the function cost_between which takes in the dictionaryof-dictionaries representation of routes, and state the order of growth in terms of time for the
function. [5 marks]
'''

routes1 = {"A": {"B": 5, "C": 6, "D": 4},
"B": {"A": 5, "D": 2},
"C": {"A": 6, "D": 7},
"D": {"A": 4, "B": 2, "C": 7}}

def cost_between(r, s, d):
    if d in r[s]:
        return r[s][d]
    else:
        print("Error")

print(cost_between(routes1,'A','B'))


'''
For the rest of this question, assume a dictionary-of-dictionaries representation is used for
the routes.
D. The function add_city takes as inputs the routes, and a pair (city, links) where city
is a new city and links is a sequence of pairs of an existing city and cost. The function updates
routes with the new city and the respective cost to the existing cities found in links.
Example:
>>> cost_between(routes, "A", "E")
NoRouteException
>>> add_city(routes, ("E", (("A", 3), ("D", 8))))
>>> cost_between(routes, "A", "E")
3
'''

def add_city(routes,tup):
    if tup[0] not in routes:
        routes[tup[0]] = {}
    for city,cost in tup[1]:
            routes[city][tup[0]] = cost
            routes[tup[0]][city] = cost
from pprint import pprint
pprint(routes1)
print("\n")
add_city(routes1, ("E", (("A", 3), ("D", 8))))
pprint(routes1)

