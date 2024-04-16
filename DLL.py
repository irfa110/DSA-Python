""" Double link list """

# Create Node 
class Node:
    def __init__(self,prev=None, data=None ,next=None):
        self.data = data 
        self.prev = prev 
        self.next = next
        

class DLL:

    def __init__(self):
        self.start = None 
    
    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n 
        self.start = n 

    def insert_at_last(self, data):
        n = Node(None,data,None)
        if not self.is_empty():
            temp = self.start 
            while temp.next is not None:
                temp = temp.next
            temp.next = n 
            temp.next.prev = temp 
        else:
            self.start = n
    
    def search(self,item):
        temp = self.start 
        if self.is_empty():
            return 
        while temp is not None:
            if temp.data == item:
                return temp 
            temp = temp.next

    def insert_after(self,item,data):
        if item is not None:
            n = Node(item,data,item.next)
            if item.next is not None:
                item.next.prev = n
            item.next = n

    def print_list(self):
        temp = self.start 
        while temp:
            print(temp.data, end=' ')
            temp = temp.next 
        
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
                self.start = None
        else:
            temp = self.start 
            while temp.next is not None:
                temp = temp.next 
            temp.prev.next = None
        
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next  
    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:

    def __init__(self,start):
        self.current = start 
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        
        data = self.current.data 
        self.current = self.current.next 
        return data


# dll = DLL()
# dll.insert_at_start(10)
# dll.insert_at_start(20)
# dll.insert_at_last(30)
# dll.print_list()

mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10),15)
for x in mylist:
    print(x,end=' ')
print()
print('-----------------------')
mylist.print_list()