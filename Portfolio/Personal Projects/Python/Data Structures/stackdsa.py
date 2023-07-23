class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, input):
        self.items.append(input)

    def pop(self):
        return self.items.pop()
    
    def check_stack(self):
        print(self.items)
    
s = stack()
while True:
    option = input("What would you like to do? (check stack, push, pop, or quit): ")
    if option == 'check stack':
        if s.is_empty():
            print("Stack is empty.")
        else:
            s.check_stack()
    elif option == 'push':
        num = input("What would you like to push?: ")
        s.push(num)
    elif option == 'pop':
        if s.is_empty():
            print("Stack is empty.")
        else:
            s.pop()
    elif option == 'exit':
        break
    else:
        print("Error. Invalid action.")