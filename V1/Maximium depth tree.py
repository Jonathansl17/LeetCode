class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        

class tree:
    def __init__(self):
        self.ROOT = None
        self.contador = 0
        
    def insertar(self,value):
        Nuevo_Nodo = Node(value)
        
        if self.ROOT == None:
            self.ROOT = Nuevo_Nodo
            
        else:
            Nodo_Actual = self.ROOT
            
            while True:
                
                if value < Nodo_Actual.value:
                    if Nodo_Actual.left == None:
                        Nodo_Actual.left = Nuevo_Nodo
                        break
                    
                    else:
                        Nodo_Actual = Nodo_Actual.left
                        
                else:
                    if Nodo_Actual.right == None:
                        Nodo_Actual.right = Nuevo_Nodo
                        break
                    
                    else:
                        Nodo_Actual = Nodo_Actual.right    
                        
    def MaxDepth(self):
      
        return self.maxDepth(self.ROOT)

    def maxDepth(self, nodo):

        if nodo == None:
            return 0

        left_depth = self.maxDepth(nodo.left)
        right_depth = self.maxDepth(nodo.right)
        

        return max(left_depth, right_depth) + 1
    
Binary = tree()

Binary.insertar(15) 
  
Binary.insertar(11)   
Binary.insertar(10)
Binary.insertar(12)

Binary.insertar(18)
Binary.insertar(16)
Binary.insertar(19)

print(Binary.MaxDepth())