from platform import node
from collections import deque
import math
from CrackingTheCodingInterview.ChapterTwo import LinkedList

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    class Node:
        def __init__(self, value=None, parent=None):
            self.value = value
            self.left_child = None
            self.right_child = None
            self.parent = None
            self.isBalanced = None
            self.isBST = None
        
    def insert(self, value):
        if(self.root == None):
            self.root = self.Node(value)
        else:
            self._insert(value, self.root)
            
    def _insert(self, value, cur_node):
        if(value <= cur_node.value):
            if(cur_node.left_child == None):
                cur_node.left_child = self.Node(value, cur_node)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        else:
            if(cur_node.right_child == None):
                cur_node.right_child = self.Node(value, cur_node)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
                
    def height(self):
        if(self.root != None):
            return self._height(self.root, 0)
        else:
            return 0
        
    def _height(self, cur_node, cur_height):
        if(cur_node == None):
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height) 
        
    def search(self, value):
        if(self.root != None):
            return self._search(self.root, value)
        else:
            return False
        
    def _search(self, cur_node, value):
        if(cur_node.value == value):
            return True
        elif(cur_node.value > value and cur_node.left_child != None):
            return self._search(cur_node.left_child, value)
        elif(cur_node.value < value and cur_node.right_child != None):
            return self._search(cur_node.right_child, value)
        return False
    
    def find(self, value):
        if self.root != None:
            return self._find(self.root, value)
        else:
            return None
        
    def _find(self, cur_node, value):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(cur_node.left_child, value)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(cur_node.right_child, value)
    
    def delete_value(self, value):
        return self.delete_node(self.find(value))
    
    def delete_node(self, node):
        parent_node = node.parent
        num_children = self.num_children(node)
        
        #Case 1: node has no children
        if num_children == 0:
            if parent_node.left_child == node:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        #Case 2: node has a single child
        elif num_children == 1:
            #get the single child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child
            #replace the node to be deleted with its child
            if parent_node.left_child == node:
                parent_node.left_child = child
            else:
                parent_node.right_child = child
                
            #update parent pointer in node
            child.parent = parent_node
            
        #Case 3
        elif num_children == 2:
            #get in-order successor of node to be deleted
            successor = self.min_value_node(node.right_child)
            
            #copy in-order successor's value to node formerly holding value we want to delete
            node.value = successor.value
            
            #delete in-order successor now that its value has been copied
            self.delete_node(successor)
        
    def min_value_node(self, node):
        current = node
        while current.left_child != None:
            current = current.left_child
        return current
    
    def num_children(self, node):
        num_children = 0
        if node.left_child != None:
            num_children+=1
        if node.right_child != None:
            num_children+=1
        return num_children
        
    def inOrderTraversal(self, node):
        if(node is not None):
            self.inOrderTraversal(node.left_child)
            print(node.value)
            self.inOrderTraversal(node.right_child)
            
            
    #4.2
    def minimalTree(self, array):
        array_len = len(array)
        if array_len == 0:
            return
        x = array_len/2
        self.root = self.Node(array[x])
        
        if len(array[0:x]) > 0:
            self.root.left_child = self.Node()
            self.root.left_child.parent = self.root
            self._minimalTree(array[0:x], self.root.left_child)
        if len(array[x+1:array_len]) > 0:
            self.root.right_child = self.Node()
            self.root.right_child.parent = self.root
            self._minimalTree(array[x+1:array_len], self.root.right_child)
    
    def _minimalTree(self, array, root):
        array_len = len(array)
        x = array_len/2
        root.value = array[x]
        
        if len(array[0:x]) > 0:
            root.left_child = self.Node()
            root.left_child.parent = root
            self._minimalTree(array[0:x], root.left_child)
        if len(array[x+1:array_len]) > 0:
            root.right_child = self.Node()
            root.right_child.parent = root
            self._minimalTree(array[x+1:array_len], root.right_child)  
     
    #4.3       
    def listOfDepths(self, root):
        linkedLists = []
        linkedLists.append(LinkedList())
        linkedLists[0].appendToList(root.value)
        self._listOfDepths(root.left_child, 1, linkedLists)
        self._listOfDepths(root.right_child, 1, linkedLists)
        i = 0
        for ll in linkedLists:
            a = ll.returnAsList()
            print('depth: ' + str(i) + 'linked list: ' + str(a))
            i+=1

    def _listOfDepths(self, node, depth, linkedLists):
        if node is not None:
            if depth >= len(linkedLists):
                linkedLists.append(LinkedList())
            linkedLists[depth].appendToList(node.value)
            self._listOfDepths(node.left_child, depth+1, linkedLists)
            self._listOfDepths(node.right_child, depth+1, linkedLists)
            
    def printTree(self, root):
        if(root is not None):
            s = 'node.value:' + str(root.value)
            if root.parent is not None:
                s += '; parent.value: ' + str(root.parent.value)
            if root.left_child is not None:
                s += '; left_child.value ' + str(root.left_child.value)
            if root.right_child is not None:
                s += '; right_child.value ' + str(root.right_child.value)
            print(s)
            self.printTree(root.left_child)
            self.printTree(root.right_child)
            
    #4.4
    def isBalanced(self):
        if self.root == None:
            return None
        self.isBalanced = True
        self._isBalanced(self.root)
        return self.isBalanced
        
    def _isBalanced(self, node):
        if node is None:
            return
        print(str(self._height(node.left_child, 0)) + ' ' + str(self._height(node.right_child, 0)))
        if abs(self._height(node.left_child, 0) - self._height(node.right_child, 0)) > 1:
            self.isBalanced = False
        self._isBalanced(node.left_child)
        self._isBalanced(node.right_child)
        
    def unMinimalTree(self, array):
        array_len = len(array)
        if array_len == 0:
            return
        x = (int)(array_len/4)
        self.root = self.Node(array[x])
        
        if len(array[0:x]) > 0:
            self.root.left_child = self.Node()
            self.root.left_child.parent = self.root
            self._minimalTree(array[0:x], self.root.left_child)
        if len(array[x+1:array_len]) > 0:
            self.root.right_child = self.Node()
            self.root.right_child.parent = self.root
            self._minimalTree(array[x+1:array_len], self.root.right_child)
    
    def _unMinimalTree(self, array, root):
        array_len = len(array)
        x = (int)(array_len/4)
        root.value = array[x]
        
        if len(array[0:x]) > 0:
            root.left_child = self.Node()
            root.left_child.parent = root
            self._minimalTree(array[0:x], root.left_child)
        if len(array[x+1:array_len]) > 0:
            root.right_child = self.Node()
            root.right_child.parent = root
            self._minimalTree(array[x+1:array_len], root.right_child) 
            
    #4.5    
    def validateBST(self): 
        if self.root == None:
            return None
        self.isBST = True
        self._validateBST(self.root)
        return self.isBST
        
    def _validateBST(self, node):
        if node == None:
            return
        if node.left_child is not None:
            if node.left_child.value > node.value:
                self.isBST = False    
            self._validateBST(node.left_child)
        if node.right_child is not None:
            if node.right_child.value < node.value:
                self.isBST = False 
            self._validateBST(node.right_child)
            
    #4.6
    def successor(self, value):
        node = self.find(value)
        if node.right_child is not None:
            return self._leftMostChild(node.right_child)
        else:
            while(node.parent is not None):
                if node.parent.value > value:
                    return node.parent.value
                node = node.parent
            return None
        
    def _leftMostChild(self, node):
        if node.left_child is None:
            return node.value
        else:
            return self._leftMostChild(node.left_child)
        
    #4.8
    def commonAncestor(self, val1, val2):
        node1 = self.find(val1)
        node2 = self.find(val2)
        
        runner = node1
        height1 = 0
        while runner is not self.root:
            runner = runner.parent
            height1+=1
        runner = node2
        height2 = 0
        while runner is not self.root:
            runner = runner.parent
            height2+=1  
            
        offset = abs(height1 - height2)
        
        if height1 >= height2:
            runner1 = node1
            runner2 = node2
        else:
            runner1 = node2
            runner2 = node1
        while offset>0:
            runner1 = runner1.parent
            offset-=1  
        
        while True:
            if runner1 == runner2:
                return runner1
            runner1 = runner1.parent
            runner2 = runner2.parent
            
    #4.9
    def possibleSeqs(self):
        output = [self.root.value]
        
        
        #temp = 
        
    def _nodesAtHeight(self, height):
        if height == 0:
            return self.root
        
        output = []
        
        
        
        
    def _leftMostAtDepth(self, height):
        runner = self.root
        while height > 0:
            if runner.left_child is not None:
                runner = runner.left_child
                height-=1
            else:
                runner = runner.right_child
                height-=1     
        return runner             
        
