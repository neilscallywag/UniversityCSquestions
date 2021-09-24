'''
Problem 2 Sequences (26 marks)
At the Happy Magic School, Harry manages the inventory of magical items used in class for all
the Year 1 students – the wands, the potions, and the spells. He has to make sure that all the
magical items are in good condition, and sends them for repair or replacement when necessary.
The status of a magical item (i.e., a wand, a potion, or a spell) is represented by a tuple of two
integers: (m, n), where m is the identity of the magical item (e.g., wand_1, wand_2, potion_1,
potion_5, spell_2, spell_5, etc.), and n is the number of remaining charges (i.e., how many times
the wand can be “fired”, or the spell can be “cast”, etc.).
Curiously, the charges of a magical item can be a negative number: – 1 – this means that the item
was “overused” once, and needs to be repaired or recharged immediately. Otherwise, if the
overused magical item is used again, the item will vanish forever!
Harry’s inventory lists are implemented as Python lists as follows:
wands = [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)]
potions = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), (6, 6), (7, 7), (8, 8)]
spells = [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]
You DO NOT have to worry about data abstraction for this problem, and can work on the
sequences directly.
a) Help Harry define a function check_charges to display the charges of the magical items,
omitting the item identities, on any inventory list. The function takes in an inventory list and
returns a new list showing only the charges (without the identities). An example run is shown
below: [5 marks]
'''
wands = [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)]
potions = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), (6, 6), (7, 7), (8, 8)]
spells = [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]
def check_charges(seq):
    return [x[1] for x in seq]
print(check_charges(spells))


'''
b) Help Harry define a function charge_5 to add 5 charges to each magical item (in any
inventory list) with fewer than 2 current charges. The function takes in an inventory list and
returns a new list showing only the updated charges (without the identities). An example run is
shown below: [5 marks]
>>> charge_5(wands)
[6, 2, 3, 4, 5]
'''
def charge_5(seq):
    charges = check_charges(seq)
    for index,charge in enumerate(charges):
        if charge < 2:
            charges[index] = charge+5
    return charges
print(charge_5(wands))

'''
c) Help Harry write a function find_bad_items that will identify all the magical items in an
inventory list that need repair or recharge right away, i.e., those with charges: – 1. The
function takes in an inventory list and returns a list of the bad items. An example run is shown
below: [6 marks]
>>> find_bad_items(spells)
[(2, -1), (5, -1)]
'''
def find_bad_items(seq):
    return[x for x in seq if x[1]<0]
print(find_bad_items(spells))

def update_inventory(seq):
    x = input("update by how many charges?")
    L = []
    for index,charge in seq:
        charge += int(x)
        L.append((index,charge))
    return L
'''
Problem 3

Sorting and Abstract Data Types (24 marks)
At the beginning of the summer holidays at the Happy Magic School, Harry’s good friend, Ron is
in-charge of collecting the magical items (i.e., the individual wands, potions, and spells) into a big
magic box and storing it in the vault. Assume that the status of each magical item is again
represented as a tuple of two integers (m, n) where m is the identity of the item, and n is the
number of remaining charges, as defined in Problem 2.
Ron’s inventory lists in a magic box are implemented in a Python dictionary as follows:
m_box = {'wands': [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)],
 'potions': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), \
 (6, 6), (7, 7), (8, 8)],
 'spells': [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]}
a) Help Ron define a function sort_magical_items to sort the magical items in the inventory
lists (i.e., the collections of wands, potions, and spells) according to the number of charges
remaining, in descending order. The function takes in a magic box and sorts the items in the
box accordingly; the function does not need to RETURN anything, but the inventory lists in
the magic box must be updated. You can use any sorting functions as introduced in class for
this question (including the built-in Python sort functions), and can again work directly on the
implementations. State any assumptions you make. An example run (with m_box as defined
above) is shown below: [6 marks]
'''
m_box = {'wands': [(1, 1), (2, 2), (3, 3), (4, -1), (5, 5)],
 'potions': [(1, 1), (2, 1), (3, 1), (4, 1), (5, 5), (6, 6), (7, 7), (8, 8)],
 'spells': [(1, 5), (2, -1), (3, 5), (4, 0), (5, -1)]}

def sort_magical_items(box):
    for key,value in box.items():
        value.sort(key=lambda x:x[1],reverse=True)
        
    return box
print(sort_magical_items(m_box))
