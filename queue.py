class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Cannot dequeue from an empty queue.")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. Cannot peek an empty queue.")

    def is_empty(self):
        return len(self.queue) == 0
