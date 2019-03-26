'''
Sorted inventories should be just that: sorted.
Right now, we just add an item onto the slots list whenever our add_item method is called.
Use the list.sort() method to make sure the slots list gets sorted after an item is added.
Only do this in the SortedInventory class.
'''


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)

class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.list1 = self.slots[:]
        self.list1.sort()
        print(self.list1)
        print(self.slots)
