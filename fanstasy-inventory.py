playerInventory = {'hammer': 1, 'nails': 47, 'fish': 3}
chestLoot = ['screw driver', 'wooden plank', 'shield', 'screw driver']

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k,v in inventory.items():
        print(str(k) + " x " + str(v))
        item_total = item_total + v;
    print("Total items: " + str(item_total))

def addToInventory(inventory, items):
    for item in items:
        if inventory.get(item):
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory

playerInventory = addToInventory(playerInventory, chestLoot)
displayInventory(playerInventory)