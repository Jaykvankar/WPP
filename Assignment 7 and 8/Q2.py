class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty")
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def display(self):
        print("Queue:", self.queue)

q = Queue()
while True:
    print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter value to enqueue: "))
        q.enqueue(item)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice, try again.")