class DirectedGraph:
    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.adjacency_list = []
            self.visited = False
            
    def __init__(self):
        self.nodes = []
        
    def addVertex(self, value):
        if(not self.findNode(value)):
            self.nodes.append(self.GraphNode(value))
        
    def addEdge(self, value1, value2):
        node1 = self.findNode(value1)
        node2 = self.findNode(value2)
        if node1 == None or node2 == None:
            return
        
        for a in node1.adjacency_list:
            if a.value == value2:
                return
          
        node1.adjacency_list.append(node2)
        
    def printGraph(self):
        sorted_nodes = sorted(self.nodes, key=lambda x:x.value)
        for node in sorted_nodes:
            a = list(n.value for n in node.adjacency_list)
            print(str(node.value) + ": " + str(a))
            
    def findNode(self, value):
        for n in self.nodes:
            if n.value == value:
                return n
        return None
        
    #4.1 O(V+E)
    def depthFirstSearch(self, start_value, value_to_search):
        root = self.findNode(start_value)
        for n in root.adjacency_list:
            if n.value == value_to_search:
                return True
            if not n.visited:
                n.visited = True
                if self.depthFirstSearch(n.value, value_to_search):
                    return True
        return False
            
    #O(V+E)
    def breadthFirstSearch(self, start_value, value_to_search):
        q = Queue()
        root = self.findNode(start_value)
        q.enqueue(root)
        while(not q.isEmpty()):
            node = q.dequeue()
            for n in node.adjacency_list:
                if not n.visited:
                    if n.value == value_to_search:
                        return True
                    n.visited = True
                    q.enqueue(n)
        return False

