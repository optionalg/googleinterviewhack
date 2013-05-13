import sys



def isSubString(a,b):
    return a.find(b) != -1


def isSubstr(a,b):    
    for i in range(0,len(a)):
        found = True
        for j in range(0,len(b)):
            if a[i+j] != b[j]:
                found = False
                break
        if found:            
            return found
    return False



#might move remove method out, and have a head point to the head node
#when the head node removed, point to the second one
class DoubleLinkedList(object):
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next

    def remove(self, value):
        if self.value == value:
            if self.next:
                self.next.pre = self.pre
            if self.pre:
                self.pre.next = self.next
            return value
        else:
            self.next.remove(value) 


l1 = DoubleLinkedList(1)
l2 = DoubleLinkedList(2, pre=l1)
l3 = DoubleLinkedList(3, pre=l2)
l1.next = l2
l2.next = l3

   


def validateBST(btree):
    #in btree, a node is represented with a list of length 3, the first for the value,
    #the second for the left child, the third for the right child
    #if btree[1][0] > btree[0] or btree[2][0] < btree[0]:
    #    return False
    #valideBST(btree[1])
    #valideBST(btree[2])
    
    return validateHelper(btree, sys.maxint, -sys.maxint-1)
    



def validateHelper(node, maxvalue, minvalue):
    if  node[0] > maxvalue:
        return False
    elif node[1] and not validateHelper(node[1], node[0], minvalue):
        return False

   
    if  node[0] < minvalue :
        return False
    elif node[2] and not validateHelper(node[2], maxvalue, node[0]):
        return False
    
    return True



def oddManOut(l):
    ht = set()
    summ = 0
    for item in l:
       if item in ht:
           summ -= item
       else:
           ht.add(item)
           summ += item
 
    return summ


def oddManOut2(l):
    r = l[0]
    for item in l[1:]:
        r ^=item
    return r





class Stack(object):
   
   def __init__(self):
       self.items = [] 
   
   def push(self,item):
       self.items.append(item)

   def pop(self):
       return self.items.pop()

   def isEmpty(self):
       if self.items:
           return False
       else:
           return True 

   def top(self):
       return self.items[-1]


class PowerStack(object):
    def __init__(self):
        self.stack = Stack()
        self.helpStack = Stack() 
        self.min = None
        self.minStack = Stack()
   
    def findMin(self):
        while (not self.stack.isEmpty()):
            item = self.stack.pop()
            self.helpStack.push(item)
            if self.min == None:
                self.min = item
            elif item < self.min:            
                self.min = item
        while  (not self.helpStack.isEmpty()):    
            self.stack.push(self.helpStack.pop())
        return self.min 


    def findMin2(self):
        return self.minStack.top()

    def push(self,item):
         self.stack.push(item)
         if self.minStack.isEmpty() or item < self.minStack.top():
             self.minStack.push(item) 
  
    def pop(self):
         item = self.stack.pop()
         if item == self.minStack.top():
             self.minStack.pop()
         return item


ps = PowerStack()
ps.push(6)
ps.push(3)
ps.push(6)
ps.push(8)
ps.push(1)
ps.push(9)
ps.push(0)
ps.push(5)

         
  


class Queue(object):
    def __init__(self):
        self.stack = Stack()
        self.helpStack = Stack() 

    def enqueue(self, value):
        self.stack.push(value)
        

    def dequeue(self):
        while (not self.stack.isEmpty()):
            self.helpStack.push(self.stack.pop())
        to_be_removed = self.helpStack.pop()
        while  (not self.helpStack.isEmpty()):    
            self.stack.push(self.helpStack.pop())
        return to_be_removed
            
    
def isInStr(a, b):
   current = 0
   for i in range(0,len(b)):
      for j in range(current,len(a)):
          if a[j] == b[i]:
              current = j + 1               
              break
      if j == len(a)-1 and i < len(b)-1:
          return False
      if i = len(b) -1 and j < len(a) -1:
          return True
   return True 
