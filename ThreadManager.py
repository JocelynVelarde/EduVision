import threading
import queue
import time

class ThreadManager:
    def __init__(self):
        self.threads = []
        self.task_queue = queue.Queue()

    def worker_function(self):
        while True:
            item = self.task_queue.get()

            if item is None:
                break
            print(f"Processing item: {item}")

            self.task_queue.task_done()

    def start_threads(self):

        count_thread = threading.Thread(target=self.count_threads)
        mult_thread = threading.Thread(target=self.multiply_threads)

        self.threads.append(count_thread)
        self.threads.append(mult_thread)

        count_thread.start()
        mult_thread.start()


    def count_threads(self):
        print(f"Count thread")
        for i in range(10):
            print(f"Thread count {i}")
            time.sleep(2)

    def multiply_threads(self):
        for i in range(5):
            print(f"Thread mult {i*10}")
            self.task_queue.put(i)
            time.sleep(3)

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()
        self.task_queue.put(None)
        print("All threads have finished.")