class Queue:
             def __init__(self):
                          self.items = []
             def isEmpty(self):
                          return self.items == []
             def enqueue(self, item):
                          self.items.insert(0,item)
             def dequeue(self):
                          return self.items.pop()
             def size(self):
                          return len(self.items)
q = Queue()
while True:
             print('Press 1 for insert')
             print('Press 2 for delete')
             print('Press 3 for quit')
             do = int(input('What would you like to do'))
             if do == 1:
                          n=int(input("enter a number to push"))
                          q.enqueue(n)
             elif do == 2:
                          if q.isEmpty():
                                       print('Queue is empty.')
                          else:
                                       print('Deleted value: ', q.dequeue())
             elif do == 3:
                          break
