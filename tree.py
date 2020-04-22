from collections import namedtuple
from config import starts, middles, ends
Node = namedtuple("Node", "value type branches")

def gen_tree(t, val):
    if t == None:
        branches = [gen_tree("middle", m) for m in middles]
        return [Node(s, "start", branches) for s in starts]
    elif t == "middle":
        branches = [gen_tree("end", e) for e in ends]
        return Node(val, "middle", branches) 
    elif t == "end":
        return Node(val, "end", None)


results = []
def walk_tree(node, last):
    global results
    if node == None:
        return
    else:
        results.append(last + node.value)
        if node.branches != None:
            for n in node.branches:
                walk_tree(n, last + node.value)
