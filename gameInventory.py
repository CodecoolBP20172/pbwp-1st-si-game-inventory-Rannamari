# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
# Displays the inventory.
from collections import Counter
import csv

def display_inventory(inventory):
    display_inventorySort = sorted(inventory.items(), key=lambda x: x[1])
    print("Inventory:")
    for k, v in display_inventorySort:
        print (v, k)
    print ("The total number of items: " + str(sum(inventory.values())))
    return inventory
    pass


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(inv)


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    a = Counter(added_items)
    b = Counter(inventory)
    c = dict(a + b)
    inventory.update(c)
    return inventory
    pass


dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    n = len(max(inventory, key=len))
    if order is None:
        s = inventory.items()
    elif order == "count,asc":
        s = sorted(inventory.items(), key=lambda x: x[1])
    elif order == "count,desc":
        s = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    print("Inventory:")
    print("count".rjust(n + 1), "item name".rjust(n + 1))
    print("-"*(n + 1)*2)
    for k, v in s:
        k = str(k)
        v = str(v)
        print (v.rjust(n + 1), k.rjust(n + 1))
    print("-"*(n + 1)*2)
    print ("The total number of items: " + str(sum(inventory.values())))
    return inventory
    pass


print_table(inv, order=None)
# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inventory, filename="import_inventory.csv"):
    with open(filename) as invFile:
        invReader = csv.reader(invFile)
        inv_list = []
        for row in invReader:
            if len(row) != 0:
                inv_list += row
    d = Counter(inv_list)
    e = Counter(inventory)
    f = dict(d + e)
    inventory.update(f)
    return inventory
    pass


import_inventory(inv, "import_inventory.csv")
print_table(inv, "count,desc")
# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inventory, filename="export_inventory.csv"):
    c = Counter(inventory)
    c = sorted(c.elements())
    with open(filename, "w") as invFile:
        invWriter = csv.writer(invFile)
        invWriter.writerow(c)
        pass


export_inventory(inv, "export_inventory.csv")
