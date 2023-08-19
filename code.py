class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:")
            for item in self.queue:
                print(item, end=" ")
            print()

if __name__ == '__main__':
    q = Queue()

    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if Empty")
        print("4. Get Size")
        print("5. Print Queue")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter item to enqueue: ")
            q.enqueue(item)
            print(f"{item} enqueued to the queue.")
        elif choice == 2:
            dequeued_item = q.dequeue()
            if dequeued_item is not None:
                print(f"Dequeued item: {dequeued_item}")
            else:
                print("Queue is empty.")
        elif choice == 3:
            if q.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        elif choice == 4:
            print(f"Queue size: {q.size()}")
        elif choice == 5:
            q.print_queue()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
