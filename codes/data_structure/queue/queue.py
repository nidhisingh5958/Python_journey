myQueue = list()
# each person to be assigned a code as P1, P2, P3,...
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code for insertion in queue :")
enqueue(myQueue,element)
print("person removed from queue is:", dequeue(myQueue))
print('Number of people in the queue is :',size(myQueue))
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
element = input("enter person’s code to enter in queue :")
enqueue(myQueue,element)
print("Now we are going to remove remaining people from the queue")
while not isEmpty(myQueue):
              print("person removed from queue is ",
              dequeue(myQueue))
