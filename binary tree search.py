#print all root to leaf paths in binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def printRoute(stack, root):
    # append this node to the path array
    stack.append(root.data)
    if(root.left == None and root.right == None):
        print(' '.join([str(i) for i in stack]))
    else:
        # otherwise try both subtrees
        printRoute(stack, root.left)
        printRoute(stack, root.right)
    stack.pop()

# Driver Code
root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
printRoute([], root)
