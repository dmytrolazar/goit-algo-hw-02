from queue import Queue
import random
from time import sleep

queue = Queue()
id = 0

def generate_request():
    global id
    queue.put(id)
    print(f"Надійшла заявка #{id}.")
    id += 1

def process_request():
    if queue.empty():
        print(f"Черга порожня.")
    else:
        request = queue.get()
        print(f"Заявка #{request} оброблена.")

while True:
    f = random.choice([generate_request, process_request])
    f()
    sleep(0.5)
