def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, tree.value)
    
def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif target >tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


findClosestValueInBSTHelper(10, 12, 13)

