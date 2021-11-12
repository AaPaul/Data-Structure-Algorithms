class Node:
    def __init__(self, key, value, isActive, children=[]):
        self.key = key
        self.value = value
        self.isActive = isActive
        self.children = children
    
    def equals(self, node) -> bool:
        if (node == None):
            return False

        return (self.key == node.key 
                and self.value == node.value
                and self.isActive == node.isActive)
             
    
    def toString(self):
        return self.key
    
def getModifiedItems(oldMenu: Node, newMenu: Node):
    if oldMenu == None and newMenu == None:
        return 0
    
    count = 0

    if oldMenu == None or newMenu == None or (not oldMenu.equals(newMenu)):
        print(oldMenu + " " + newMenu)
        count += 1
    
    children1 = getChildNodes(oldMenu)
    children2 = getChildNodes(newMenu)

    for key, _ in children1.items():
        count += getModifiedItems(children1.get(key), children2.get(key, None))
    
    for key, _ in children2.items():
        if not children1.get(key):
            count += getModifiedItems(None, children2.get(key))

    return count

def getChildNodes(menu: Node):
    _map = {}
    if (menu == None):
        return _map
    
    for i in menu.children:
        _map[i.key] = i
    
    return _map

if __name__ == "__main__":
    a = Node("a", 1, True)
    b = Node("b", 2, True)
    c = Node("c", 3, True)
    d = Node("d", 4, True)
    e = Node("e", 5, True)
    g = Node("g", 7, True)

    a.children.append(b)
    a.children.append(c)

    b.children.append(d)
    b.children.append(e)

    a1 = Node("a", 1, True)
    b1 = Node("b", 2, True)
    c1 = Node("c", 3, True)
    d1 = Node("d", 4, True)
    e1 = Node("e", 5, True)
    f1 = Node("f", 6, True)
    g1 = Node("g", 7, True)

    a1.children.append(b1)
    a1.children.append(c1)

    b1.children.append(d1)

    c1.children.append(e1)

    count =getModifiedItems(a, a1)
    print(count)