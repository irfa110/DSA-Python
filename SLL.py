""" Singly Linked List """

class Node:
    def __init__(self,data,next=None):
        self.data = data 
        self.next = next


class SLL:

    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n 
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            self.start = n
        else:
            head = self.start 
            while head.next:
                head = head.next 
            head.next = n
    def search(self,data):
        temp = self.start 
        while temp:
            if temp.data == data:
                return temp 
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next 
        
    def delete_last(self):
        if not self.is_empty():
            temp = self.start 
            if temp.next is None:
                self.start = None
            else:
                while temp.next.next is not None:
                    temp = temp.next 
                temp.next = None
    
    def delete_item(self,data):
        if not self.is_empty():
            temp = self.start 
            if temp.next is None:
                if temp.data == data:
                    self.start = None 
            else:
                if temp.data == data:
                    self.start = temp.next
                while temp.next is not None:
                    if temp.next.data == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next 
    
    def __iter__(self):
        return SLLIterator(self.start)
    
class SLLIterator:
    def __init__(self,start):
        self.current = start
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.data 
            self.current = self.current.next
            return data
        

#driver Code
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()

for x in mylist:
    print(x,end=' ')

print()