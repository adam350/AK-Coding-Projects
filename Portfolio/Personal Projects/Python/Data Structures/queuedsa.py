class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)
    
    def check_queue(self):
        print(self.items)

q = queue()
while True:
    option = input("What would you like to do? (check queue, enqueue, dequeue or exit): ")
    if option == 'exit':
        break
    else:
        if option == 'check queue':
            if q.is_empty():
                print("Queue is empty.")
            else:
                q.check_queue()
        elif option == 'enqueue':
            num = input("What would you like to enqueue? ")
            q.enqueue(num)
        elif option == 'dequeue':
            q.dequeue()
        