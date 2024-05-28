# class Queue:
#     def __init__(self):
#         self.items=[]

#     def is_empty(self):
#         return len(self.items) == 0

#     def enqueue(self, data):
#         self.items.append(data)

#     def dequeue(self):
#         if not self.is_empty():
#             self.items.pop(0)
#         else:
#             raise IndexError("Queue Underflow")

#     def get_front(self):
#         if not self.is_empty():
#             return self.items[0]
#         else:
#             raise IndexError("Queue Underflow")

#     def get_rear(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("Queue Underflow")

#     def size(self):
#         return len(self.items)


# q1 = Queue()

# try:
#     print(q1.get_front())
# except IndexError as e:
#     print(e.args[0])

# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# q1.enqueue(40)
# q1.enqueue(50)
# print("Front=", q1.get_front(), "Rear=", q1.get_rear())
# try:
#     q1.dequeue()
#     print("Queue has now", q1.size(), "elements")
# except IndexError as e:
#     print(e.args[0])


class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_front(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError("No data in the queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.get_front(),q1.get_rear())
q1.dequeue()
print(q1.get_front(),q1.get_rear())