# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# visit, left, right
def preorder(self, root):
    if root is None:
        return []
    
    stack = [root]
    output = []
    
    # loop while there are elements in stack
    while stack:
        
        #pop the last element from the stack and store it into temp.
        temp = stack.pop()
        
        # append. the value of temp to output. this is the visit function.
        output.append(temp.val)
        
        # add the children of the temp into the stack in reverse order. 
        # reverse order because it's left right and not right left.
        # children of 1 = [3,2,4], if not reveresed then 4 will be popped out first from the stack.
        # if reversed then stack = [4,2,3]. Here 3 will pop out first.
        # This continues till the stack is empty.
        stack.extend(temp.children[::-1])
    
    #return the output
    return output360

# recursive
def preorder(root):
    output =[]
    
    def dfs(root, output):
        # If root is none return 
        if root is None:
            return

        # for preorder we first add the root val
        output.append(root.val)

        # Then add all the children to the output
        for child in root.children:
        dfs(child, output)

    # perform dfs on the root and get the output stack
    dfs(root, output)
    
    # return the output of all the nodes.
    return output


    