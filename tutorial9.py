class Inventory:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.items = []

    def add(self, name, value):
        self.items.append((name, value))

    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, key):
        return f"{self.items[key][0]} ({self.items[key][1]} gold)"
    
    def __str__(self):
        return f"Inventory '{self.owner_name}': {len(self.items)} items, total {sum([item[1] for item in self.items])} gold"
    
    def __repr__(self):
        return f"Inventory('{self.owner_name}', {len(self.items)} items)"
    
    def __add__(self, other):
        if isinstance(other, Inventory):
            new_inventory = Inventory(self.owner_name)
            item_dict = {}
            for name, value in self.items:
                if name not in item_dict:
                    item_dict[name] = value
                else:
                    item_dict[name] = value
            for name, value in other.items:
                if name not in item_dict:
                    item_dict[name] = value
                else:
                    item_dict[name] = value
            new_inventory.items = [(name, value)for name, value in item_dict.items()]
            return new_inventory
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, Inventory):
            new_inventory = Inventory(self.owner_name)
            item_dict = {}
            for_removal = [name for name, value in other.items]
            for  name, value in self.items:
                if name not in for_removal:
                    item_dict[name] = value
                else:
                    continue
                
            new_inventory.items = [(name, value)for name, value in item_dict.items()]
            return new_inventory
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Inventory):
            return sum([value for _, value in self.items]) == sum([value for _, value in other.items])

    def __gt__(self, other):
        if isinstance(other, Inventory):
            return sum([value for _, value in self.items]) > sum([value for _, value in other.items])

    def __bool__(self):
        return len(self.items) != 0
    

inv1 = Inventory("Hero")
inv1.add("Sword", 50)
inv1.add("Shield", 30)
inv1.add("Potion", 10)

inv2 = Inventory("Merchant")
inv2.add("Shield", 30)
inv2.add("Bow", 40)

print(len(inv1))
print(inv1[0])
print(inv1)
print(repr(inv1))

inv3 = inv1 + inv2
print(len(inv3))

inv4 = inv1 - inv2
print(len(inv4))
print(inv4[0])

print(inv1 > inv2)

inv5 = Inventory("Traveler")
inv5.add("Ring", 20)
inv5.add("Bow", 50)
print(inv2 == inv5)

empty = Inventory("Goblin")
if not empty:
    print("Inventory is empty")