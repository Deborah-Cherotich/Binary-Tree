class Node:
    def __init__(self, key):
        self.left = None    
        self.right = None   
        self.val = key      

def access_item(root, key):
    if root is None or root.val == key:   
        return root
    if root.val < key:                    
        return access_item(root.right, key)
    return access_item(root.left, key)    

root = Node(5)                 
root.left = Node(3)             
root.right = Node(7)            
root.left.left = Node(2)        
root.right.left = Node(6)       
root.right.right = Node(8)      

key = 4                         
result_node = access_item(root, key)  

if result_node is not None:
    print(f"Found node with value {key}")   
else:
    print(f"Node with value {key} not found")    
