class Node:
    def __init__(self, data=None):
        self.data = data
        self.previous = None
        self.next = None


class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_at_tail(self, data) -> bool:
        # Write code here
          
        if self.head is None: 
            newNode = Node(data)
            self.head = newNode  
            return
        n = self.head
        while n.next is not None:
            n = n.next
        newNode = Node(data)
        n.next = newNode
        newNode.previous = n  
        return True
           
    def add_at_head(self, data) -> bool:
        newNode = Node(data)
        if(self.head == None):
           self.head = newNode;
           return 
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode
        return True

        
    def add_at_index(self, index, data) -> bool:
         newNode = Node(data)

  
           if(index < 1):
              return False
           elif (index == 1):
              newNode.next = self.head
              self.head.previous = newNode
              self.head = newNode
              return True
           else:    
              temp = self.head
              for i in range(1, index-1):
                 if(temp != None):
                    temp = temp.next   
    
   
              if(temp != None):
                 newNode.next = temp.next
                 newNode.previous = temp
                 temp.next = newNode  
                  if (newNode.next != None):
                     newNode.next.previous = newNode
                  return True
              else:
                  return False

    def get(self, index) -> int:
        # Write code here
        temp = self.head
        found = 0
        i = 0
        if(temp != None):
          while (temp != None):
            i += 1
            if(temp.data == searchValue):
              found += 1
              break
            temp = temp.next
          if(found == 1):
              return True
          else:
              return False
        else:
             return False

    def delete_at_index(self, index) -> bool:
        # Write code here
        if(index < 1):
              print("\nposition should be >= 1.")
        elif (index == 1 and self.head != None):
             nodeToDelete = self.head
             self.head = self.head.next
             nodeToDelete = None
             if (self.head != None):
                self.head.prev = None
        else:    
            temp = self.head
            for i in range(1, index-1):
               if(temp != None):
                  temp = temp.next   
    
    
            if(temp != None and temp.next != None):
               nodeToDelete = temp.next
               temp.next = temp.next.next
               if(temp.next.next != None):
                  temp.next.next.prev = temp.next  
                  nodeToDelete = None 
            else:
                print("\nThe node is already null.")

    def get_previous_next(self, index) -> list:
        # Write code here


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = []
iteration_count = 0

for item in input_data.split(', '):
    inner_list = []
    if item.isnumeric():
        data.append(int(item))
    elif item.startswith('['):
        item = item[1:-1]
        for letter in item.split(','):
            if letter.isnumeric():
                inner_list.append(int(letter))
        data.append(inner_list)

obj = DoublyCircularLinkedList()
result = []
for i in range(len(operations)):
    if operations[i] == "add_at_head":
        result.append(obj.add_at_head(data[i]))
    elif operations[i] == "add_at_tail":
        result.append(obj.add_at_tail(data[i]))
    elif operations[i] == "add_at_index":
        result.append(obj.add_at_index(int(data[i][0]), data[i][1]))
    elif operations[i] == "get":
        result.append(obj.get(data[i]))
    elif operations[i] == "get_previous_next":
        result.append(obj.get_previous_next(data[i]))
    elif operations[i] == 'delete_at_index':
        result.append(obj.delete_at_index(data[i]))

print(result)
