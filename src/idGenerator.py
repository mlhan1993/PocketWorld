import time
from threading import Lock
import random
import string


class IDGenerator:

    def __init__(self, server_id):
        self.lock = Lock()
        self.counter = 0
        self.server_id = hex(server_id)
        self.cache = set()
        self.cache_size = 5000

    def get_key(self, size=12):
        self.lock.acquire()
        self.counter += 1
        curtime = time.time()
        random.seed((self.counter, self.server_id, curtime))

        def rand_str():
            return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

        random_string = rand_str()

        while True:
            if random_string not in self.cache:
                break
            else:
                random_string = rand_str()

        if len(self.cache) >= self.cache_size:
            self.cache = set()
            self.counter = 0

        self.cache.add(random_string)
        self.lock.release()
        return random_string