#4.7
def buildOrder(projects, dependencies):
    g = _buildGraph(projects, dependencies)
    proj = list(projects)
    for v in g.nodes:        
        for a in v.adjacency_list:
            try:
                proj.remove(a.value)
            except ValueError:
                pass
    if len(proj) == 0:
        print('No valid build order.')
        return
    output = []
    for v in proj:
        output.append(v)
    temp = list(output)
    while len(temp)>0:
        for t in temp[:]:
            v = g.findNode(t)
            for a in v.adjacency_list:
                if not a.value in output:
                    output.append(a.value)
                    temp.append(a.value)
            temp.remove(t)
    return output
        
        
def _buildGraph(projects, dependencies):
    g = DirectedGraph()
    for p in projects:
        g.addVertex(p)
    for d in dependencies:
        g.addEdge(d[0], d[1])      
    return g  

class Queue:
    def __init__(self):
        self.items = deque()
        
    def enqueue(self, node):
        self.items.append(node)
    
    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.popleft()
        
    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
        
    def isEmpty(self):
        return not bool(self.items) 
    
    def getQueue(self):
        return self.items 
    
    def inQueue(self, node):
        for n in self.items:
            if n == node:
                return True
        return False
        
def main():
    a = [1,2,3,4,5,6,7,8,9,10]
    bst = BinarySearchTree()
    bst.unMinimalTree(a)
    bst.printTree(bst.root)
    
    print(bst.commonAncestor(3, 10).value)
    #print(bst.find(2))
    #bst.listOfDepths(bst.root)
    #print(bst.successor(10))
    
    #projects = ['a','b','c','d','e','f']
    #dependencies = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
    #print(buildOrder(projects, dependencies))
    
    
    
    
    ''''g = DirectedGraph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.addVertex(6)
    g.addVertex(7)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 4)
    g.addEdge(4, 2)
    g.addEdge(6, 2)
    g.addEdge(6, 3)
    g.addEdge(4, 3)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.printGraph()
    print(g.depthFirstSearch(4, 6))'''
    
    
if __name__ == '__main__':
    main()

