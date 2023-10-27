# First task from the lecture

class Storage:
    storage = []
 
    def __init__(self, capacity):
        self.capacity = capacity
 
    def add_product(self, product: str):
        if self.capacity > 0:  # There is free space
            self.capacity -= 1
            Storage.storage.append(product)
 
    def get_products(self):
        return Storage.storage

    
# Second task by the lecture

class Storage:
    storage = []
 
    def __init__(self, capacity):
        self.capacity = capacity
 
    def add_product(self, product: str):
        if self.capacity > len(Storage.storage):  # There is free space
            Storage.storage.append(product)
 
    def get_products(self):
        return Storage.storage
    
# Third way by me

        